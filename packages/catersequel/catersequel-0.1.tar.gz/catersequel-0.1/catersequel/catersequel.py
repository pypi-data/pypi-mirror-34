from .base import Row, RowResult, Query, ExecuteResult


class Catersequel:
    def __init__(self, engine, autocommit=True):
        self._engine = engine
        self._autocommit = autocommit
        self._in_transaction = False
    
    def _commit(self):
        if self._autocommit and not self._in_transaction:
            self.commit()

    def _get_sql(self, query):
        if isinstance(query, Query):
            return query.as_sql()

        return query

    def _get_params(self, query, params):
        if not isinstance(query, Query):
            return params

        query_params = query.get_params()
        if query_params is None:
            return params

        if params is None:
            return query_params
        
        if type(query_params) != type(params):
            raise Exception("Diferent parameters format!")

        if isinstance(query_params, dict):
            query_params.update(params)
            return query_params

        query_params.extend(params)
        return query_params

    def query(self, query=None, params=None, **kwargs):
        q = Query()
        if params is None:
            params = kwargs

        if query is not None:
            q.append(query, params=params)

        return q
    
    def execute(self, query, params=None, **kwargs):
        if params is None:
            params = kwargs

        sql = self._get_sql(query)
        _params = self._get_params(query, params)
        data = self._engine.execute(sql, _params)
        self._commit()
        return ExecuteResult(**data)

    def fetchone(self, query, params=None, **kwargs):
        if params is None:
            params = kwargs

        sql = self._get_sql(query)
        _params = self._get_params(query, params)
        data = self._engine.fetchone(sql, _params)
        self._commit()
        if data is None:
            return None
        
        return Row(**data)

    def fetchall(self, query, params=None, **kwargs):
        if params is None:
            params = kwargs

        sql = self._get_sql(query)
        _params = self._get_params(query, params)
        data = self._engine.fetchall(sql, _params)
        self._commit()
        if data is None:
            return None

        return RowResult(data, row_class=Row)

    def reset(self):
        self._engine.reset()

    def commit(self):
        self._engine.commit()
        self._in_transaction = False

    def begin(self):
        self._engine.begin()
        self._in_transaction = True

    def mogrify(self, query, params=None, fnx=None):
        sql = self._get_sql(query)
        _params = self._get_params(query, params)
        data = self._engine.mogrify(sql, _params)
        if fnx is None:
            return data

        fnx(data)
