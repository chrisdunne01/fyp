#!/usr/bin/env python
import requests
import sys

ipaddress = sys.argv[1]

# requires authentication
result = requests.get('http://root:pass@%s/axis-cgi/admin/restart.cgi' % ipaddress)
print(result)
