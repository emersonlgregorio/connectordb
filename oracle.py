import json
import datetime
import oracledb

# oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_13")
oracledb.init_oracle_client(lib_dir=r"/app/oracle/instantclient_21_13")

class Oracle:

    def __init__(self, connection):
        user = connection['user']
        password = connection['password']
        dsn = connection['dsn']

        try:
            self.conn = oracledb.connect(user=user,
                                          password=password,
                                          dsn=dsn
                                         )

        except oracledb.Error as er:
            print('Connect failed, exiting')
            print(er)
            exit()

        # If no errors, print connected
        print('connected')

    def selectDb(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        column_names = list(map(lambda x: x.lower(), [
            d[0] for d in cursor.description]))
        # list of data items
        rows = list(cursor.fetchall())
        result = [dict(zip(column_names,row)) for row in rows]
        cursor.close()
        self.conn.close()
        # print(type(result))
        # print(result)
        # return json.dumps(result, indent=4, sort_keys=True, default=str)
        return result

    def executeDB(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.execute('commit')
        cursor.close()
        self.conn.close()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)