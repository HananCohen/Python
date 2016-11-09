#!/usr/bin/env python
###########################################################################################
# File name: vpc_runner.py
# Date: 8/11/2016
# Created By: Hanan Cohen <hanan.c80@gmail.com>
# 
#   Usage:
#     python vpc_runner 
#
###########################################################################################

# [Import external libs]
import boto
import boto.vpc
import time
import os
import sys

# [AWS Credentials Env setup ]

os.environ['AWS_SECRET_ACCESS_KEY'] = "my_var" 
os.environ['AWS_ACCESS_KEY_ID'] = "my_var"


# [Params] 

REGION_NAME = 'us-east-1'
AMI_ID = 'ami-01f05461'  # Ubuntu Server 14.04 LTS (HVM), SSD Volume Type


conn = boto.vpc.connect_to_region(REGION_NAME)
 
# [Create a VPC]
vpc = conn.create_vpc('10.0.0.0/16')
 
# [Configure the VPC to support DNS resolution and hostname assignment]
conn.modify_vpc_attribute(vpc.id, enable_dns_support=True)
conn.modify_vpc_attribute(vpc.id, enable_dns_hostnames=True)
 
# [Create an Internet Gateway]
gateway = conn.create_internet_gateway()
 
#[ Attach the Internet Gateway to our VPC]
conn.attach_internet_gateway(gateway.id, vpc.id)
 
# [Create a Route Table]
route_table = conn.create_route_table(vpc.id)
 
# [Create a size /24 subnet]
subnet = conn.create_subnet(vpc.id, '10.0.0.0/24')
 
# [Associate Route Table with our subnet]
conn.associate_route_table(route_table.id, subnet.id)
 
# [Create a Route from our Internet Gateway to the internet]
route = conn.create_route(route_table.id, '0.0.0.0/0', gateway.id)
 
# [Create a new VPC security group]
sg = conn.create_security_group('pycon_group',
                                'A group for PyCon',
                                vpc.id)
  
# [Authorize access to port 22 from anywhere]
sg.authorize(ip_protocol='tcp', from_port=22, to_port=22, cidr_ip='0.0.0.0/0')

# [Printing the details of new vpc]
 
print ('The you just created a new vpc in' + REGION_NAME +'with the following details:')
print ('vpc id:' + vpc.id)
print ('subnet id:' + subnet.id)
print ('routing table id:' + route_table.id)
print ('IGW id:' + gateway.id)

