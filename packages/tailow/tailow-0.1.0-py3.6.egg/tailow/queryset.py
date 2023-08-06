from tailow.connection import Connection
from tailow.operators import Q

class QuerySet(object):

    def __init__(self, klass, limit=100, skip=0):
        self.klass = klass
        self._skip = skip
        self._offset = 0
        self._limit = limit
        self._filters = {}
        self._orders = []

    def coll(self):
        return Connection.get_collection(self.klass._collection)
    
    def skip(self, num):
        self._skip = num
        return self
    
    def limit(self, num):
        self._limit = num
        return self
    
    def offset(self, num):
        self._offset = num
        return self

    def filter(self, **kwargs):
        for field_name, value in kwargs.items():
            if field_name not in self.klass._fields:
                raise ValueError("Invalid field being queried: {}".format(field_name))
            field = self.klass._fields[field_name]
            self._filters[field_name] = field.to_son(value)
        return self

    def order(self, field_name, direction=None):
        self._orders.append((field_name, direction))
        return self
    
    async def find(self):
        """ Find all value regarding the filters """
        qus = Q(self._filters)
        values = self.coll().find(qus.query)
        if self._skip:
            values = values.skip(self._skip)
        if self._orders:
            values = values.sort(self._orders)
        values = await values.to_list(length=self._limit)
        return list(map(lambda x: self.klass(**x), values))
    
    async def get(self):
        qus = Q(self._filters)
        values = await self.coll().find_one(qus.query)
        if values:
            return self.klass(**values)
        return None
    
    async def count(self):
        qus = Q(self._filters)
        values = await self.coll() \
                       .find(qus.query) \
                       .count()
        return values