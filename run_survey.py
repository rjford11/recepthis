import survey_test
import numpy
import requests
import logging

print 'Open CSV'

#try:
#    import http.client as http_client
#except ImportError:
    # Python 2
#    import httplib as http_client
#http_client.HTTPConnection.debuglevel = 1

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

#survey_test.open_csv ('C:\Users\ford1\work\receptiviti\survey_test.csv','rb')

#survey_test.open_csv ('C:\Users\ford1\work\receptiviti\survey_test.xlsx','rb')

nurses=survey_test.open_csv ('Sheet_1.xls','rb')
#print 'NURSES=%s' %(nurses)
survey_test.parse_receptiviti ('https://app.receptiviti.com', '58cb2226e53b0b05af522850', 'mVMB00cqeKB5rJwkfQC2fKsJyL1ck6NZlQoWPfHQG1U', nurses)