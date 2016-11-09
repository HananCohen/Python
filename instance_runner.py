#!/usr/bin/env python
# encoding: utf-8
###########################################################################################
# File name: instance_runner.py
# Date: 8/11/2016
# Created By: Hanan Cohen <hanan.c80@gmail.com>
# 
#   Usage:
#     python instance_runner.py
#
###########################################################################################

import argparse
import logging
import string
import sys

from boto import vpc, exception

from lib.aws_location import LocationData
from lib.aws_util import check_config

# Get subnet info 

def get_subnets(connection, vpc_id):
  """Function that returns all subnets within a given AWS VPC.
  :connection: AWS Connection.
  :vpc_id: VPC Identifier.

  """
  return connection.get_all_subnets(filters={'vpc_id': vpc_id})


def format_data(region, vpc_id, vpc_subnet, subnets):
  """Function that outputs region data based on template.

  :region: EC2 Region.
  :vpc_id: VPC Identifier.
  :vpc_subnet: Subnet allocated to VPC.
  :subnets: Subnets defined within VPC.

  todo:: Serialization. (yaml/json)
  """
  with open('vpc_subnets.tmpl') as f:
    templ = string.Template(f.read())

  region_dict = {}
  region_dict['region'] = region
  region_dict['vpc_id'] = vpc_id
  region_dict['vpc_subnet'] = vpc_subnet
  region_dict['subnets'] = ', '.join(subnets)

  print templ.safe_substitute(region_dict)


def parse_args():
  parser = argparse.ArgumentParser(
      description='Script for obtaining VPC Subnet information.')

  group = parser.add_mutually_exclusive_group()

  group.add_argument("-d", "--debug",
      help="Enable debug messages",
      action="store_true")

  group.add_argument("-v", "--verbose",
      help="Enable verbose messages",
      action="store_true")

  args = parser.parse_args()

  if args.debug:
    logging.basicConfig(level=logging.DEBUG)
  elif args.verbose:
    logging.basicConfig(level=logging.INFO)
  else:
    logging.basicConfig(level=logging.CRITICAL)

def main():
  parse_args()

  try:
    check_config()
  except EnvironmentError as e:
    print("Error: Could not open config file: {}".format(e))
    sys.exit(1)

  loc = LocationData()

  for region in loc.get_regions():
    try:
      connection = vpc.connect_to_region(region)
      for vpc_raw in loc.get_vpcs_raw(connection):
        vpc_id = str(vpc_raw).split(':')[1]
        subnets = []
        for subnet_id in get_subnets(connection, vpc_id):
          subnets.append(subnet_id.cidr_block)   
      format_data(region, vpc_id, vpc_raw.cidr_block, subnets)
    except exception.EC2ResponseError as e:
      logging.error("EC2Error: {}".format(e))
      continue

if __name__ == '__main__':
  main()
  
  
  
  


# Get subnet id to create instance  



# Create instance in the new vpc

reservation = conn.run_instances(
    image_id=base_ami,
    key_name=<name_of_key>,
    security_group_ids=['<sg-12345678>'],
    subnet_id=<id_subnet>)