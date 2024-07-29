import psycopg2

class Postgres:
    def __init__(self, connection):
        #verify the architecture of Python

        print(connection)

        host = connection['host']
        database = connection['database']
        user = connection['user']
        password = connection['password']

        try :
            #Initialize your connection
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
            )
        except:
            print('Connect failed, exiting')
            exit()

        #If no errors, print connected
        print('connected')

    def dbSelect(self, query):
        conn = self.conn.cursor()
        conn.execute(query)
        column_names = list(map(lambda x: x.lower(), [
            d[0] for d in conn.description]))
        # list of data items
        rows = list(conn.fetchall())
        result = [dict(zip(column_names, row)) for row in rows]
        # print(result)
        conn.close()

        # print(rows)
        return result

    def executeDb(self, query):
        try:
            conn = self.conn.cursor()
            conn.execute(query)
            self.conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.close()
            return 1