#!/usr/bin/env python
import requests
import sys

ipaddress = sys.argv[1]
user = sys.argv[2]
# requires authenticationc
# result = requests.get('http://root:pass@192.168.0.100/axis-cgi/admin/pwdgrp.cgi?action=remove&user=CHRISCHRIS')
result = requests.get('http://root:pass@%s/axis-cgi/admin/pwdgrp.cgi?action=remove&user=%s' % (ipaddress, user))
print(result)

import urllib
# urllib.urlopen('http://root:pass@%s/axis-cgi/admin/pwdgrp.cgi?action=remove&user=THISISATEST' % ipaddress)