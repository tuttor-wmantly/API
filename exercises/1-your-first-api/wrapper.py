import requests
 
class API:
	def __init__(self, base_url=None, token=None):
		self.base_url = base_URL or 'http://192.168.1.50:3000/'
		self.token = token or ''
		
		self.headers = {
			'auth-token': self.token
		}
		
	def __process_error(self, res):
		if res.status_code in range(200, 299):
			return None
		
		if res.status_code = 401:
			# do stuff for bad login
			
		return res.reason
		
	def get(self, path):
		res = request.get(self.base_url+path, headers=self.headers)
		err = self.__process_error(res)
		
		return res, err
	
	def post(self, path, json=None):
		res = request.post(self.base_url+path, headers=self.headers, json=json or {})
		err = self.__process_error(res)
		
		return res, err
		

	def login(self, username, password):
		data = {
			'username': username,
			'password': password
		}
		res, err = self.post('auth/login', data)
		
		if err:
			return err
		
		self.token = res.json().get('token')
		return true

