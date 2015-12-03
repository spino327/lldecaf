#!/bin/python
   
# Copyright (C) 2015 Computer Architecture and Parallel Systems Laboratory (CAPSL)    
#
# Original 
# author: Sergio Pino
# E-mail: sergiop@udel.edu
# 
# License
#     
# Redistribution of this code is allowed only after an explicit permission is
# given by the original author or CAPSL and this license should be included in
# all files, either existing or new ones. Modifying the code is allowed, but
# the original author and/or CAPSL must be notified about these modifications.
# The original author and/or CAPSL is also allowed to use these modifications
# and publicly report results that include them. Appropriate acknowledgments
# to everyone who made the modifications will be added in this case.
#
# Warranty    
#
# THIS CODE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES THAT
# THE COVERED CODE IS FREE OF DEFECTS, MERCHANTABLE, FIT FOR A PARTICULAR
# PURPOSE OR NON-INFRINGING. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE
# OF THE COVERED CODE IS WITH YOU. SHOULD ANY COVERED CODE PROVE DEFECTIVE IN
# ANY RESPECT, YOU (NOT THE INITIAL DEVELOPER OR ANY OTHER CONTRIBUTOR) ASSUME
# THE COST OF ANY NECESSARY SERVICING, REPAIR OR CORRECTION. THIS DISCLAIMER
# OF WARRANTY CONSTITUTES AN ESSENTIAL PART OF THIS LICENSE. NO USE OF ANY
# COVERED CODE IS AUTHORIZED HEREUNDER EXCEPT UNDER THIS DISCLAIMER.

'''
Created on Jun 20, 2015

Driver for decaf compiler

@author: Sergio Pino sergiop@udel.edu
'''

import sys
from lldecaf.frontend import scanner
from lldecaf.frontend import parser
#import splanginterp

if __name__ == '__main__':
    # If a filename has been specified, we try to run it.
    # If a runtime error occurs, we bail out and enter
    # interactive mode below
    if len(sys.argv) == 2:
        data = open(sys.argv[1]).read()
        prog = parser.parse(data, debug_flag=False)
        print(prog)
#         if not prog: raise SystemExit
#         b = basinterp.BasicInterpreter(prog)
#         try:
#             b.run()
#             raise SystemExit
#         except RuntimeError:
#             pass
    
#     else:
#         b = basinterp.BasicInterpreter({})
