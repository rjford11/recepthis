import requests

r = requests.get('https://www.google.com')

r.text

r.encoding

print 'test = %s' %(r.text)