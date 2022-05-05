import sqlite3
import json

class BasicDB:
    pass

class CustomDB:
    def __init__(self, db_path, table_name, table_schema):
        self.db_path = db_path
        self.table_name = table_name
        self.table_schema = table_schema
        self.conn = sqlite3.connect(self.db_path)

        self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({self.table_schema});")
        self.inc = self.conn.execute(f"SELECT * FROM information_schema.columns WHERE table_name = '{self.table_name}' LIMIT 1;")

    #TODO: PROTECT AGAINST SQL INJECTION!!!! URGENT!!!

    def pop(self, table, query): #pull latest in table
        return self.conn.execute(f"SELECT * FROM {table} WHERE {query} ORDER BY {self.inc} DESC LIMIT 1;")
    def pull(self, table, query): #pull oldest in table
        return self.conn.execute(f"SELECT * FROM {table} WHERE {query} LIMIT 1;") #fix this these sqls are garbage
    def stack(self, query): #push to table
        self.conn.execute(f"INSERT INTO {self.table_name} VALUES ({query});")#!!
    def execute(self, query):
        self.conn.execute(query)
        self.conn.commit()
    def close(self):
        self.conn.close()
