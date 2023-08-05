import itertools
import os

import yaml

from mensor.constraints import CONSTRAINTS, And, Constraint
from mensor.utils import SequenceMap
from mensor.utils.registry import SubclassRegisteringABCMeta

from .stats import global_stats_registry
from .types import (Join, EvaluatedMeasures, MeasureEvaluator,
                    _Dimension, _Measure,
                    _StatisticalUnitIdentifier)

__all__ = ['MeasureProvider']


class MeasureProvider(MeasureEvaluator, metaclass=SubclassRegisteringABCMeta):
    """
    This is the base class that provides the API contract for all data sources
    in the `mensor` universe. Every `MeasureProvider` instance is a proxy to
    a different data source, allowing identifiers, measures and dimensions to
    be evaluated in different contexts; and the class exists simply to provide
    metadata about the data stored therein.

    Terminology:
        There are three classes of metadata: identifiers, dimensions and
        measures.

        Identifiers - Specifications of statistical unit types; i.e. the
            indivisible unit of an analysis. For example: "user", or "session",
            etc.
        Dimensions - Features associated with a statistical unit that are not
            aggregatable, such as "country" of a "user" or "platform" of a
            "client".
        Measures - Features associated with a statistical unit that are
            aggregatable (extensive), such as age, length, etc.

        While not relevant in the context of MeasureProviders, "metrics" are
        arbitrary functions of measures.

        Note that all measures and identifiers can be used as dimensions, but
        not vice versa.

    Defining Metadata:

        Setting and extracting metadata is done via a series of methods, which
        are similar for each type of metadata.

        Identifiers:
        - .identifiers
        - .provides_identifier
        - .unit_types
        - .identifier_for_unit
        - .foreign_keys_for_unit

        Dimensions:
        - .dimensions
        - .provides_dimension
        - .dimensions_for_unit
        - .provides_partition
        - .partitions_or_unit

        Measures:
        - .measures
        - .provides_measure
        - .measures_for_unit

    `MeasureProvider`s are registered into pools of `MeasureProvider`s called
    `MeasureRegistry`s. Once registered, the registry can evaluate measures
    transparently across all `MeasureProvider`s, handling the joins as necessary.
    """

    REGISTRY_KEYS = None

    @classmethod
    def _on_registered(cls, key):
        return cls.register_stats(key)

    @classmethod
    def register_stats(cls, key):
        pass

    @classmethod
    def from_yaml(cls, yml):
        if '\n' not in yml:
            with open(os.path.expanduser(yml)) as f:
                return cls.from_dict(yaml.load(f))
        else:
            return cls.from_dict(yaml.loads(yml))

    @classmethod
    def from_dict(cls, d):
        assert 'kind' in d
        assert d.get('role') in (None, 'provider')
        klass = cls.for_kind(d['kind'])
        instance = klass(
            name=d.get('name'),
            identifiers=d.get('identifiers'),
            measures=d.get('measures'),
            dimensions=d.get('dimensions'),
            provisions=d.get('provisions'),
            **d.get('opts', {})
        )
        return instance

    def __init__(self, name=None, *, identifiers=None, measures=None, dimensions=None,
                 provisions=None):
        # TODO: Support adding metadata like measure provider maintainer
        self.name = name

        self.identifiers = identifiers
        self.dimensions = dimensions
        self.measures = measures
        self.provisions = provisions

        self.opts.add_option('context', 'A dictionary specifying runtime specified context.', required=False, default={})

    def _get_dimensions_from_specs(self, cls, specs):
        dims = SequenceMap()
        if specs is None:
            return dims
        for spec in specs:
            dim = cls.from_spec(spec, provider=self)
            dims[dim] = dim
        return dims

    def __repr__(self):
        return '{}<{}>'.format(self.__class__.__name__, self.name)

    # Statistical unit specifications

    @property
    def identifiers(self):
        '''
        Dict matching type of abstract statistical unit ('user', 'user:guest', 'user:host',
        'reservation', etc) to a material internal id specification.
        To use a namespace, add a name after a ':' character,
        e.g. 'user:guest' or 'user:host', whereupon all of the features
        granted to a 'user' type will be prefixed in this context,
        e.g. 'guest:dim_country'
        '''
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        self._identifiers = self._get_dimensions_from_specs(_StatisticalUnitIdentifier, identifiers)

    def provides_identifier(self, unit_type=None, expr=None, desc=None, role='foreign', dummy=False):
        identifier = _StatisticalUnitIdentifier(unit_type, expr=expr, desc=desc, role=role, dummy=dummy, provider=self)
        self._identifiers.append(identifier)
        return self

    @property
    def unit_types(self):
        return set(self._identifiers.keys())

    def identifier_for_unit(self, unit_type):
        if isinstance(unit_type, _StatisticalUnitIdentifier):
            if unit_type.provider is self:
                return unit_type
            unit_type = unit_type.mask
        if unit_type in self.identifiers:
            return self.identifiers[unit_type]
        for identifier in sorted(self.identifiers, key=lambda x: len(x.name), reverse=True):
            if identifier.matches(unit_type):
                return identifier.with_mask(unit_type if isinstance(unit_type, str) else unit_type.name)
        raise ValueError("No such identifier: '{}'.".format(unit_type))

    def foreign_keys_for_unit(self, unit_type=None):
        if unit_type is None:
            return self.identifiers
        unit_type = self.identifier_for_unit(unit_type)

        foreign_keys = SequenceMap()
        for foreign_key in self.identifiers:
            if self._unit_has_foreign_key(unit_type, foreign_key):
                if unit_type.name == foreign_key:
                    foreign_key = foreign_key.with_mask(unit_type.mask)
                foreign_keys.append(foreign_key)
        return foreign_keys

    def reverse_foreign_keys_for_unit(self, unit_type=None):
        return {}

    def _unit_has_foreign_key(self, unit_type, foreign_key):
        return unit_type.is_unique

    # Dimension specifications

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        self._dimensions = self._get_dimensions_from_specs(_Dimension, dimensions)

    def provides_dimension(self, name=None, desc=None, expr=None, default=None, shared=False, requires_constraint=False):
        dimension = _Dimension(name, desc=desc, expr=expr, default=default, shared=shared, requires_constraint=requires_constraint, provider=self)
        self._dimensions.append(dimension)
        return self

    def dimensions_for_unit(self, unit_type=None, include_partitions=True):
        if unit_type is None:
            return self.dimensions
        unit_type = self.identifier_for_unit(unit_type)

        dimensions = SequenceMap()
        for dimension in self.dimensions:
            if (
                self._unit_has_dimension(unit_type, dimension)
                and (include_partitions or not dimension.partition)
            ):
                dimensions.append(dimension)
        return dimensions

    def _unit_has_dimension(self, unit_type, dimension):
        if dimension.partition:
            return True
        return unit_type.is_unique

    # Semantic distinction between standard dimension and partition
    # Since difference is semantically different but technically almost
    # identical, we expose them as two different things.
    # Note that partitions also appears as dimensions, since they are
    # functionally equivalent in most cases.
    # (partitions behave differently in joins TODO: document this difference)
    def provides_partition(self, name=None, desc=None, expr=None, requires_constraint=False):
        dimension = _Dimension(name, desc=desc, expr=expr, shared=True, partition=True, requires_constraint=requires_constraint, provider=self)
        self._dimensions.append(dimension)
        return self

    def partitions_for_unit(self, unit_type=None):
        return {
            dimension: dimension for dimension in self.dimensions_for_unit(unit_type) if dimension.partition
        }

    # Measure specifications

    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, measures):
        self._measures = self._get_dimensions_from_specs(_Measure, measures)

    def provides_measure(self, name=None, expr=None, default=None, desc=None, shared=False, distribution='normal'):
        measure = _Measure(name, expr=expr, default=default, desc=desc, shared=shared, distribution=distribution, provider=self)
        self._measures.append(measure)
        return self

    def measures_for_unit(self, unit_type=None):
        if unit_type is None:
            return self.measures
        unit_type = self.identifier_for_unit(unit_type)

        measures = SequenceMap()
        for measure in self.measures:
            if self._unit_has_measure(unit_type, measure):
                measures.append(measure)
        return measures

    def _unit_has_measure(self, unit_type, measure):
        return unit_type.is_unique

    @property
    def provisions(self):
        return {
            name: kwargs['source'].get_strategy(
                unit_type=kwargs['unit_type'],
                measures=kwargs['measures'],
                segment_by=kwargs['segment_by'],
                where=kwargs['where'],
                **kwargs['opts']
            )
            for name, kwargs in self._provisions.items()
        }

    @provisions.setter
    def provisions(self, provisions):
        self._provisions = provisions or {}

    def requires_provision(self, name, unit_type, measures=None, segment_by=None, where=None,
                           source=None, **opts):
        assert 'dry_run' not in opts, "Cannot hard specify 'dry_run' in provision options."
        self._provisions[name] = {
            'unit_type': unit_type,
            'measures': measures,
            'segment_by': segment_by,
            'where': where,
            'source': source,
            'opts': opts
        }
        return self

    # Measure evaluation
    def _prepare_evaluation_args(f):
        def wrapped(self, unit_type, measures=None, segment_by=None, where=None, joins=None, stats_registry=None, stats=True, covariates=False, **opts):
            unit_type = self.identifier_for_unit(unit_type)
            measures = {} if measures is None else self.resolve(unit_type=unit_type, features=measures, role='measure')
            segment_by = {} if segment_by is None else self.resolve(unit_type=unit_type, features=segment_by, role='dimension')
            where = Constraint.from_spec(where)
            joins = joins or []
            stats_registry = stats_registry or global_stats_registry
            opts = self.opts.process(**opts)
            return f(self, unit_type, measures=measures, segment_by=segment_by, where=where, joins=joins, stats_registry=stats_registry, stats=stats, covariates=covariates, **opts)
        return wrapped

    @_prepare_evaluation_args
    def evaluate(self, unit_type, measures=None, segment_by=None, where=None,
                 joins=None, stats_registry=None, stats=True, covariates=False, **opts):
        """
        This method evaluates the requested `measures` in this MeasureProvider
        segmented by the dimensions in `segment_by` after joining in the
        joins in `joins` and subject to the constraints in `where`; treating
        `unit_type` objects as indivisible.

        Parameters:
            unit_type (str, _StatisticalUnitIdentifier): The unit to treat as
                indivisible in this analysis.
            measures (list<str, _Measure>): The measures to be calculated.
            segment_by (list<str, _Feature>): The dimensions by which to segment
                the measure computations.
            where (dict, list, tuple, BaseConstraint): The
                constraints within which measures should be computed.
            stats (bool): Whether to keep track of the distribution of the
                measures, rather than just their sum.
            covariates (bool, list<tuple>): Whether to compute all covariates
                (if bool) or else a list of tuples of measures within which
                all pairs of covariates should be computed.
            opts (dict): Additional arguments to be passed onto `._evalaute`
                implementations.

        Returns:
            EvaluatedMeasures: A wrapper around the dataframe of the results of the computation.
        """
        from mensor.backends.pandas import PandasMeasureProvider  # We need this for some pandas transformations

        # Split joins into compatible and incompatible joins; 'joins_pre' and
        # 'joins_post' (so-called because compatible joins occur before any
        # computation in this method).
        joins_pre = [j for j in joins if j.compatible]
        joins_post = [j for j in joins if not j.compatible]

        # If there are post-joins, we will need to add the 'count' measure
        # (assuming it has not already been requested), so that we can weight
        # post-joins appropriately.
        if len(joins_post) > 0 and 'count' not in measures:
            count_measure = self.measures['count'].as_private
            measures[count_measure] = count_measure

        # If there are post-joins, we need to ensure that the pre- operations
        # that happen within the `._evaluate` method do not suppress prematurely
        # private fields that are necessary to later join in the post-joins.
        # We therefore modify the privacy of fields for the `._evaluate` stage
        # depending on whether they are needed later. We also suppress and
        # external fields not provided by pre-joins, so that `._evaluate`
        # instances need not concern themselves with them.

        # Moreover, if there are post-joins and where constraints, some of the constraints
        # may need to be applied after post-joins. As such, we split the where
        # constraints into where_pre and where_post.
        measures_pre, segment_by_pre, where_pre, measures_post, segment_by_post, where_post = (
            self._compat_fields_split(measures, segment_by, where, joins_post=joins_post)
        )

        # Allow MeasureProvider instance to evaluate all pre- computations.
        result = self._evaluate(
            unit_type,
            measures_pre,
            segment_by=segment_by_pre,
            where=where_pre,
            joins=joins_pre,
            stats_registry=stats_registry,
            stats=stats and len(joins_post) == 0,
            covariates=covariates,
            **opts
        )

        if len(joins_post) > 0:

            # Join in precomputed incompatible joins
            # TODO: Clean-up how joined measures are detected (remembering measure fields have suffixes)
            joined_measure_fields = set()
            if len(joins_post) > 0:
                for join in joins_post:
                    joined_measure_fields.update(join.object.measure_fields)
                    result = result.merge(
                        join.object.raw,
                        left_on=join.left_on,
                        right_on=join.right_on,
                        how=join.how
                    )

            # Check columns in resulting dataframe
            expected_columns = _Measure.get_all_fields(measures_post, unit_type=unit_type, rebase_agg=True, stats_registry=stats_registry, stats=False) + [f.via_name for f in segment_by_post]
            excess_columns = set(result.columns).difference(expected_columns)
            missing_columns = set(expected_columns).difference(result.columns)
            if len(excess_columns):  # remove any unnecessary columns (such as now used join keys)
                result = result.drop(excess_columns, axis=1)
            if len(missing_columns):
                raise RuntimeError('Data is missing columns: {}.'.format(missing_columns))

            # All new joined in measures need to be multiplied by the count series of
            # this dataframe, so that they are properly weighted.
            if len(joined_measure_fields) > 0:
                result = result.apply(lambda col: result['count|raw'] * col if col.name in joined_measure_fields else col, axis=0)

            result = PandasMeasureProvider._finalise_dataframe(
                df=result, unit_type=unit_type, measures=measures_post, segment_by=segment_by_post,
                where=where_post, stats=stats, stats_registry=stats_registry,
                rebase_agg=False, reagg=False
            )

        return EvaluatedMeasures.for_measures(result, stats_registry=stats_registry)

    def _compat_fields_split(self, measures, segment_by, where, joins_post=None):
        """
        This method splits measures and segment_by dictionaries into two,
        corresponding to pre- and post- computation. The pre- field modify
        private statuses to prevent loss of join keys, and suppress
        external fields in joins_post. The second set are remove all features
        that were private in the pre- computation phase.

        It also splits where constraints such that constraints are applied
        as early as possible while still being semantically correct.
        """
        if len(joins_post) == 0:
            return measures, segment_by, where, None, None, None

        join_post_fields = []  # TODO: Use dictionaries for performance
        for join in joins_post:
            join_post_fields.extend([m.as_via(join.join_prefix) for m in join.measures])
            join_post_fields.extend([d.as_via(join.join_prefix) for d in join.dimensions])

        join_left_post_keys = list(itertools.chain(*[  # TODO: Use dictionaries for performance
            join.left_on
            for join in joins_post
        ]))

        join_right_post_keys = list(itertools.chain(*[  # TODO: Use dictionaries for performance
            join.right_on
            for join in joins_post
        ]))

        # Process constraint clauses
        where_pre = []
        where_post = []

        def add_constraint(op):
            if len(set(op.dimensions).intersection([
                d if isinstance(d, str) else d.via_name
                for d in (join_post_fields + join_right_post_keys)
            ])) > 0:
                where_post.append(op)
            else:
                where_pre.append(op)

        if where:
            if where.kind is CONSTRAINTS.AND:
                for op in where.operands:
                    add_constraint(op)
            else:
                add_constraint(where)

        where_pre = And.from_operands(where_pre)
        where_post = And.from_operands(where_post)

        # Process measures and dimensions
        def features_split(features, extra_public_keys=[]):
            pre = {}
            post = {}

            for feature in features:
                if feature.external and feature in join_post_fields:
                    post[feature] = feature
                    continue
                if feature.private and feature in (join_left_post_keys + extra_public_keys + (where_post.dimensions if where_post else [])):
                    pre[feature.as_public] = feature.as_public
                else:
                    pre[feature] = feature
                if not pre[feature].private:
                    post[feature] = feature

            return pre, post

        measures_pre, measures_post = features_split(measures, [self.resolve(unit_type=None, features='count', role='dimension')])
        segment_by_pre, segment_by_post = features_split(segment_by)

        return measures_pre, segment_by_pre, where_pre, measures_post, segment_by_post, where_post

    def _evaluate(self, unit_type, measures=None, segment_by=None, where=None,
                  joins=None, stats_registry=None, stats=True, covariates=False, **opts):
        """
        MeasureProviders must in their _evaluate function (in logical order):

        - Extract the nominated measures and dimensions that are not marked 'external'
          from their associated data store, including from any provisions.
        - Join in any compatible joins based on their intermediate representation, along
          with any fields from these joins marked as 'external' in the the appropriate
          dictionaries.
        - Apply any constraints passed in through `where`.
        - Suppress any dimensions / measures marked as private.
        - * If `stats` is `True`, apply the statistical aggregations appropriate
          for each field, as well as generating any requested covariates (only
          ever required if there are no incompatible joins that will be merged
          in later).

        To assist with this, the base MeasureProvider.evaluate function commits to:
        - Preparing all values passed to _evaluate in the native data types of mensor.
        - Filtering down any external measures / dimensions to those that are needed
          for compatible joins.
        - Filtering any constraints down to those that can be applied within the
          MeasureProvider.
        - Adjusting the privacy of measures / dimensions such that all fields marked
          private within the _evaluate call can be safely suppressed without breaking
          the functionality of the parent `evaluate` method and future
          incompatible joins.
        """
        raise NotImplementedError("Generic implementation not implemented.")

    @_prepare_evaluation_args
    def get_ir(self, unit_type, measures=None, segment_by=None, where=None,
               joins=None, stats_registry=None, stats=True, covariates=False, **opts):
        # Get intermediate representation for this evaluation query
        if not all(isinstance(j, Join) and j.compatible for j in joins):
            raise RuntimeError("All joins for IR must be compatible with this provider.")
        return self._get_ir(
            unit_type=unit_type,
            measures=measures,
            segment_by=segment_by,
            where=where,
            joins=joins,
            stats_registry=stats_registry,
            stats=stats,
            covariates=covariates,
            **opts
        )

    def _get_ir(self, unit_type, measures=None, segment_by=None, where=None,
                joins=None, stats_registry=None, stats=True, covariates=False, **opts):
        raise NotImplementedError

    # Compatibility
    def _is_compatible_with(self, provider):
        '''
        If this method returns True, this MeasureProvider can take responsibility
        for evaluation and/or interpreting the required fields from the provided
        provider; otherwise, any required joins will be performed in memory in
        pandas.
        '''
        return False

    # Constraint interpretation
    @property
    def _constraint_maps(self):
        """
        A dictionary of mappings from CONSTRAINTS types to an internal
        representation useful to apply the constraint.
        """
        return {}

    def _constraint_map(self, kind):
        """
        Parameters:
            kind (CONSTRAINTS): The type of constraint for which to extract the
                internal represtation of the mapper.
        """

        if kind not in self._constraint_maps:
            raise NotImplementedError("{} cannot apply constraints of kind: `{}`".format(self.__class__.__name__, kind))
        return self._constraint_maps[kind]
