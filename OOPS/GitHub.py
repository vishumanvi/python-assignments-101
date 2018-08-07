import urllib
from urllib.request import Request, urlopen

from urllib.error import URLError, HTTPError

class GitHub(object):

	def __init__(self,username):
		self.username = username
		self.base_url = "https://api.github.com/users/"
		self.gitURL = str(self.base_url) + str(self.username)


	def get_user_info(self):
		try:
			headers = {}
			headers[
			User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
			#req = urllib.request.Request(self.gitURL, headers=headers)
			req = Request(self.gitURL)
			res = urlopen(req)
			print(res)
		#	x = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
			# saveFile = open('noheaders.txt', 'w')
			# saveFile.write(str(x.read()))
			# saveFile.close()
			#print(str(resp.read()))
		except URLError as e:
			print(e.reason)


	def get_user_repos(self):
	# 	try:
	# #		response = request.urlopen(self.base_url + self.username + "/repos")
	# #		print(response)
	# 	except:
	# 		print ("Exception")
		pass


GH = GitHub("vishumanvi")
GH.get_user_info()
GH.get_user_repos()
