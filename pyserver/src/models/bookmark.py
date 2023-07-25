import json

class Bookmark:
    
	def __init__(self, url:str, label:str, group:str):
		self.url = url
		self.label = label
		self.group = group

	def __repr__(self):
		return json.dumps(self.__dict__)
