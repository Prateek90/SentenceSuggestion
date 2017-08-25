import json

with open('/home/prateek/sample_conversations.json') as data_file:
    OrignalData=json.load(data_file)

service_data=list()

for data in OrignalData['Issues']:
    for messages in data['Messages']:
        if messages['IsFromCustomer']==False:
            service_data.append(messages['Text'])