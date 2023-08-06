#!/usr/bin/env python

import at_cpp_lookup
import at_tobject_setter
import at_tobject_callable
import at_roostats_lookup

## Patch on-demand (conflict in sphinx which has limited env)
def init():
  at_cpp_lookup._init()
  at_tobject_setter._init()
  at_tobject_callable._init()
