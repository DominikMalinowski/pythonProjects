
# load JSON data 
jsonString = '{"name": "Sophie", "isCat": true, "miceCaught":0, "felineIQ":null}'

import json
jsonData = json.loads(jsonString)
print(jsonData)

# save data as JSON 
pythonString = {'name': 'Sophie', 'isCat': True, 'miceCaught':0, 'felineIQ': None}
import json
jsonDataFromString = json.dumps(pythonString)
print(jsonDataFromString)
