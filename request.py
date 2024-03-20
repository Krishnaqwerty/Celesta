import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'X':27.730500,'Y':75.336116,'Depth':5})

print(r.json())


