import json
import random

#import pdb #Debug

from expects import expect, equal
from expects.matchers.built_in import be_above
from expects.matchers.built_in.have_keys import have_key

import pytest
from requests import *

import conftest
import factories

import requests
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

person_api_url='https://app.receptiviti.com/v2/api/person'
person_data = factories.get_person_data()
#person_data='{'gender': 1, 'name': 'John d5ea98c77924495a95c65b723c964f46 Doe', 'person_handle': 'cb481fdf968045a28d9092bb60024200'}'
auth_headers = conftest.auth_headers('58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U')

#auth_headers='{'X-API-KEY': '58cb2226e53b0b05af522850', 'X-API-SECRET-KEY': 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U'}'

requests.response = post(person_api_url, json=person_data, headers=auth_headers)