import json

class BaseResponse:
    
	def __init__(self, status:int, error:str = None, body:any = None):
		self.status = status
		self.error = error
		self.body = body

	def __repr__(self):
		return json.dumps(self.__dict__)
