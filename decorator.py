from Connection import Connection


def connection(func):
    def wrapper(msg):
        conn = Connection().connection()
        conn.autocommit(True)
        func(conn, msg)
        conn.close()
    return wrapper
