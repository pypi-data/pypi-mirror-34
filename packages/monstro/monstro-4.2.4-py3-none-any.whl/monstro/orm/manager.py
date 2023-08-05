# coding=utf-8

from .queryset import QuerySet


class Manager(object):

    def bind(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __getattr__(self, attribute):
        return getattr(QuerySet(self.model), attribute)

    async def create(self, **kwargs):
        return await self.model(data=kwargs).save()
