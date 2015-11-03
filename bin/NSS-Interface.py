#!/usr/bin/env python3.3
# -*- coding: utf8 -*-
#
# Management Interface
#
# Copyright (c) 2015    NorthernSec
# Copyright (c) 2015    Pieter-Jan Moreels

# Imports
import os
import sys
runpath=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runpath, '..'))

import argparse
from lib.DatabaseLayer import addTokens, selectAllFrom
from lib.Toolkit import is_hex
from lib.Objects import HoneyToken

if __name__=='__main__':
  description='''Management script'''

  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('-L', action='store_true', help='List')
  parser.add_argument('-A', action='store_true', help='Add')
  parser.add_argument('-t', metavar='token',     help='Token to add or remove')
  parser.add_argument('-a', metavar='action',    help='Action to take when triggered (accept/block/drop)')
  parser.add_argument('-d', metavar='database',  help='Database to be modified')
  parser.add_argument('-I', action='store_true', help='Case Insensitive')
  parser.add_argument('-B', action='store_true', help='Binary Blob (enter in hex)')
  parser.add_argument('-N', action='store_true', help='Notify - Alert the user right away')
  args = parser.parse_args()
  
  #Defaults
  _DEFAULT_ACTION = "drop"
  _DEFAULT_DB = "NSS.lite"
  _ACCEPTED_ACTIONS=["accept", "drop", "block"]
  _TABLES_TO_PRINT=["HoneyTokens"]
  
  db=args.d if args.d else _DEFAULT_DB
  
  if args.L:
    for x in _TABLES_TO_PRINT:
      print("="*80 + "\n%s\n"%(x) + "="*80)
      for y in selectAllFrom(db, x):
        sys.stdout.write("|  ")
        for z in sorted(y.keys()):
          sys.stdout.write("%s: %s  |  "%(z, y[z]))
        print()
  elif args.A:
    if args.t:
      # if args.B (Binary), get the clean hex version
      token=args.t if not args.B else is_hex(args.t)
      action=args.a.lower() if args.a else _DEFAULT_ACTION
      alert=True if args.N else False
      CI=True if args.I else False
      IB=True if args.B else False
      # check if everything is allright
      if action not in _ACCEPTED_ACTIONS: sys.exit("Unknown action: %s"%args.a.lower())
      if args.B and not token:            sys.exit("Invalid hex!")
      HoneyToken(token, action, alert, CI, IB)
      addTokens(db, HoneyToken(token, action, alert, CI, IB))
    
