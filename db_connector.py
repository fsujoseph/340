import pymysql

host = 'classmysql.engr.oregonstate.edu'
user = 'cs340_riverami'
passwd = '6072'
db = 'cs340_riverami'


def connect_to_database():
    """
    Connects to database and returns database object
    """
    connection = pymysql.connect(host=host, user=user, passwd=passwd, database=db)
    return connection


def execute_query(connection=None, query=None, query_params=()):
    if connection is None:
        print("No connection to the database found! Have you called connect_to_database() first?")
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params))
    cursor = connection.cursor()
    cursor.execute(query, query_params)
    connection.commit()
    return cursor
