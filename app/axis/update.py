#!/usr/bin/env python
import requests

# requires authentication
result = requests.get('http://192.168.0.100/axis-cgi/admin/pwdgrp.cgi?action=update&user=joe&pwd=bar')