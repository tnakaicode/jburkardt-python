#! /usr/bin/env python3
#
def mortality_test ( ):

#*****************************************************************************80
#
## mortality_test() tests mortality().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mortality_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mortality().' )

  mortality_cdf_plot ( )
  mortality_count_plot ( )
  mortality_expected_plot ( )
  mortality_pdf_plot ( )
  mortality_plus10_plot ( )
  mortality_table ( )
  mortality_this_year_plot ( )
  mortality_to_die_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mortality_test():' )
  print ( '  Normal end of execution.' )

  return

def mortality_average_life ():

#*****************************************************************************80
#
## mortality_average_life() estimates the average life span.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real combined_life, male_life, female life: the average life span for
#    the combined, male, and female populations.
#
  import numpy as np

  age_death, combined_death, male_death, female_death = mortality_count ( )

  combined_life = 0.0
  male_life = 0.0
  female_life = 0.0

  age_max = len ( age_death )

  for i in range ( 0, age_max ):
    years = age_death[i] + 0.5
    combined_life = combined_life + years * combined_death[i]
    male_life = male_life + years * male_death[i]
    female_life = female_life + years * female_death[i]

  combined_life = combined_life / np.sum ( combined_death )
  male_life = male_life / np.sum ( male_death )
  female_life = female_life / np.sum ( female_death )

  return combined_life, male_life, female_life

def mortality_cdf ():

#*****************************************************************************80
#
## mortality_cdf() determines mortality cumulative density function.
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
  import numpy as np
#
#  Get the data.
#
  age, combined, male, female = mortality_count ( )
#
#  Normalize.
#
  combined = combined / np.sum ( combined )
  male = male / np.sum ( male )
  female = female / np.sum ( female )
#
#  Compute the CDF's as cumulative sums.
#
  combined_cdf = np.cumsum ( combined )
  male_cdf = np.cumsum ( male )
  female_cdf = np.cumsum ( female )

  return age, combined_cdf, male_cdf, female_cdf

def mortality_cdf_plot ():

#*****************************************************************************80
#
## mortality_cdf_plot() plots mortality cumulative density function.
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
  import matplotlib.pyplot as plt
#
#  Get the data.
#
  age, combined_cdf, male_cdf, female_cdf = mortality_cdf ( ); 
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( age, combined_cdf, 'k-', linewidth = 3 )
  plt.plot ( age, male_cdf, 'b-', linewidth = 3 )
  plt.plot ( age, female_cdf, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age at death -->' )
  plt.ylabel ( '<-- Probability of death -->' )
  plt.title ( 'Probability of death at or before given age, in 2007' )
  plt.legend ( [ 'Combined', 'Male', 'Female' ] )
  plt.grid ( True )

  filename = 'mortality_cdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

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
#    integer combined(115), male(115), female(115): the number of deaths 
#    combined, male, and female..
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
  combined = data[:,1]
  male = data[:,2]
  female = data[:,3]

  return age, combined, male, female

def mortality_count_plot ():

#*****************************************************************************80
#
## mortality_count_plot() plots mortality counts.
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'mortality_count_plot():' )
  print ( '  mortality_count_plot() plots mortality counts.' )
#
#  Get the data.
#
  age, combined, male, female = mortality_count ( )
