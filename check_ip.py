import iptools
from iptools import IpRangeList, netmask2prefix, validate_cidr
import os

r = IpRangeList('202.202.0.0/16')

def validate_sg_ip():
    print (r)
    iip = raw_input('Enter your IP: ')
    print validate_cidr(iip)
    if rip in r:
        print ("Your input IP is accepted list of ips")
    else:
        print ("Sorry, your IP is not allowed")

if __name__ == '__main__':
    validate_sg_ip()
