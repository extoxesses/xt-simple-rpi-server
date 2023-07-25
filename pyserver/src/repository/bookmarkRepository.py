#!/usr/bin/env python3

from src.repository.baseRepository import BaseRepository


class BookmarkRepository(BaseRepository):

	def __init__(self, database:str):
		super().__init__(database)

	def get_all_bookmarks(self):
		return self.con.cursor().execute('SELECT * FROM bookmark').fetchall()
