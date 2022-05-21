#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import argparse

from discover.etcd_conf import EtcdConf
from discover.register import Register
import multiprocessing
import os

parser = argparse.ArgumentParser()
parser.add_argument("--etcd_host", type=str, default="127.0.0.1", help="etcd_host (default=127.0.0.1)", required=False)
parser.add_argument("--etcd_port", type=str, default="2379", help="etcd_port (default=2379)", required=False)
args = parser.parse_args()

def RegisterNode(servername, addr, env, etcd_conf):
  print(os.getpid())
  print(servername, addr, env)
  r = Register(servername, addr, env, etcd_conf)
  r.Serve()


if __name__ == '__main__':
  register_process = multiprocessing.Process(target=RegisterNode, args=(
    "test_py",
    "0.0.0.9922",
    "dev",
    EtcdConf(host=args.etcd_host, port=args.etcd_port)
  ))
  register_process.start()
  while True:
    time.sleep(3)
    print("sleep tag")