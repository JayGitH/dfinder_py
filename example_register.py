#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from discover.etcd_conf import EtcdConf
from discover.register import Register


if __name__ == '__main__':
  r = Register("test_py", "0.0.0.99", "dev", etcd_conf=EtcdConf(host="localhost", port=2379))
  r.Serve()
  while True:
    print("haha")
    time.sleep(5)
    pass