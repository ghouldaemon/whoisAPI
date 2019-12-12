#!/usr/bin/python3

import urllib.request
import json
import time


def input_ip():
    ip_info = input("Enter domain name or IP address for lookup: ")
    return ip_info


def who_is_api(x):
    api_url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_sjFVQFuCim9odvCodZziKCOJldWnf&domainName=' + x + '&outputFormat=JSON'
    return api_url


output_ip_info = input_ip()
api_result = who_is_api(output_ip_info)
time.sleep(1)
print("Getting information...")
time.sleep(1)
print("*******************************")
json_obj = urllib.request.urlopen(api_result)
read_json = json_obj.read().decode('utf8')

print(read_json)