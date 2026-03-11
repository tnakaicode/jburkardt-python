#! /usr/bin/env python3
#
def insurance_simulation_test ( ):

#*****************************************************************************80
#
## insurance_simulation_test() tests insurance_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'insurance_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Simulate term life insurance.' )

  insurance_simulation_test1 ( )
  insurance_simulation_test2 ( )

  print ( '' )
  print ( 'insurance_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def insurance_simulation_test1 ( ):

#*****************************************************************************80
#
## insurance_simulation_test1() observes a single case year by year.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'insurance_simulation_test1()' )
  print ( '  Observe a single case year by year.' )

  age = 25
  term = 40
  yearly_fee = 500.0
  death_benefit = 100000.0

  pay_in_total = 0.0
  pay_out_total = 0.0
  value_total = 0.0
  pay_age_total = np.zeros ( 100 )

  verbose = True

  pay_in, pay_out, pay_age, value = insurance_simulation ( \
    age, term, yearly_fee, death_benefit, verbose )

  return

def insurance_simulation_test2 ( ):

#*****************************************************************************80
#
## insurance_simulation_test2() simulates one case many times.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'insurance_simulation_test2()' )
  print ( '  Average many instances of a single case.' )

  age = 25
  term = 40
  yearly_fee = 500.0
  death_benefit = 100000.0

  pay_in_total = 0.0
  pay_out_total = 0.0
  value_total = 0.0
  death_total = 0

  trials = 1000
  verbose = False

  for i in range ( 0, trials ):
    pay_in, pay_out, pay_age, value = insurance_simulation ( \
      age, term, yearly_fee, death_benefit, verbose )
    pay_in_total = pay_in_total + pay_in
    pay_out_total = pay_out_total + pay_out
    value_total = value_total + value
    if ( 0 < pay_out ):
      death_total = death_total + 1

  pay_in_mean = pay_in_total / trials
  pay_out_mean = pay_out_total / trials
  value_mean = value_total / trials

  print ( '' )
  print ( '  The case was simulated ', trials, ' times.' )
  print ( '  Number of (covered) deaths ', death_total )
  print ( '  Average customer payments  = ', pay_in_mean )
  print ( '  Average company payments   = ', pay_out_mean )
  print ( '  Average bank account value = ', value )

  return

def insurance_simulation ( age, term, yearly_fee, death_benefit, verbose ):

#*****************************************************************************80
#
## insurance_simulation() simulates a term life insurance plan.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer age: the age at which coverage is to begin.
#
#    integer term: the number of years of coverage.
#
#    real yearly_fee: the annual payment the customer makes.
#
#    real death_benefit: the amount paid by the covering company
#    if the customer dies during the covered term.
#
#    logical verbose: true if printed output is desired.
# 
#  Output:
#
#    real pay_in: the amount the customer paid in yearly fees.
#
#    real pay_out: the amount the company returned to the customer.
#
#    integer pay_age: the age at which the customer died, receiving
#    the benefit, or 0 if none.
#
#    real value: the value equivalent to putting the yearly payments
#    into a savings account at 4 percent interest.
#
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Get probability of dying in this year.
#
  age_this_year, total_this_year, male_this_year, female_this_year = \
    mortality_this_year ( )
#
#  Initialize.
#
  pay_in = 0.0
  pay_out = 0.0
  pay_age = 0
  value = 0.0
  interest_rate = 0.04

  if ( verbose ):
    print ( '' )
    print ( '  Customer age: ', age )
    print ( '  Number of years of coverage ', term )
    print ( '  Annual payment = ', yearly_fee )
    print ( '  Company benefit for death within term ', death_benefit )
    print ( '  Annual interest rate is ', interest_rate )
    print ( '' )
    print ( 'Bracket   P(Death)      Pay       Bank  Benefit' )
    print ( '' )
#
#  Loop over the terms of the insurance coverage.
#
  for year_age in range ( age, age + term ):
#
#  Cover the interval [year_age,year_age+1].
#
    value = value * ( 1.0 + interest_rate )
    value = value + yearly_fee

    pay_in = pay_in + yearly_fee
    died = ( rng.random ( ) < total_this_year[year_age] )
    if ( died ):
      pay_age = year_age
      pay_out = death_benefit

    if ( verbose ):
      print ( '[%2d,%2d]  %8.4f  %8.0f  %8.0f  %8.0f' \
        % ( year_age, year_age + 1, total_this_year[year_age], \
        pay_in, value, pay_out ) )

    if ( died ):
      break

  return pay_in, pay_out, pay_age, value

def mortality_count ( ):

#*****************************************************************************80
#
## mortality_count() returns mortality counts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer age(115): the age, in years, at death, from 0 to 114.
#
#    integer total(115), male(115), female(115): the number of deaths total,
#    male, and female..
#
  import numpy as np

  data = np.array ( [ \
   [   0,  29138,  16293,  12845 ], \
   [   1,   1940,   1056,    884 ], \
   [   2,   1178,    665,    513 ], \
   [   3,    882,    501,    381 ], \
   [   4,    703,    412,    291 ], \
   [   5,    595,    345,    250 ], \
   [   6,    570,    314,    256 ], \
   [   7,    528,    297,    231 ], \
   [   8,    511,    281,    230 ], \
   [   9,    507,    282,    225 ], \
   [  10,    551,    307,    244 ], \
   [  11,    535,    323,    212 ], \
   [  12,    590,    347,    243 ], \
   [  13,    781,    462,    319 ], \
   [  14,    979,    627,    352 ], \
   [  15,   1372,    903,    469 ], \
   [  16,   2009,   1337,    672 ], \
   [  17,   2593,   1847,    746 ], \
   [  18,   3504,   2576,    928 ], \
   [  19,   3821,   2895,    926 ], \
   [  20,   3769,   2865,    904 ], \
   [  21,   4187,   3183,   1004 ], \
   [  22,   4309,   3335,    974 ], \
   [  23,   4113,   3109,   1004 ], \
   [  24,   4305,   3266,   1039 ], \
   [  25,   4129,   3074,   1055 ], \
   [  26,   4233,   3062,   1171 ], \
   [  27,   4226,   3081,   1145 ], \
   [  28,   4160,   2970,   1190 ], \
   [  29,   4183,   2920,   1263 ], \
   [  30,   4117,   2895,   1222 ], \
   [  31,   4102,   2820,   1282 ], \
   [  32,   4263,   2853,   1410 ], \
   [  33,   4339,   2928,   1411 ], \
   [  34,   4820,   3189,   1631 ], \
   [  35,   5309,   3420,   1889 ], \
   [  36,   5837,   3778,   2059 ], \
   [  37,   6255,   4066,   2189 ], \
   [  38,   6598,   4181,   2417 ], \
   [  39,   6882,   4310,   2572 ], \
   [  40,   7607,   4707,   2900 ], \
   [  41,   8475,   5326,   3149 ], \
   [  42,   9546,   6006,   3540 ], \
   [  43,  10932,   6773,   4159 ], \
   [  44,  12165,   7538,   4627 ], \
   [  45,  13071,   8145,   4926 ], \
   [  46,  14477,   8975,   5502 ], \
   [  47,  15643,   9494,   6149 ], \
   [  48,  16708,  10187,   6521 ], \
   [  49,  17839,  11103,   6736 ], \
   [  50,  19360,  11935,   7425 ], \
   [  51,  20623,  12752,   7871 ], \
   [  52,  21352,  13327,   8025 ], \
   [  53,  22451,  14169,   8282 ], \
   [  54,  23162,  14369,   8793 ], \
   [  55,  24254,  15224,   9030 ], \
   [  56,  24955,  15509,   9446 ], \
   [  57,  26279,  16272,  10007 ], \
   [  58,  27504,  16828,  10676 ], \
   [  59,  29466,  17757,  11709 ], \
   [  60,  32041,  19256,  12785 ], \
   [  61,  27403,  16407,  10996 ], \
   [  62,  28804,  17045,  11759 ], \
   [  63,  31648,  18821,  12827 ], \
   [  64,  34756,  20499,  14257 ], \
   [  65,  33801,  19641,  14160 ], \
   [  66,  33496,  19431,  14065 ], \
   [  67,  34281,  19643,  14638 ], \
   [  68,  35602,  20371,  15231 ], \
   [  69,  37811,  21406,  16405 ], \
   [  70,  38341,  21522,  16819 ], \
   [  71,  40687,  22715,  17972 ], \
   [  72,  43613,  23861,  19752 ], \
   [  73,  44334,  24272,  20062 ], \
   [  74,  47272,  25482,  21790 ], \
   [  75,  51055,  27202,  23853 ], \
   [  76,  54369,  28631,  25738 ], \
   [  77,  58251,  30303,  27948 ], \
   [  78,  60579,  30986,  29593 ], \
   [  79,  64775,  32547,  32228 ], \
   [  80,  67786,  33696,  34090 ], \
   [  81,  70562,  34094,  36468 ], \
   [  82,  73985,  34585,  39400 ], \
   [  83,  75459,  34565,  40894 ], \
   [  84,  75861,  34194,  41667 ], \
   [  85,  77832,  33889,  43943 ], \
   [  86,  77066,  32478,  44588 ], \
   [  87,  73003,  29683,  43320 ], \
   [  88,  66968,  25889,  41079 ], \
   [  89,  64355,  24175,  40180 ], \
   [  90,  58928,  21012,  37916 ], \
   [  91,  54036,  18120,  35916 ], \
   [  92,  48749,  15483,  33266 ], \
   [  93,  42448,  12787,  29661 ], \
   [  94,  36019,  10075,  25944 ], \
   [  95,  29592,   7834,  21758 ], \
   [  96,  22912,   5445,  17467 ], \
   [  97,  18237,   4072,  14165 ], \
   [  98,  13730,   2812,  10918 ], \
   [  99,  10006,   1939,   8067 ], \
   [ 100,   6952,   1188,   5764 ], \
   [ 101,   4868,    827,   4041 ], \
   [ 102,   3105,    484,   2621 ], \
   [ 103,   1995,    274,   1721 ], \
   [ 104,   1222,    196,   1026 ], \
   [ 105,    747,     86,    661 ], \
   [ 106,    411,     67,    344 ], \
   [ 107,    227,     19,    208 ], \
   [ 108,    114,     15,     99 ], \
   [ 109,     63,      8,     55 ], \
   [ 110,     29,      5,     24 ], \
   [ 111,     17,      2,     15 ], \
   [ 112,      9,      2,      7 ], \
   [ 113,      4,      0,      4 ], \
   [ 114,      1,      0,      1 ] ] )

  age = data[:,0]
  total = data[:,1]
  male = data[:,2]
  female = data[:,3]

  return age, total, male, female

def mortality_this_year ( ):

#*****************************************************************************80
#
## mortality_this_year() returns probability of death this year.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer age(115): the age_brackets, in years, from 0:1 to 114:115.
#
#    real total_this_year(115), male_this_year(115), female_this_year(115): 
#    the probability that a person alive at the beginning of the age bracket 
#    will die by the end of that age bracket.
#
  import numpy as np

  age, total, male, female = mortality_count ( )

  n = len ( age )

  total_this_year = np.zeros ( n )
  pop_this_year = np.sum ( total )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      total_this_year[i] = total[i] / pop_this_year
    pop_this_year = pop_this_year - total[i]

  male_this_year = np.zeros ( n )
  pop_this_year = np.sum ( male )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      male_this_year[i] = male[i] / pop_this_year
    pop_this_year = pop_this_year - male[i]

  female_this_year = np.zeros ( n )
  pop_this_year = np.sum ( female )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      female_this_year[i] = female[i] / pop_this_year
    pop_this_year = pop_this_year - female[i]

  return age, total_this_year, male_this_year, female_this_year

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  insurance_simulation_test ( )
  timestamp ( )

