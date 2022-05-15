#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import etcd3
import time
from discover.etcd_conf import EtcdConf
import discover.util


class Register:
  def __init__(self, servername, addr, env, etcd_conf = EtcdConf()):
    self.servername = servername
    self.env = env
    self.etcd_conf = etcd_conf
    self.addr = addr
    self.token = discover.util.random_str()
    self.etcd_client = etcd3.Etcd3Client(host = etcd_conf.host, port = etcd_conf.port)
    pass
  

  def _makeKey(self):
    return self.env + '/' + self.servername + '/' + self.token


  def Serve(self):
    # 阻塞任务
    lease = self.etcd_client.lease(ttl = 15)
    self.etcd_client.put(self._makeKey(), self.addr, lease)
    print("serve begin, lease.id={}".format(lease.id))
    while True:
      print("debug|refresh lease|lease.id={}".format(lease.id))
      refresh_list = lease.refresh()
      print("debug|", refresh_list)
      resp = self.etcd_client.get_lease_info(lease_id=lease.id)
      print("debug|", resp)
      time.sleep(5)