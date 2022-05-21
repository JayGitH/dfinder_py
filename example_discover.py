#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from discover.discover import Discover
from discover.etcd_conf import EtcdConf
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--etcd_host", type=str, default="127.0.0.1", help="etcd_host (default=127.0.0.1)", required=False)
parser.add_argument("--etcd_port", type=str, default="2379", help="etcd_port (default=2379)", required=False)
args = parser.parse_args()


if __name__ == '__main__':
  dco = Discover("dev", EtcdConf(host=args.etcd_host, port=args.etcd_port))
  while True:
    print("pyrandom=", dco.GetRandomAddr("test_py"))
    print("pylist=", dco.GetAllAddrs("test_py"))
    time.sleep(5)
    pass
  