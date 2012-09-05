################################
## Øving 1 - TDT4110
## The probability of getting
## two pair in Texas Hold'em
## Øyvind Robertsen
################################
import math

coeff1 = (13 * (13-1))/(2 * 1)
coeff2 = pow(((4 * (4-1))/(2 * 1)),2)
coeff3 = 11/1
coeff4 = 4/1

favored_possibilities = coeff1 * coeff2 * coeff3 * coeff4
total_possibilities = 2598960
probability_of_two_pair= format(favored_possibilities/total_possibilities, '.4f')
print('The probability of getting two pair in Texas Hold\'em is ',probability_of_two_pair,'.',sep='')
