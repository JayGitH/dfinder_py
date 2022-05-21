#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from grpc import server
from discover.etcd_conf import EtcdConf
import etcd3

from discover.svrdef import SvrDef
from discover.util import make_prefix


class Discover:
  def __init__(self, env : str, etcd_conf : EtcdConf):
    self.etcd_conf = etcd_conf
    self.etcd_client = etcd3.Etcd3Client(host = etcd_conf.host, port = etcd_conf.port)
    self.str2def : dict[str, SvrDef] = dict()
    self.env = env
    pass
  

  def _GetPrefix(self, servername : str) -> dict:
    resp = self.etcd_client.get_prefix(make_prefix(self.env, servername))
    ret = dict()
    for item in resp:
      # bytes to str
      ret[str(item[1].key, encoding='utf-8')] = str(item[0], encoding='utf-8')
    return ret


  def GetAllAddrs(self, servername : str) -> list:
    updMap = self._GetPrefix(servername)
    if servername in self.str2def.keys():
      pass
    else:
      self.str2def[servername] = SvrDef(servername)
    
    self.str2def[servername].Update(updMap)
    return self.str2def[servername].AddrList()


  def GetRandomAddr(self, servername : str) -> str:
    updMap = self._GetPrefix(servername)
    if servername in self.str2def.keys():
      pass
    else:
      self.str2def[servername] = SvrDef(servername)
    
    self.str2def[servername].Update(updMap)
    return self.str2def[servername].RandomAddr()
    