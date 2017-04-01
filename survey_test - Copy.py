import test_people_api
import conftest, csv
import pandas as pd
import json
import uuid, random
from datetime import datetime

from requests import *
print 'start'

def get_headers(apikey, apisecret):
    header = {}
    if apikey:
        header['X-API-KEY'] = apikey
    if apisecret:
        header['X-API-SECRET-KEY'] = apisecret
    return header

def get_api_url(baseurl):
    return "{}/person".format(api_base_url(baseurl))

def api_base_url(baseurl):
    return "{}/v2/api".format(baseurl)

def open_csv (file_path, open_mode):
    u_cols = ['gender', 'nurse', 'text']
    df = pd.read_excel(file_path, names=u_cols)
    #print df.head()
    user_txt=df.iloc[:,-1]
    user_txt=df['text'].values
    s1=user_txt[0]
    #print 's1= %s' %(s1)
   
    return df

def parse_receptiviti (baseurl, apikey, apisecret, nurses):
    for index, row in nurses.iterrows():
        txt=row['text']
        gender=row['gender']
        attribs = {
            "language_content": txt,
            "content_source": 4,
            "content_handle": uuid.uuid4().hex,
            "content_date": datetime.now().isoformat(),
            "recipient_id": None,
            "content_tags": ['tag1', 'tag2', 'tag3'],
            'language': 'english'
        }
        person_data = {'name': "Nurse Survey".format(uuid.uuid4().hex), 'person_handle': uuid.uuid4().hex, 'gender': gender}
        person_data["content"] = attribs
        #print 'person_data=%s' %(attribs)
        auth_headers = get_headers(apikey, apisecret)
        person_api_url = get_api_url(baseurl)
        response = post(person_api_url, json=person_data, headers=auth_headers)
        response_json = json.loads(response.content)
        
        #print 'response_json=%s' %(response_json)
        imaginative = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["imaginative"]
        netspeak_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["netspeak_focus"]
        persuasive = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["persuasive"]
        liberal = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["liberal"]
        self_assured = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["self_assured"]

        print 'type nurses=%s' %(str(type(nurses)))
        nurses['imaginative']=imaginative
        
        #print 'imaginative=%s' %(imaginative)

    print 'NUR = %s' %(nurses)
    writer = pd.ExcelWriter('new.xlsx')
    nurses.to_excel(writer)
    writer.save()