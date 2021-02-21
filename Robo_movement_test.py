#importing required packages
import unittest
import Robo_Movement

#Testing for the default path
def test_get_distance():
    expected = 4
    result = Robo_Movement.get_distance("F1,R1,B2,L1,B3")
    assert expected == result

#Tesing for different command (path)
def test_two_get_distance():
    expected = "Invalid Path, Accepted: F,B,R,L"
    result = Robo_Movement.get_distance("A9,C7,B2,X1,D3")
    assert expected == result

#Testing for lowercase
def test_three_get_distance():
    expected = "Please use capital letters for the commands (directions)"
    result = Robo_Movement.get_distance("a5,d7,B2,X1,D3")
    assert expected == result

#Testing for two digit movement
def test_four_get_distance():
    expected = "Only one alphabet and one digit allowed between commas"
    result = Robo_Movement.get_distance("F99,R1,B2,L1,B3")
    assert expected == result
