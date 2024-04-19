#Import your dependencies
import json
from hdbcli import dbapi
import datetime

class Hana:
    def __init__(self, connection):

        address = connection['address']
        port = connection['port']
        user = connection['user']
        password = connection['password']

        try :
            #Initialize your connection
            self.conn = dbapi.connect(
                address=address,
                port=port,
                user=user,
                password=password,
            )
        except dbapi.Error as er:
            print('Connect failed, exiting')
            print(er)
            exit()

        #If no errors, print connected
        print('connected')

    def selectDb(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        column_names = list(map(lambda x: x.lower(), [
            d[0] for d in cursor.description]))
        # list of data items
        rows = list(cursor.fetchall())
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        # print(type(result))
        # print(result)
        # return json.dumps(result, indent=4, cls=DateTimeEncoder, default=str)
        return result

    def executeDb(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)