#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class SvrDef:
  def __init__(self, servername : str):
    self.ServerName = servername
    self.addrsMap = dict() # server_sub_name to addr
    pass
  
  '''
   更新服务配置
   svrDef.Update({
     "svr1": "addr1",
     "svr2": "addr2",
     ...
   })
  '''
  def Update(self, serverSubName2Addr : dict):
    delete_key = set()
    for k in self.addrsMap.keys():
      if k in serverSubName2Addr.keys():
        pass
      else:
        delete_key.add(k)
      pass
    
    for k in serverSubName2Addr.keys() :
      self.addrsMap[k] = serverSubName2Addr[k]
      pass

    for k in delete_key:
      self.addrsMap.pop(k)
    pass

  def RandomAddr(self) -> str:
    k = random.choice(list(self.addrsMap.keys()))
    return self.addrsMap[k]

  def AddrList(self) -> list:
    return self.addrsMap.values()