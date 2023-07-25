#!/usr/bin/env python3

import psutil

class SystemService:

	__GB_SCALE_FACTOR = pow(1024,3)
	__ALERT_TMP = 40

	def get_cpu_temp():
		sensors_temps = psutil.sensors_temperatures()
		cpu_thermal = sensors_temps.get('cpu_thermal', None)
		if cpu_thermal is None:
			return None
		else:
			return cpu_thermal[0][1]

	def get_disk():
		disk = psutil.disk_usage('/')
		return {
			'total': disk[0] / SystemService.__GB_SCALE_FACTOR,
			'used': disk[1] / SystemService.__GB_SCALE_FACTOR,
			'free': disk[2] / SystemService.__GB_SCALE_FACTOR,
			'percent': disk[3]
		}

	def get_network():
		net = psutil.net_if_stats()
		interfaces = []
		for eth in net.keys():
			elem = {
				'interface': eth,
				'speed': net[eth].speed,
				'unit': 'MB/s'
			}
			interfaces.append(elem)
		return interfaces

	def get_virtual_memory():
		mem = psutil.virtual_memory()
		return {
			'total': mem[0] / SystemService.__GB_SCALE_FACTOR,
			'available': mem[1] / SystemService.__GB_SCALE_FACTOR,
			'percent': mem[2],
			'used': mem[3] / SystemService.__GB_SCALE_FACTOR,
			'free': mem[4] / SystemService.__GB_SCALE_FACTOR
		}

	def is_alert(temperature):
		return True if temperature is None else temperature >= SystemService.__ALERT_TMP
