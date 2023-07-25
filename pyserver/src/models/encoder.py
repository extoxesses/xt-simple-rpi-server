from json import JSONEncoder

class CustomEncoder(JSONEncoder):
	
	def default(self, obj:any):
		if type(obj) is not list:
			return self.object_encoder(obj)
		else:
			return self.list_encoder(obj)

	def object_encoder(self, obj:any) -> dict:
		return obj.__dict__

	def list_encoder(self, obj:list) -> list:
		dict_array = []
		for e in obj:
			dict_array.append(e.__dict__)
		return dict_array
