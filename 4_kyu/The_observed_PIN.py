# The observed PIN.

# Topic: ALGORITHMS.

'''
# Task:
-------
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find 
all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead 
of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all 
possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

# Sample Tests:
----------------
import codewars_test as test
from solution import get_pins

@test.describe('Sample tests')
def sample_tests():
    
    test_cases = [
        ('8', ['5','7','8','9','0']),
        ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339","366","399","658","636","258","268","669","668","266","369","398",
            "256","296","259","368","638","396","238","356","659","639","666","359",
            "336","299","338","696","269","358","656","698","699","298","236","239"
        ])
    ]
        
    for pin, expected in test_cases:
        
        @test.it('PIN: ' + repr(pin))
        def _():
            actual = sorted(get_pins(pin))
            exp = sorted(expected)
            test.assert_equals(actual, exp, 'PIN: ' + pin)


# Code:
-------
def get_pins(observed):
    pass # TODO: This is your job, detective! 
    
'''
# Solution:
from itertools import product

def get_pins(observed):
    # Mapping each digit to its possible adjacent digits including itself
    adjacent = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    # Using itertools.product to create all combinations of adjacent digits for each digit in the observed PIN
    return [''.join(p) for p in product(*(adjacent[d] for d in observed))]

# Testing the function with the provided sample tests
test_cases = [
    ('8', ['5', '7', '8', '9', '0']),
    ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
    ('369', [
        "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
        "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
        "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
    ])
]
results = {pin: sorted(get_pins(pin)) for pin, _ in test_cases}
results

# Description:
'''
Here's the implementation of the get_pins function, which generates all possible variations of a PIN, considering adjacent digits on a keypad. 
This implementation maps each digit to its possible adjacent digits (including itself) and then uses itertools.product to create all combinations 
of these adjacent digits for the observed PIN. ​​

'''



