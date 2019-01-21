#!/usr/bin/env python
import requests

# requires authentication
result = requests.get('http://root:pass@192.168.0.100/axis-cgi/admin/systemlog.cgi')
print(result)
