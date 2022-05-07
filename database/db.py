import sqlite3
import json

class BasicDB:
	def __init__(self, db_path, table_name, table_schema):
		self.db_path = db_path
		self.table_name = table_name
		self.table_schema = table_schema
		self.conn = sqlite3.connect(self.db_path)

		self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER AUTO INCREMENT, {self.table_schema});")

	#TODO: PROTECT AGAINST SQL INJECTION!!!! URGENT!!!
	#todo: add logging

	def pop(self, table, query): #pull latest in table
		return self.conn.execute(f"SELECT * FROM {table} WHERE {query} ORDER BY id DESC LIMIT 1;")
	def pull(self, table, query): #pull oldest in table
		return self.conn.execute(f"SELECT * FROM {table} WHERE {query} LIMIT 1;") #fix this these sqls are garbage
	
	def stack(self, table, query): #push to table
		self.conn.execute(f"INSERT INTO {table} VALUES ({query});")#!!
	def check(self, table, query):
		return self.conn.execute(f"SELECT * FROM {table} WHERE {query} LIMIT 1;")

class CustomDB(BasicDB):
	def __init__(self, db_path, table_name, table_schema):
		self.db_path = db_path
		self.table_name = table_name
		self.table_schema = table_schema
		self.conn = sqlite3.connect(self.db_path)

		self.conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({self.table_schema});")
	
	def execute(self, query):
		self.conn.execute(query)
