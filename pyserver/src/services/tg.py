#!/usr/bin/env python3

from datetime import datetime
from telegram import Bot

from models.event import Event
from repository.eventRepository import EventRepository
from services.system import SystemService


class TelegramService:
        
    # 10 minutes
	__ALERT_ELAPSED_TIME = 600
  
	__ALERT_MSG  = "ALERT! {}'s CPU temperature is above {}°C"
	__ALERT_ERR  = "ERROR! Error risen while trying check state on {}: {}"
	__CRITIC_MSG = "CRITIC! Temperature is too high (now {}) since {}"
	__OK_MSG = "Temperature under security threshold"

	def __init__(self, hostname:str, database:str, bot:Bot):
		self.hostname = hostname
		self.database = database

	def get_check_message(self) -> str:
		msg = None
		try:
			repository = EventRepository(self.database)
			last_event = repository.get_last_event()
			
			cpu_temp = SystemService.get_cpu_temp()
			if (last_event is None):
				last_event = Event(cpu_temp, False, datetime.now(), datetime.now())
			print(f'> Last status: ${str(last_event)}')

			is_alert = SystemService.is_alert(cpu_temp)
			if (is_alert):
				msg = self.__get_alert_msg(cpu_temp, last_event)
			elif (last_event.is_alert):
				msg = TelegramService.__OK_MSG
			
			current_status = last_event.update(cpu_temp, is_alert)
			repository.save(current_status)

		except Exception as e:
			err = e.message if hasattr(e, 'message') else str(e)
			msg = TelegramService.__ALERT_ERR.format(self.hostname, err)

		finally:
			repository.close()
		
		print(msg)
		return msg


	def __get_alert_msg(self, temperature:float, last_event:Event) -> str:
		last_event_change_at = last_event.last_event_change_at if last_event.last_event_change_at is not None else datetime.now()
		elapsed = datetime.now() - last_event_change_at
		if (elapsed.total_seconds() < TelegramService.__ALERT_ELAPSED_TIME):
			altmsg = TelegramService.__ALERT_MSG.format(self.hostname, temperature)
		else:
			if (last_event.last_event_change_at is None):
				last_event_change_at = 'unknown'
			else:
				altmsg = TelegramService.__CRITIC_MSG.format(temperature, last_event_change_at.isoformat())

		return altmsg
