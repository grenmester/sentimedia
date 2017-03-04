import json

json_data = open('conversation.json').read()
j = json.loads(json_data)
messageList = []
for i in range(len(j)):
    try:
        tup = (j[i]['body'])
        messageList.append(tup)
    except:
        pass
