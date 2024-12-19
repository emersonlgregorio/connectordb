import json
import datetime
import oracledb
import os

try:
    if os.name == 'nt':  # 'nt' indica Windows
        oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_13")
    else:  # Qualquer outro sistema operacional (assumindo Linux)
        oracledb.init_oracle_client(lib_dir=r"/app/oracle/instantclient")
    print("Oracle client initialized successfully!")
except oracledb.DatabaseError as e:
    print("Error initializing Oracle client:", e)
    print("Make sure the Oracle client is installed and the path is correct.")

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


if __name__ == '__main__':
    connection = {
        "dsn": "172.20.2.2:1521/prod",  # Exemplo de DSN (IP:Porta/SID ou Service Name)
        "user": "agnew",
        "password": "agnew"
    }

    query = f"""
        SELECT * FROM AC_VW_NF_EXP_REMESSA WHERE DANFE_EXP LIKE '51241103262185000109550010000302161238966510'
    """

    nf_remessas = Oracle(connection).selectDb(query)

    print(nf_remessas)
