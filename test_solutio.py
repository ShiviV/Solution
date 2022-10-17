# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 19:24:59 2022

@author: verma
"""
import numpy as np
import pytest
import solution

def test_answer():
    v = [[2, 1, 0, 2, 1],
         [0, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    assert solution.rotOranges(v) == -1 
    print("Success")

def test_answer_all_zeroes():
    v = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    assert solution.rotOranges(v) == 0 

def test_answer_all_ones():
    v = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
    assert solution.rotOranges(v) == -1 

def test_size():
    v = [[2, 1, 0, 2, 1],
         [0, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    assert solution.checksize(v) !=(1001,1001)
    print("Success")


