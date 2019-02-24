# importing the requests library 
import requests 
  
#get json file from api at given url
#uses GET requests
def api_request(URL):
	# sending get request and saving the response as response object 
	r = requests.get(url = URL) 
  
	# extracting data in json format 
	data = r.json() 
	return data

def get_contributer_statistics():
	# api-endpoint 
	URL = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/stats/contributors"

 	data = api_request(URL = URL)
	
  	# extract login and total contributions data 
  	extractedData = [
  		{
  			'login' : data[0]['author']['login'],
			'total' : data[0]['total']
  		}
  	]


  	return extractedData
	
	

get_contributer_statistics()