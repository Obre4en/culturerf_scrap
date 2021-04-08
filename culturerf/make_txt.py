import json

with open('/home/obre4en/Documents/Scrapy/culturerf/dump_formated.json', 'r') as json_file:
    data = json.load(json_file)

poems = open('poems.txt', 'w')


for i in data['poems']:

    for title in i['title']:
        poems.write('\n')
        poems.write('\n')
        poems.write(title +'\n')
        poems.write('\n')


    for content in i['content']:
        x = content.strip()
        poems.write(x+'\n')

json_file.close()
