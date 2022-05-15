#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from discover.etcd_conf import EtcdConf
from discover.register import Register
import multiprocessing
import os

def RegisterNode(servername, addr, env, etcd_conf):
  print(os.getpid())
  print(servername, addr, env)
  r = Register(servername, addr, env, etcd_conf)
  r.Serve()


if __name__ == '__main__':
  register_process = multiprocessing.Process(target=RegisterNode, args=(
    "test_py",
    "0.0.0.99",
    "dev",
    EtcdConf(host="localhost", port=2379)
  ))
  register_process.start()
  while True:
    time.sleep(3)
    print("sleep tag")