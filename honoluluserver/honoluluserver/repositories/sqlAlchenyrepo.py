from honoluluserver.domain import station as st
from honoluluserver.domain import measurement as ms

from sqlalchemy import create_engine, text
import pandas as pd
import json 

actions_per_route = {
    "station": {
        "Query": "select * from station",
        "Data": st.Station
    },
    "precipitation": {
        "Query": """
            select date, prcp from 
            measurement
            where date >= date(
                (
                    select max(date) from measurement   
                )
                ,
                '-12 month'
            )
            """,
        "Data": ms.Measurement
    },
    "tobs": {
        "Query": """
            select ms.date as date, ms.tobs as tobs from 
            measurement as ms
            where 
            ms.date >= date(
                (
                    select max(date) from measurement
                )
                ,
                '-12 month'
            )
        """,
        "Data": ms.Measurement
    }
}

class SQLiteRepo:
    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if key in ['size', 'price']:
            return getattr(element[key], operator)(int(value))
        elif key in ['latitude', 'longitude']:
            return getattr(element[key], operator)(float(value))

        return getattr(element[key], operator)(value)

    def runQuery(self, sql):
        result = self.engine.connect().execute((text(sql)))
        return pd.DataFrame(result.fetchall(), columns=result.keys())

    def list(self, filters=None, route="station"):

        self.engine=create_engine('sqlite:///honoluluserver/repositories/hawaii.sqlite')

        reference = actions_per_route[route]

        lista = self.runQuery(reference["Query"]);

        result = json.loads(lista.to_json(orient='records'))

        return [reference["Data"].from_dict(r) for r in result]