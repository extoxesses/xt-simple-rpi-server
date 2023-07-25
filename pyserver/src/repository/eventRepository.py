#!/usr/bin/env python3

from src.models.event import Event
from src.repository.baseRepository import BaseRepository

class EventRepository(BaseRepository):

	__FIND_LAST_EVENT = 'SELECT cpu_temp, is_alert, last_update, last_status_change_at FROM event ORDER BY id DESC LIMIT 1'
	__INSERT = 'INSERT INTO event(cpu_temp, is_alert, last_update, last_status_change_at) VALUES(?,?,?,?)'

	def __init__(self, database:str):
		super().__init__(database)

	def get_last_event(self):
		event = super(EventRepository, self).con.cursor().execute(EventRepository.__FIND_LAST_EVENT).fetchone()
		if event is not None:
			return Event.from_dict(event)
		return None
	
	def save(self, event:Event):
		self.con.cursor().execute(EventRepository.__INSERT, (event.cpu_temp, event.is_alert, event.last_update, event.last_event_change_at))
		self.con.commit()
