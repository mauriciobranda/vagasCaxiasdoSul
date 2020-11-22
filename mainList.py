#Webscrapping vagas Guppy

import requests, json
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def consultaVagas(companycode):

    if companycode == 1:
        companyName = 'randon'
    elif companycode == 2:
        companyName = 'soprano'
    elif companycode == 3:
        companyName = 'totvs'
    elif companycode == 4:
        companyName = 'promob'
    else:
        print ("4 - Got a false expression value")

    url = 'https://'+companyName+'.gupy.io/'

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    # find a list of all span elements
    spans = soup.find_all('span', {'class' : 'title'})

    # create a list of lines corresponding to element texts
    lines = [span.get_text() for span in spans]

    #coletando job link
    data = soup.findAll('a',attrs={'class':'job-list__item'})
    #coletando kob description
    spans = soup.findAll('span', {'class' : 'title'})

    my_listA = []
    for a in data:
        links = a.findAll('href')
        my_listA.append(a['href'])
        #print(a['href'])
    
    

    my_listS = []
    for a in spans:
        links = a.findAll('title')
        my_listS.append(a.text)

        #print(a.text)

    a_dict = {}
    keyList = ["title", "url"]
    for i in keyList: 
        a_dict[i] = None

    finalList = []
    conta = 0
    while conta < len(my_listA):
        #finalList.append(my_listS[conta]+';'+url+my_listA[conta])
        
        a_dict = {'title': my_listS[conta],'url': url+my_listA[conta]}

        '''a_dict["title"].append(my_listS[conta])
        a_dict["url"].append(url+my_listA[conta])'''
        finalList.append(dict(a_dict))
        #print(a_dict)
        conta += 1
    
    return finalList

your_list_as_json = json.dumps(consultaVagas(1),indent=1, sort_keys=True, ensure_ascii=False) 
#  print(your_list_as_json) 


y = json.loads(your_list_as_json)

#print(y["title"][1])

    

#print('[%s]' % ', '.join(map(str, consultaVagas(2))))

