#!/usr/bin/env python

import mechanize
import sys
import os
from requests import get


USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
LAST_IP_FILE="/tmp/LAST_IP"

LAST_IP = "0.0.0.0"
if os.path.exists(LAST_IP_FILE):
    with open(LAST_IP_FILE) as f:
        LAST_IP = f.readline()

ip = get('https://api.ipify.org').text
if LAST_IP == ip:
    print ('Public IP (unchanged):' + ip)
    sys.exit(0)

print ('Public IP :' + ip)

host = 'https://my.ionos.co.uk'
url = host + '/xml/config/Login'
domainUrl = host + '/xml/config/DomainOverview'

br = mechanize.Browser()
# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url)


br.select_form(nr=0)
br.form['oaologin.username'] = USERNAME
br.form['oaologin.password'] = PASSWORD
print (br.geturl())
br.submit()


print (br.geturl())
req = br.click_link(text='Manage Domain')
br.open(req)
print (br.geturl())

req = br.click_link(text='Modify DNS Settings')
br.open(req)
print (br.geturl())

req = br.click_link(text='A')
br.open(req)
print (br.geturl())


br.select_form(nr=0)
ip0 = br.find_control(name="record.value")
ip0.value = str(ip)
br.submit()


br.close()

with open(LAST_IP_FILE, "w") as f:
    f.write(str(ip))

print ("IP update complete.")
