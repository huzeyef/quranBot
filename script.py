import requests




url = "https://api.quran.com/api/v4/"
# url2= 'https://quranenc.com/api/v1/translation/sura/amharic_sadiq/1'
# r = requests.get(url2)
# d = r.json()
# for i in d['result']:
#     print(i['translation'])

def get_all_chapters():
    response = requests.get(url + 'chapters')
    if response.status_code == 200:
        data = response.json()  # If the response is in JSON format
        for i in data['chapters']:
            print(i['name_simple'])
    else:
        print(f"Request failed with status code: {response.status_code}")




def get_detail_of_a_single_chapter(id):
    response = requests.get(url + f'chapters/{id}/')
    if response.status_code == 200:
        data = response.json()  # If the response is in JSON format
        x = data['chapter']
        detail = [
            x['revelation_place'],
            x['revelation_order'],
            x['name_simple'],
            x['name_arabic'],
            x['verses_count'],
            x['pages'],
            x['translated_name']['name']
        ]
        info = f'The chapter {detail[2]}({detail[3]}) was revealed at {detail[0]}. The revelation order was {detail[1]} and its verses count is {detail[4]}'
        info2 = f'''
surah name: {detail[2]}
revelation place: {detail[0]}
verses count: {detail[4]}
revelation order: {detail[1]}
pages: {detail[5]}
English name: {detail[6]}    
'''
        print(info2)
    else:
        print(f"Request failed with status code: {response.status_code}")
get_detail_of_a_single_chapter(104)


