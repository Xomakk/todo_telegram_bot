import sqlite3


class Database:
    def __init__(self) -> None:
        self.__con = sqlite3.connect('data.db')

        self.__con.execute(
            """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    userId TEXT NOT NULL,
                    content TEXT NOT NULL,
                    status integer DEFAULT 0 NOT NULL 
                )
            """
        )

        self.__con.commit()

    def execute(self, sql_request):
        cur = self.__con.cursor()
        return cur.execute(sql_request)

    def commit(self):
        self.__con.commit()