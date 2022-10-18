
import numpy as np
import pytest
import solution

def test_all_twos():
    v = [[2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2]]
    assert solution.infect(v) == 0 
    print("Success")

def test_answer():
    v = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0]]
    assert solution.infect(v) == -1 

def test_answer_all_zeroes():
    v = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    assert solution.infect(v) == -1 

def test_answer_all_ones():
    v = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
    assert solution.infect(v) == -1 

def test_Negative():
    v = [[-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1]]
    assert solution.infect(v) == 0 

def test_Negative():
    v = [[-1, -2, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1]]
    assert solution.infect(v) == 0 

def test_Negative():
    v = [[-1, 2, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1]]
    assert solution.infect(v) == 0 

def test_Negative():
    v = [[-1, 2.6, -1, -1, -1],
         [-1, -1, -1, -1, -1],
         [-1, 3.4, -1, -1, -1]]
    assert solution.infect(v) == 0 

def test_size():
    v = [[2, 1, 0, 2, 1],
         [0, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]
    assert solution.checksize(v) !=(1001,1001)
    print("Success")




