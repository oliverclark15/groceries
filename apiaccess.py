import requests

def search_product(product_name):
	search_term = product_name
	address = "https://api.nal.usda.gov/ndb/search/?format=json&q="+search_term+"&sort=r&max=5&offset=0&api_key=9RIhR3MpAsmRjawn5IIOZUSF3NfdtFhdJh8CDXw0"
	return requests.get(address)

def search_code(code):
	search_code_value = code
	print(search_code_value)
	code_address = "https://api.nal.usda.gov/ndb/reports/?ndbno="+search_code_value+"&type=b&format=json&api_key=9RIhR3MpAsmRjawn5IIOZUSF3NfdtFhdJh8CDXw0"
	return requests.get(code_address)

	

	