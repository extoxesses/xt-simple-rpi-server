#!/usr/bin/env python

import sqlite3

class BaseRepository:

	def __init__(self, database:str):
		self.database = database
		self.con = sqlite3.connect(self.database)

	def close(self):
		self.con.close()
