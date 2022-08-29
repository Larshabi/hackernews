import sys
import requests
import json


def hack():
    kids_list = []
    part_list = []
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    try:
        print('starting scraping')
        result = requests.get(url)
        data =  json.loads(result.text)
        new_result = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{data[0]}.json?print=pretty')
        new_data = json.loads(new_result.text)
        if 'kids' in new_data.keys() and 'parts' in new_data.keys():
            kids = new_data.pop("kids")
            new_url = 'http://127.0.0.1:8000/api/v1/'
            requests.post(new_url, new_data)
            for kid in kids:
                li = kids.pop()
                kids_list.append(li)
            parts = new_data.pop("parts")
            for part in parts:
                pa = parts.pop()
                part_list.append(pa)
        elif 'kids' in new_data.keys() and not 'parts' in new_data.keys():
            kids = new_data.pop("kids")
            new_url = 'http://127.0.0.1:8000/api/v1/'
            requests.post(new_url, new_data)
            for kid in kids:
                li = kids.pop()
                kids_list.append(li)
        elif 'parts' in new_data.keys() and not 'kids' in new_data.keys():
            parts = new_data.pop("parts")
            new_url = 'http://127.0.0.1:8000/api/v1/'
            requests.post(new_url, new_data)
                # parts_list.append(parts)
            for part in parts:
                pa = parts.pop()
                part_list.append(pa)
        else:
            new_url = 'http://127.0.0.1:8000/api/v1/'
            requests.post(new_url, new_data)       
        print('scraping done')
        return kids_list
    
    except Exception as e:
        print('The collection failed.')
        print(sys.exc_info())
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_tb.tb_lineno)
       
def kids(kid_list):
    comment_list = []
    for kid in kid_list:
        r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{kid}.json?print=pretty')
        new_r = json.loads(r.text)
        if 'kids' in new_r.keys():
            kids = new_r.pop('kids')
            requests.post('http://127.0.0.1:8000/api/v1/comments/', new_r)
            for k in kids:
                ki = kids.pop()
                comment_list.append(ki)
        requests.post('http://127.0.0.1:8000/api/v1/comments/', new_r)
    print('done')
    return comment_list

               
def hacker():
    kid = hack()
    if kid == None:
        return print('No connection to the API')
    kids(kid)
     