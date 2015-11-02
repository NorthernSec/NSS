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

if __name__=='__main__':
  description='''Management script'''

  parser = argparse.ArgumentParser(description=description)
  parser.add_argument('-L', action='store_true', help='List')
  parser.add_argument('-A', action='store_true', help='Add')
  parser.add_argument('-t', metavar='token',     help='Token to add or remove')
  parser.add_argument('-a', metavar='action',    help='Action to take when triggered')
  parser.add_argument('-d', metavar='database',  help='Action to take when triggered')
  parser.add_argument('-I', action='store_true', help='Case Insensitive')
  args = parser.parse_args()
  
  #Defaults
  _DEFAULT_ACTION = "drop"
  _DEFAULT_DB = "NSS.lite"

  db=args.d if args.d else _DEFAULT_DB
  
  if args.L:
    tables=["HoneyTokens"]
    for x in tables:
      print("="*80 + "\n%s\n"%(x) + "="*80)
      for y in selectAllFrom(db, x):
        sys.stdout.write("|  ")
        for z in sorted(y.keys()):
          sys.stdout.write("%s: %s  |  "%(z, y[z]))
        print()
  elif args.A:
    if args.t:
      token=args.t
      action=args.a if args.a else _DEFAULT_ACTION
      CI=True if args.I else False
      addTokens(db, {"token": token, "action": action, "caseinsensitive": CI})
    
