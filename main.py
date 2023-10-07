import psycopg2
import queryprocessor


def getDBConn():
    conn = psycopg2.connect(
        database="miniproject",
        user="admin",
        password="password",
        host="127.0.0.1",
        port="5432",
    )

    conn.autocommit = True
    return conn


if __name__ == "__main__":
    conn = getDBConn()
    queryprocessor = queryprocessor.QProcessor()

    query = """SELECT A2, A3 FROM R, S WHERE R.A2 = S.B2 AND R.A3 = S.B3;"""
    queryprocessor.processSelectQuery(query)
    queryprocessor.displayTokens()

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # cursor.execute(query)

    # result = cursor.fetchall()
    # for row in result:
    #     print(row)

    conn.close()
