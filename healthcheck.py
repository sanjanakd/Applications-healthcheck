##!/usr/bin/python python

import requests

mylist = ['ec2-34-229-116-234.compute-1.amazonaws.com','ec2-34-204-5-106.compute-1.amazonaws.com']

for host in mylist:
    uri="http://"+host+":8085/rest/docker/health"

    try:
       req = requests.get(uri, timeout=300)	
       print "\n Application on"+host+"status", req
    except requests.exceptions.RequestException as e:
       print "\n Application is down:",e

