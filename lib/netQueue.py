import os
import sys
runpath=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runpath, '..'))

import binascii
import re
from netfilterqueue import NetfilterQueue
from DatabaseLayer import selectAllFrom

HoneyTokens=[]
db="NSS.lite"

def readData():
  try:
    global HoneyTokens
    HoneyTokens=selectAllFrom(db, "HoneyTokens")
    print("imported %s honeytokens"%len(HoneyTokens))
  except Exception as e:
    print("An error occured: %s"%e)

def checkTraffic(pkt):
  try:
    for x in HoneyTokens:
      check = re.compile(x["token"], re.IGNORECASE) if x['caseinsensitive'] else re.compile(x["token"])
      if(check.search(pkt.get_payload())):
        if x["action"].lower() == "drop":
          print("Packet dropped!")
          pkt.drop()
          return
    # no reason to drop
    pkt.accept()
  except Exception as e:
    print(e)

readData()
nfqueue = NetfilterQueue()
nfqueue.bind(1, checkTraffic)
try:
  nfqueue.run()
except KeyboardInterrupt:
  print("Interruped by user")

