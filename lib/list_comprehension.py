#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [num for num in num_list if num % 2 == 0]
    return evens_list

def make_exclamation(sentence_list):
    exclamation_list = [string + "!" for string in sentence_list]
    return exclamation_list