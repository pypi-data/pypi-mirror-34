#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Apr 27, 2018

Course work: 

@author: raja

Source:
    
'''

def get_state(pin):
    
    if(pin == 625015):
        return 'Tamilnadu'

    return 'Not Found'

def get_location(pin):
    if(pin == 625513):
        return 'Bodi'
    
    if(pin == 625015):
        return 'TCE'

    return 'Not Found'
