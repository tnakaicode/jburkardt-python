#! /usr/bin/env python
#
def coupon_complete_pdf ( type_num, box_num ):

#*****************************************************************************80
#
## COUPON_COMPLETE_PDF evaluates the Complete Coupon Collection PDF.
#
#  Discussion:
#
#    PDF(TYPE_NUMBOX_NUM) is the probability that, given an inexhaustible 
#    supply of boxes, inside each of which there is one of TYPE_NUM distinct
#    coupons, which are uniformly distributed among the boxes, that it will 
#    require opening exactly BOX_NUM boxes to achieve at least one of each
#    kind of coupon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Herbert Wilf,
#    Some New Aspects of the Coupon Collector's Problem,
#    SIAM Review,
#    Volume 48, Number 3, September 2006, pages 549-565.
#
#  Parameters:
#
#    Input, integer BOX_NUM, the number of boxes that had to be opened
#    in order to just get at least one of each coupon.
#    0 <= BOX_NUM.  If BOX_NUM < TYPE_NUM, then PDF is surely 0.
#
#    Input, integer TYPE_NUM, the number of distinct coupons.
#    1 <= TYPE_NUM.
#
#    Output, real PDF, the value of the PDF.
#
  from stirling2 import stirling2_value
#
#  Nonsense cases.
#
  if ( box_num < 0 ):

    pdf = 0.0

  elif ( type_num < 1 ):

    pdf = 0.0
#
#  Degenerate but meaningful case.
#
  elif ( type_num == 1 ):

    if ( box_num == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0
#
#  Easy cases.
#
  elif ( box_num < type_num ):

    pdf = 0.0
#
#  General case.
#
  else:

    factor = 1.0
    for i in range ( 1, type_num + 1 ):
      factor = factor * float ( i ) / float ( type_num )

    for i in range ( type_num + 1, box_num + 1 ):
      factor = factor / float ( type_num )
    
    pdf = factor * stirling2_value ( box_num - 1, type_num - 1 )

  return pdf

def coupon_complete_pdf_test ( ):

#*****************************************************************************80
#
## COUPON_COMPLETE_PDF_TEST tests COUPON_COMPLETE_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COUPON_COMPLETE_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COUPON_COMPLETE_PDF evaluates the Coupon Complete PDF.' )
  print ( '' )

  for type_num in range ( 2, 5 ):

    print ( '' )
    print ( '  Number of coupon types is %d' % ( type_num ) )
    print ( '' )
    print ( '   BOX_NUM      PDF             CDF' )
    print ( '' )
    cdf = 0.0
    for box_num in range ( 1, 21 ):
      pdf = coupon_complete_pdf ( type_num, box_num )
      cdf = cdf + pdf
      print ( '  %8d  %14g  %14g' % ( box_num, pdf, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COUPON_COMPLETE_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  coupon_complete_pdf_test ( )
  timestamp ( )

