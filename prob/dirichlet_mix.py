#! /usr/bin/env python
#
def dirichlet_mix_check ( comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## DIRICHLET_MIX_CHECK checks the parameters of a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    Input, integer ELEM_NUM, the number of elements of an observation.
#
#    Input, real A(ELEM_NUM,COMP_NUM), the probabilities
#    for element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    Input, real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
  check = True

  for comp_i in range ( 0, comp_num ):

    for elem_i in range ( 0, elem_num ):
      if ( a[elem_i,comp_i] <= 0.0 ):
        print ( '' )
        print ( 'DIRICHLET_MIX_CHECK - Fatal error!' )
        print ( '  A(ELEM,COMP) <= 0.' )
        print ( '  COMP = %d' % ( comp_i ) )
        print ( '  ELEM = %d' % ( elem_i ) )
        print ( '  A[COMP,ELEM] = %f' % ( a[elem_i,comp_i] ) )
        check = False
        return check

  positive = False

  for comp_i in range ( 0, comp_num ):

    if ( comp_weight[comp_i] < 0.0 ):
      print ( '' )
      print ( 'DIRICHLET_MIX_CHECK - Fatal error!' )
      print ( '  COMP_WEIGHT(COMP) < 0.' )
      print ( '  COMP = %d' % ( comp_i ) )
      print ( '  COMP_WEIGHT(COMP) = %d' % ( comp_weight[comp_i] ) )
      check = False
      return check
    elif ( 0.0 < comp_weight[comp_i] ):
      positive = True

  if ( not positive ):
    print ( '' )
    print ( 'DIRICHLET_MIX_CHECK - Fatal error!' )
    print ( '  All component weights are zero.' )
    check = False

  return check

def dirichlet_mix_mean ( comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## DIRICHLET_MIX_MEAN returns the means of a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    Input, integer ELEM_NUM, the number of elements of an observation.
#
#    Input, real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    Input, real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#    Output, real MEAN(ELEM_NUM), the means for each element.
#
  import numpy as np
  from dirichlet import dirichlet_mean
  from r8vec_sum import r8vec_sum

  comp_weight_sum = r8vec_sum ( comp_num, comp_weight )

  mean = np.zeros ( elem_num )
  a_column = np.zeros ( elem_num )

  for j in range ( 0, comp_num ):
    for i in range ( 0, elem_num ):
      a_column[i] = a[i,j]
    comp_mean = dirichlet_mean ( elem_num, a_column )
    for i in range ( 0, elem_num ):
      mean[i] = mean[i] + comp_weight[j] * comp_mean[i]

  for i in range ( 0, elem_num ):
    mean[i] = mean[i] / comp_weight_sum

  return mean

def dirichlet_mix_pdf ( x, comp_num, elem_num, a, comp_weight ):

#*****************************************************************************80
#
## DIRICHLET_MIX_PDF evaluates a Dirichlet mixture PDF.
#
#  Discussion:
#
#    The PDF is a weighted sum of Dirichlet PDF's.  Each PDF is a
#    "component", with an associated weight.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(ELEM_NUM), the argument of the PDF.
#
#    Input, integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    Input, integer ELEM_NUM, the number of elements of an observation.
#
#    Input, real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    Input, real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from dirichlet import dirichlet_pdf
  from r8vec_sum import r8vec_sum

  comp_weight_sum = r8vec_sum ( comp_num, comp_weight )

  a_column = np.zeros ( elem_num )

  pdf = 0.0

  for j in range ( 0, comp_num ):

    for i in range ( 0, elem_num ):
      a_column[i] = a[i,j]

    comp_pdf = dirichlet_pdf ( x, elem_num, a_column )

    pdf = pdf + comp_weight[j] * comp_pdf / comp_weight_sum

  return pdf

def dirichlet_mix_pdf_test ( ):

#*****************************************************************************80
#
## DIRICHLET_MIX_PDF_TEST tests DIRICHLET_MIX_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  comp_num = 2
  elem_num = 3

  print ( '' )
  print ( 'DIRICHLET_MIX_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIRICHLET_MIX_PDF evaluates the Dirichlet Mix PDF.' )

  x = np.array ( [ 0.500, 0.125, 0.375 ] )

  a = np.array ( [ \
    [ 0.250, 1.500 ], \
    [ 0.500, 0.500 ], \
    [ 1.250, 2.000 ] ] )

  comp_weight = np.array ( [ 1.0, 2.0 ] )

  check = dirichlet_mix_check ( comp_num, elem_num, a, comp_weight )

  if ( not check ):
    print ( '' )
    print ( 'DIRICHLET_MIX_PDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '  Number of elements ELEM_NUM =   %6d' % ( elem_num ) )
  print ( '  Number of components COMP_NUM = %6d' % ( comp_num ) )

  r8mat_print ( elem_num, comp_num, a, '  PDF parameters A(ELEM,COMP):' )

  r8vec_print ( comp_num, comp_weight, '  Component weights:' )

  pdf = dirichlet_mix_pdf ( x, comp_num, elem_num, a, comp_weight )

  print ( '' )
  print ( '  PDF value =           %14g' % ( pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIRICHLET_MIX_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def dirichlet_mix_sample ( comp_num, elem_num, a, comp_weight, seed ):

#*****************************************************************************80
#
## DIRICHLET_MIX_SAMPLE samples a Dirichlet mixture PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer COMP_NUM, the number of components in the Dirichlet
#    mixture density, that is, the number of distinct Dirichlet PDF's
#    that are mixed together.
#
#    Input, integer ELEM_NUM, the number of elements of an observation.
#
#    Input, real A(ELEM_NUM,COMP_NUM), the probabilities for
#    element ELEM_NUM in component COMP_NUM.
#    Each A(I,J) should be positive.
#
#    Input, real COMP_WEIGHT(COMP_NUM), the mixture weights of the densities.
#    These do not need to be normalized.  The weight of a given component is
#    the relative probability that that component will be used to generate
#    the sample.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(ELEM_NUM), a sample of the PDF.
#
#    Output, integer COMP, the index of the component of the Dirichlet
#    mixture that was chosen to generate the sample.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from dirichlet import dirichlet_sample
  from discrete import discrete_sample
#
#  Choose a particular density component COMP.
#
  comp, seed = discrete_sample ( comp_num, comp_weight, seed )
#
#  Sample the density number COMP.
#
  a_column = np.zeros ( elem_num )
  for i in range ( 0, elem_num ):
    a_column[i] = a[i,comp-1]

  x, seed = dirichlet_sample ( elem_num, a_column, seed )

  return x, comp, seed

def dirichlet_mix_sample_test ( ):

#*****************************************************************************80
#
## DIRICHLET_MIX_SAMPLE_TEST tests DIRICHLET_MIX_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8row_max import r8row_max
  from r8row_mean import r8row_mean
  from r8row_min import r8row_min
  from r8row_variance import r8row_variance
  from r8vec_print import r8vec_print

  comp_num = 2
  elem_num = 3
  sample_num = 1000

  seed = 123456789

  print ( '' )
  print ( 'DIRICHLET_MIX_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIRICHLET_MIX_SAMPLE samples the Dirichlet Mix distribution' )
  print ( '  DIRICHLET_MIX_MEAN computes the Dirichlet Mix mean' )

  a = np.array ( [ \
    [ 0.250, 1.500 ], \
    [ 0.500, 0.500 ], \
    [ 1.250, 2.000 ] ] )

  comp_weight = np.array ( [ 1.0, 2.0 ] )

  check = dirichlet_mix_check ( comp_num, elem_num, a, comp_weight )

  if ( not check ):
    print ( '' )
    print ( 'DIRICHLET_MIX_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  Number of elements ELEM_NUM =   %6d' % ( elem_num ) )
  print ( '  Number of components COMP_NUM = %6d' % ( comp_num ) )

  r8mat_print ( elem_num, comp_num, a, '  PDF parameters A(ELEM,COMP):' )

  r8vec_print ( comp_num, comp_weight, '  Component weights:' )

  mean = dirichlet_mix_mean ( comp_num, elem_num, a, comp_weight )

  r8vec_print ( elem_num, mean, '  PDF mean:' )

  x = np.zeros ( [ elem_num, sample_num ] )
  for j in range ( 0, sample_num ):
    v, comp, seed = dirichlet_mix_sample ( comp_num, elem_num, a, comp_weight, seed )
    for i in range ( 0, elem_num ):
      x[i,j] = v[i]

  xmax = r8row_max ( elem_num, sample_num, x )

  xmin = r8row_min ( elem_num, sample_num, x )

  mean = r8row_mean ( elem_num, sample_num, x )

  variance = r8row_variance ( elem_num, sample_num, x )

  print ( '' )
  print ( '  Sample size = %6d' % ( sample_num ) )
  print ( '' )
  print ( '  Observed Min, Max, Mean, Variance:' )
  print ( '' )

  for i in range ( 0, elem_num ):
    print ( '  %6d  %14g  %14g  %14g  %14g' \
    % ( i, xmin[i], xmax[i], mean[i], variance[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIRICHLET_MIX_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  dirichlet_mix_pdf_test ( )
  dirichlet_mix_sample_test ( )
  timestamp ( )
 
