# See URL = https://pixe.la/v1/users/javedmomin1234/graphs/graph1.html
import requests
import datetime
USERNAME = "javedmomin1234"
TOKEN = "ded4refer4r3r3sddc"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
params = { 
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# HTTP POST Method Used to Directly Create Account Using Python
#response = requests.post(url = pixela_endpoint, json=params)
#print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "Hours",
    "type" : "int",
    "color": "momiji"
    }
headers = {
    "X-USER-TOKEN" : TOKEN,
}
# HTTP POST Method Used to Directly Create Graphs Using Python
#graph = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
#print(graph.text)
today = datetime.datetime.now()
pixel_creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How Many Hours did you code Today?\n"),
}

response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers = headers)
print(response.text)

#UPDATE ENDPOINT
#update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#new_pixel_data = {
#    "quantity": "10"
#}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

#DELETE ENDPOINT
#delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_endpoint,headers=headers)
#print(response.text)
