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
    u_cols = ['respondentid', 'collectorid', 'startdate', 'enddate', 'ipaddress', 'email', 'firstname', 'lastname', 'custom', 'age', 
              'gender', 'education', 'educationother', 'cert', 'certother', 'travel', 'facility', 'facilityother', 'employee',
              'zipcode', 'howlongyear', 'howlongmonth', 'satisfaction', 'adequatestaffing', 'turnover', 'cms', 'extovert', 'critical','dependable',
              'anxious', 'newexperience', 'reserved', 'sympathetic', 'careless', 'calm', 'convenitonal', 'text1', 'text2']
    df = pd.read_excel(file_path, names=u_cols)
    #df = pd.read_excel(file_path)
    #print df.head()   
    return df

def parse_receptiviti (baseurl, apikey, apisecret, nurses):
    for index, row in nurses.iterrows():
        txt1=row['text1']
        txt2=row['text2']
        txt=txt1+txt2
        gender=row['gender']
        print 'gender=%s' %(gender)
        if gender=='Male':
            gender=2
        elif gender=='Female':
            gender=1
        else: 
            gender=0
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
        print 'person_data=%s' %(attribs)
        auth_headers = get_headers(apikey, apisecret)
        person_api_url = get_api_url(baseurl)
        response = post(person_api_url, json=person_data, headers=auth_headers)
        response_json = json.loads(response.content)
        
        print 'response_json=%s' %(response_json)
        imaginative = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["imaginative"]
        netspeak_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["netspeak_focus"]
        persuasive = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["persuasive"]
        liberal = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["liberal"]
        self_assured = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["self_assured"]
        body_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["body_focus"]
        trusting = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["trusting"]
        organized = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["organized"]
        type_a = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["type_a"]
        intellectual = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["intellectual"]
        family_oriented = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["family_oriented"]
        disciplined = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["disciplined"]
        neuroticism = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["neuroticism"]
        cooperative = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["cooperative"]
        social_skills = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["social_skills"]
        openness = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["openness"]
        cold = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["cold"]
        adjustment = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["adjustment"]
        aggressive = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["aggressive"]
        depression = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["depression"]
        food_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["food_focus"]
        generous = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["generous"]
        sexual_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["sexual_focus"]
        power_driven = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["power_driven"]
        friend_focus = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["friend_focus"]
        extraversion = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["extraversion"]
        agreeableness = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["agreeableness"]
        happiness = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["happiness"]
        ambitious = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["ambitious"]
        friendly = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["friendly"]
        artistic = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["artistic"]
        independent = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["independent"]
        melancholy = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["melancholy"]
        workhorse = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["workhorse"]
        reward_bias = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["reward_bias"]
        energetic = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["energetic"]
        self_conscious = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["self_conscious"] 
        assertive = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["assertive"] 
        insecure = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["insecure"]
        impulsive = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["impulsive"]
        conscientiousness = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["conscientiousness"]
        thinking_style = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["thinking_style"]
        dutiful = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["dutiful"]
        empathetic = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["empathetic"]
        stressed = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["stressed"]
        health_oriented = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["health_oriented"]
        work_oriented = response_json["contents"][0]["receptiviti_scores"]["percentiles"]["work_oriented"]

        print 'type nurses=%s' %(str(type(nurses)))
        nurses['imaginative']=imaginative
        nurses['netspeak_focus']=netspeak_focus
        nurses['persuasive']=persuasive
        nurses['liberal']=liberal
        nurses['self_assured']=self_assured
        nurses['body_focus']=body_focus
        nurses['trusting']=trusting
        nurses['organized']=organized
        nurses['type_a']=type_a
        nurses['intellectual']=intellectual
        nurses['family_oriented']=family_oriented
        nurses['disciplined']=disciplined
        nurses['neuroticism']=neuroticism
        nurses['cooperative']=cooperative
        nurses['social_skills']=social_skills
        nurses['openness']=openness
        nurses['cold']=cold
        nurses['adjustment']=adjustment
        nurses['aggressive']=aggressive
        nurses['depression']=depression
        nurses['food_focus']=food_focus
        nurses['generous']=generous
        nurses['sexual_focus']=sexual_focus
        nurses['power_driven']=power_driven
        nurses['friend_focus']=friend_focus
        nurses['extraversion']=extraversion
        nurses['agreeableness']=agreeableness
        nurses['happiness']=happiness
        nurses['ambitious']=ambitious
        nurses['friendly']=friendly
        nurses['artistic']=artistic
        nurses['independent']=independent
        nurses['melancholy']=melancholy
        nurses['workhorse']=workhorse
        nurses['reward_bias']=reward_bias
        nurses['energetic']=energetic
        nurses['self_conscious']=self_conscious
        nurses['assertive']=assertive
        nurses['insecure']= insecure
        nurses['impulsive']=impulsive
        nurses['conscientiousness']=conscientiousness
        nurses['thinking_style']=thinking_style
        nurses['dutiful']=dutiful
        nurses['empathetic']=empathetic
        nurses['stressed']=stressed
        nurses['health_oriented']=health_oriented
        nurses['work_oriented']=work_oriented

       


        
        #print 'imaginative=%s' %(imaginative)

    print 'NUR = %s' %(nurses)
    writer = pd.ExcelWriter('new.xlsx')
    nurses.to_excel(writer)
    writer.save()