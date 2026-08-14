import requests

def sendRequest(tempRequest: str):
    response = requests.get(tempRequest)
    return response.json()
