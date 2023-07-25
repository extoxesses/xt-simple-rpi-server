from datetime import datetime
import json

class Event:

	def __init__(self, cpu_temp:int, is_alert:bool = False,
							 last_update:datetime = datetime.now(),
							 last_event_change_at:datetime = datetime.now()):
		self.cpu_temp = cpu_temp
		self.is_alert = is_alert
		self.last_update = last_update
		self.last_event_change_at = last_event_change_at

	@staticmethod
	def from_dict(event:dict) -> 'Event':
		last_update = datetime.strptime(event[2], '%Y-%m-%d %H:%M:%S.%f')
		if event[3] is not None:
			last_event_change_at = datetime.strptime(event[3], '%Y-%m-%d %H:%M:%S.%f')
		else:
			last_event_change_at = None
		return Event(event[0], event[1], last_update, last_event_change_at)


	def __str__(self) -> str:
		last_update_format = self.last_update.isoformat() if self.last_update is not None else None
		last_event_change_at_format = self.last_event_change_at.isoformat() if self.last_event_change_at is not None else None
		return f'cpu_temp: {self.cpu_temp}, is_alert: {self.is_alert}, last_update: {last_update_format}, last_event_change_at: {last_event_change_at_format}'

	def __repr__(self) -> str:
		return json.dumps(self.__dict__)
	
	def update(self, temp, is_alert) -> 'Event':
		now = datetime.now()
		if not self.is_alert == is_alert:
			self.last_event_change_at = now

		self.cpu_temp = temp
		self.is_alert = is_alert
		self.last_update = now

		return self
