from .base import DelayedQuerySet


class DelayedUnionQuerySet(DelayedQuerySet):
    def __init__(self, *querysets, **kwargs):
        kwargs.setdefault('all', False)
        unexpected_kwarg = next((k for k in kwargs.keys() if k != 'all'), None)
        if unexpected_kwarg:
            raise TypeError(
                "received an unexpected keyword argument '{}'".format(
                    unexpected_kwarg
                )
            )
        return super(DelayedUnionQuerySet, self).__init__(*querysets, **kwargs)

    def _apply_operation(self):
        """
        Returs the union of all of the component querysets.
        """
        return self._querysets[0].union(*self._querysets[1:], **self._kwargs)

    def distinct(self):
        """
        Returns a new :class:`DelayedUnionQuerySet` instance that will
        select only distinct results.
        """
        clone = self._clone()
        clone._kwargs['all'] = False
        return clone

    def update(self, **kwargs):
        """
        Updates all elements in the component querysets, setting all the given
        fields to the appropriate values.  Returns the total number of
        (not-necessarily distinct) rows updated.
        """
        total_count = 0
        for queryset in self._querysets:
            total_count += queryset.update(**kwargs)
        return total_count
