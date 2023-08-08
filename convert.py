#!/usr/bin/python3

import json
import sys
import copy
import math

mapping = {
  62: 16,
  63: None,
  64: 17,
  65: 18,
  66: None,
  67: 19,
  68: 20,
  69: None,
  70: 21,
  71: None,
  72: 22,
  73: None,
  74: 23,
  75: None,
  76: 24,
  77: 25,
  78: None,
  79: 26,
  80: None,
  81: 27,
  82: 28,
}


def to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fi=open("codes/climate/2220.json")
obj=json.loads(str(fi.read()))


for mode in obj['commands']:
    if mode == 'off':
        continue

    cmds = obj['commands'][mode]
    for fan in cmds:
        #print('%s - %s' % (mode, fan))
        temps = copy.copy(cmds[fan])
        temps_new = cmds[fan] = {}
        for tmp_f in temps:
            tmp_c = mapping[int(tmp_f)]
            if not tmp_c:
                continue

            #print(tmp_f)
            #print(tmp_c)
            temps_new[tmp_c] = temps[tmp_f]

print(json.dumps(obj, indent=2))