#
#  Create the plot.
#
  plt.clf ( )
  plt.plot ( age, combined, 'k-', linewidth = 3 )
  plt.plot ( age, male, 'b-', linewidth = 3 )
  plt.plot ( age, female, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age at death -->' )
  plt.ylabel ( '<-- Number of deaths -->' )
  plt.title ( 'mortality counts: 2007' )
  plt.legend ( [ 'combined', 'male', 'female' ] )
  plt.grid ( True )

  filename = 'mortality_count.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def mortality_expected_plot ():

#*****************************************************************************80
#
## mortality_expected_plot() plots expected mortality.
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
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Get the data.
#
  age, combined, male, female = mortality_count ( )
#
#  Get sums for normalization.
#
  n = len ( age )

  et = np.NAN * np.ones ( n )
  em = np.NAN * np.ones ( n )
  ef = np.NAN * np.ones ( n )
  for i in range ( 0, n ):
    if ( 0 < np.sum ( combined[i:n] ) ):
      et[i] = np.dot ( age[i:n], combined[i:n] ) / np.sum ( combined[i:n] )
    if ( 0 < np.sum ( male[i:n] ) ):
      em[i] = np.dot ( age[i:n], male[i:n] ) / np.sum ( male[i:n] )
    if ( 0 < np.sum ( female[i:n] ) ):
      ef[i] = np.dot ( age[i:n], female[i:n] ) / np.sum ( female[i:n] )
#
#  Make the plot.
#
  plt.clf ( )
  plt.plot ( age, et, 'k-', linewidth = 3 )
  plt.plot ( age, em, 'b-', linewidth = 3 )
  plt.plot ( age, ef, 'r-', linewidth = 3 )
  plt.plot ( age, age, 'g-', linewidth = 3 )
  plt.xlabel ( '<-- Age at death -->' )
  plt.ylabel ( '<-- Number of deaths -->' )
  plt.title ( 'Life expectancy by age, in 2007' )
  plt.grid ( True )
  plt.legend ( [ 'Combined', 'Male', 'Female', 'Age if you die now', 'Location' ] )
  filename = 'mortality_expected.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.close ( )

  return

def mortality_pdf ():

#*****************************************************************************80
#
## mortality_pdf() computes the mortality probability density function.
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
  import numpy as np

  age, combined, male, female = mortality_count ( )
#
#  Normalize the data.
#
  combined_pdf = combined / np.sum ( combined )
  male_pdf = male / np.sum ( male )
  female_pdf = female / np.sum ( female )

  return age, combined_pdf, male_pdf, female_pdf

def mortality_pdf_plot ():

#*****************************************************************************80
#
## mortality_pdf_plot() plots mortality probability density function.
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
  import matplotlib.pyplot as plt

  age, combined_pdf, male_pdf, female_pdf = mortality_pdf ()
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( age, combined_pdf, 'k-', linewidth = 3 )
  plt.plot ( age, male_pdf, 'b-', linewidth = 3 )
  plt.plot ( age, female_pdf, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age at death -->' )
  plt.ylabel ( '<-- Probability of death -->' )
  plt.title ( 'Probability of deaths for each age, in 2007' )
  plt.legend ( [ 'Combined', 'Male', 'Female' ] )
  plt.grid ( True )

  filename = 'mortality_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.close ( )

  return

def mortality_plus10_plot ():

#*****************************************************************************80
#
## mortality_plus10_plot() plots the chance of living at least 10 more years.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'mortality_plus10_plot():' )
  print ( '  Plot the probability of living at least 10 more years.' )
#
#  Get the data.
#
  age, combined, male, female = mortality_count ( )

  n = len ( age )
#
#  Compute the combined, male, and female death counts by summing the deaths.
#
  combined_to_die = np.sum ( combined )
  male_to_die = np.sum ( male )
  female_to_die = np.sum ( female )
#
#  The number alive at age K is the population minus the number who have died 
#  up to that age.
#  (Mild off-by-one error here.)
#
  combined_alive = combined_to_die - np.cumsum ( combined )
  male_alive = male_to_die - np.cumsum ( male )
  female_alive = female_to_die - np.cumsum ( female )
#
#  The chance of being alive 10 years from now is the ratio between
#  the number of people like you alive in 10 years to the number of people
#  like you alive right now.
#
  combined_10 = np.zeros ( n )
  male_10 = np.zeros ( n )
  female_10 = np.zeros ( n )

  combined_10[0:n-10] = combined_alive[10:n] / combined_alive[0:n-10]
  male_10[0:n-10] = male_alive[10:n] / male_alive[0:n-10]
  female_10[0:n-10] = female_alive[10:n] / female_alive[0:n-10]
#
#  Draw the plot.
#
  plt.clf ( )
  plt.plot ( age, combined_10, 'k-', linewidth = 3 )
  plt.plot ( age, male_10, 'b-', linewidth = 3 )
  plt.plot ( age, female_10, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age now -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'Probability of at least 10 more years of life' )
  plt.legend ( [ 'Combined', 'Male', 'Female' ] )
  plt.grid ( True )

  filename = 'mortality_plus10.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.close ( )

  return

def mortality_table ( ):

#*****************************************************************************80
#
## mortality_table() constructs a mortality table().
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
  import numpy as np

  print ( '' )
  print ( 'mortality_table():' )
  print ( '  Create a mortality table' )

  age, combined, male, female = mortality_count ( )
  age, combined_pdf, male_pdf, female_pdf = mortality_pdf ( )
  age, combined_cdf, male_cdf, female_cdf = mortality_cdf ( )
  age, combined_this_year, male_this_year, female_this_year = \
    mortality_this_year ( )

  combined_life, male_life, female_life = mortality_average_life ( )

  n = len ( age )

  print ( '' )
  print ( '  COMBINED STATISTICS = Male + Female' )
  print ( '  Average life span = ', combined_life )
  print ( '' )
  print ( '    Bracket  Pop       Deaths      PDF       CDF   This Year' )
  print ( '' )

  pop = np.sum ( combined )
  for i in range ( 0, n ):
    print ( '  [%3d:%3d]  %7d  %7d  %8.4f  %8.4f  %8.4f' \
    % ( age[i], age[i]+1, pop, combined[i], combined_pdf[i], combined_cdf[i], \
    combined_this_year[i] ) )
    pop = pop - combined[i]

  print ( '' )
  print ( '  MALE STATISTICS' )
  print ( '  Average life span = ', male_life )
  print ( '' )
  print ( '    Bracket  Pop       Deaths      PDF       CDF   This Year' )
  print ( '' )

  pop = np.sum ( male )
  for i in range ( 0, n ):
    print ( '  [%3d:%3d]  %7d  %7d  %8.4f  %8.4f  %8.4f' \
    % ( age[i], age[i]+1, pop, male[i], male_pdf[i], male_cdf[i], \
    male_this_year[i] ) )
    pop = pop - male[i]

  print ( '' )
  print ( '  FEMALE STATISTICS' )
  print ( '  Average life span = ', female_life )
  print ( '' )
  print ( '    Bracket  Pop       Deaths      PDF       CDF   This Year' )
  print ( '' )

  pop = np.sum ( female )
  for i in range ( 0, n ):
    print ( '  [%3d:%3d]  %7d  %7d  %8.4f  %8.4f  %8.4f' \
    % ( age[i], age[i]+1, pop, female[i], female_pdf[i], female_cdf[i], \
    female_this_year[i] ) )
    pop = pop - female[i]

  return

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
#    real combined_this_year(115), male_this_year(115), female_this_year(115): 
#    the probability that a person alive at the beginning of the age bracket 
#    will die by the end of that age bracket.
#
  import numpy as np

  age, combined, male, female = mortality_count ( )

  n = len ( age )

  combined_this_year = np.NAN * np.ones ( n )
  pop_this_year = np.sum ( combined )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      combined_this_year[i] = combined[i] / pop_this_year
    pop_this_year = pop_this_year - combined[i]

  male_this_year = np.NAN * np.ones ( n )
  pop_this_year = np.sum ( male )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      male_this_year[i] = male[i] / pop_this_year
    pop_this_year = pop_this_year - male[i]

  female_this_year = np.NAN * np.ones ( n )
  pop_this_year = np.sum ( female )
  for i in range ( 0, n ):
    if ( 0 < pop_this_year ):
      female_this_year[i] = female[i] / pop_this_year
    pop_this_year = pop_this_year - female[i]

  return age, combined_this_year, male_this_year, female_this_year

def mortality_this_year_plot ():

#*****************************************************************************80
#
## mortality_this_year_plot() plots mortality probability density function.
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
  import matplotlib.pyplot as plt

  age, combined_this_year, male_this_year, female_this_year = \
    mortality_this_year ( )
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( age, combined_this_year, 'k-', linewidth = 3 )
  plt.plot ( age, male_this_year, 'b-', linewidth = 3 )
  plt.plot ( age, female_this_year, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age bracket -->' )
  plt.ylabel ( '<-- Probability of death this year -->' )
  plt.title ( 'Probability of death this year for each age, in 2007' )
  plt.legend ( [ 'Combined', 'Male', 'Female' ] )
  plt.grid ( True )

  filename = 'mortality_this_year.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.close ( );

  return

def mortality_to_die ():

#*****************************************************************************80
#
## mortality_to_die() computes the per bracket "to die" function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer age_to_die[115]: age bracket limits from 0 to 114.
#
#    combined_to_die[115]: combined_to_die[i] is the number of people who will 
#    die this year who are at least age_to_die[i] or older.
#
#    male_to_die[115]: male_to_die[i] is the number of males who will 
#    die this year who are at least age_to_die[i] or older.
#
#    female_to_die[115]: female_to_die[i] is the number of females who will 
#    die this year who are at least age_to_die[i] or older.
#
  import numpy as np

  age, combined_death, male_death, female_death = mortality_count ( )

  n = len ( age )
#
#  This bracket's "to die" minus this year's deaths gives next bracket's "to die".
#
  age_to_die = np.linspace ( 0, n, n + 1 )

  combined_to_die = np.zeros ( n + 1 )
  combined_to_die[0] = np.sum ( combined_death )
  for i in range ( 1, n + 1 ):
    combined_to_die[i] = combined_to_die[i-1] - combined_death[i-1]

  male_to_die = np.zeros ( n + 1 )
  male_to_die[0] = np.sum ( male_death )
  for i in range ( 1, n + 1 ):
    male_to_die[i] = male_to_die[i-1] - male_death[i-1]

  female_to_die = np.zeros ( n + 1 )
  female_to_die[0] = np.sum ( female_death )
  for i in range ( 1, n + 1 ):
    female_to_die[i] = female_to_die[i-1] - female_death[i-1]

  return age_to_die, combined_to_die, male_to_die, female_to_die

def mortality_to_die_plot ():

#*****************************************************************************80
#
## mortality_to_die_plot() plots population.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'mortality_to_die_plot():' )
  print ( '  mortality_to_die_plot() plots the per bracket "to die" function.' )
#
#  Get the data.
#
  age_to_die, combined_to_die, male_to_die, female_to_die = mortality_to_die ( )
#
#  Create the plot.
#
  plt.clf ( )
  plt.plot ( age_to_die, combined_to_die, 'k-', linewidth = 3 )
  plt.plot ( age_to_die, male_to_die, 'b-', linewidth = 3 )
  plt.plot ( age_to_die, female_to_die, 'r-', linewidth = 3 )
  plt.xlabel ( '<-- Age -->' )
  plt.ylabel ( '<-- Die this age -->' )
  plt.title ( 'To die function: 2007' )
  plt.legend ( [ 'combined', 'male', 'female' ] )
  plt.grid ( True )

  filename = 'mortality_to_die.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

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
  mortality_test ( )
  timestamp ( )

