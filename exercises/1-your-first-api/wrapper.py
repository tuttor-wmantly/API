import requests

class Markit:
	def __init__(self):
		self.base_url = "http://dev.markitondemand.com/Api/v2/

	def company_search(self, string):
		res = requests.get(self.base_url+'api_path')
		pass

	def get_quote(self, string):
		pass

	
if __name__ == '__main__':
	markit = Markit()
	markit.company_search('Netflix')
