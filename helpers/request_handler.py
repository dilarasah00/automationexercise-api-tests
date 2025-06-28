import requests

def get_request(url,data = None, params= None):
    return requests.get(url,data=data, params=params)

def post_request(url,data = None, params= None):
    return requests.post(url,data=data, params=params)

def put_request(url,data = None, params= None):
    return requests.put(url,data=data, params=params)

def delete_request(url,data = None, params= None):
    return requests.delete(url,data=data, params=params)