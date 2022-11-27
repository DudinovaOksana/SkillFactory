import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)
print(texts[0], '\n')
print(type(r.content))

