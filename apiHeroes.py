import requests
from pprint import pprint
''''Задачу про яндекс диск не стал перекатывать - ее разобрали, все работет, хотя пока и не все ясно'''
#
#
# resp = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json").json()
#
#
#
# my_list = []
# result_list = []
# for item in resp:
#
#     if item['name'] == 'Hulk' or item['name'] == 'Captain America' or item['name']=='Thanos':
#         my_list.append(item)
#
# for item in my_list:
#
#     result_list.append([item['powerstats']['intelligence'],item['name']])
#
#
#
#
# print(f'Наиболее интеллектуальный герой из {result_list[0]},{result_list[1]}, {result_list[2]} - {max(result_list)}')



stack_responce = requests.get('https://api.stackexchange.com/search/advanced?pagesize=1&fromdate=1672185600&todate=1672358400&&tagged=python&site=stackoverflow.com').json()

pprint(stack_responce)

