#! /usr/bin/env python

from mini_rainfall import calculate_mean_until

def test_positive_ints():
    assert calculate_mean_until([1,2,3,99], 99) == 2.0

def test_negative_ints():
    assert calculate_mean_until([-1,-2,-3,99], 99) == 0

def test_no_ints():
    assert calculate_mean_until([99], 99) == 0
