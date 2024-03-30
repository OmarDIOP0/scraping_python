from urllib import request
import json

url = 'http://www.official-joke-api.appspot.com/random_ten'
r= request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)
jokes=[]
for j in jsonData:
    setup = j['setup']
    punchline = j['punchline']
    jokes.append((setup,punchline)) 

print(jokes)
print(len(jokes))