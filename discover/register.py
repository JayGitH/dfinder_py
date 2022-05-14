#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import etcd3
import tornado
import time

from discover.etcd_conf import EtcdConf


def random_str(l = 16) -> str:
  res = str()
  randList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lim = len(randList)
  for i in range(l):
    res += randList[random.randint(0, lim - 1)]
  return res

class Register:
  def __init__(self, servername, addr, env, etcd_conf = EtcdConf()):
    self.servername = servername
    self.env = env
    self.etcd_conf = etcd_conf
    self.addr = addr
    self.token = random_str()
    self.etcd_client = etcd3.Etcd3Client(host = etcd_conf.host, port = etcd_conf.port)
    pass
  

  def _makeKey(self):
    return self.env + '/' + self.servername + '/' + self.token


  def Serve(self):
    lease = self.etcd_client.lease(ttl = 15)
    self.etcd_client.put(self._makeKey(), self.addr, lease)

    def refresh_lease():
      self.etcd_client.refresh_lease(lease.id)

    tornado.ioloop.PeriodicCallback(refresh_lease, 10000).start()
      