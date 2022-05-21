#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

from grpc import server

def random_str(l : int = 16) -> str:
  res = str()
  randList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lim = len(randList)
  for i in range(l):
    res += randList[random.randint(0, lim - 1)]
  return res


def make_prefix(env : str, servername : str) -> str:
  return env + "/" + servername + "/"