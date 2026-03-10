#! /usr/bin/env python3
#
def apriori_test ( ):

#*****************************************************************************80
#
## apriori_test() tests the apriori algorithm for recommendations.
#
#  Modified:
#
#    16 October 2021
#
  import pandas as pd
  import itertools

  data = pd.read_csv ( "GroceryStoreDataSet.csv" )

  print ( data )

  sales_num = data.shape[0] 

  records = []
  for i in range ( 0, sales_num ):
    records.append ( [ str ( data.values[i,j] ) for j in range ( 0, 4 ) ] )

  items = sorted ( [ item for sublist in records for item in sublist if item != 'nan' ] )

  print ( 'items' )
  print ( items )
  l0 = { i: items.count(i) for i in items }
  print ( "item:counts" )
  print ( l0 )
#
#  Only consider items whose frequency is above a given minimum.
#
  minimum_support_count = 4
  l1 = stage1 ( l0, items, minimum_support_count )

  print ( "frequent items:counts" )
  print ( l1 )
#
#  Only consider items whose frequency is above a given minimum.
#
  minimum_support_count = 4
  l2 = stage2 ( l1, records, minimum_support_count )

  print ( "frequent items:counts" )
  print ( l2 )

  return

def stage1 ( l0, items, minimum_support_count ):

## stage1 returns a list of items that occurred frequently.

  l1 = {}
  for key, value in l0.items():
    if ( minimum_support_count <= value ):
      l1[key] = value

  return l1

def stage2 ( l1, records, minimum_support_count ):

  import itertools
  import pandas as pd

  l1 = sorted ( list ( l1.keys() ) )
  L1 = list ( itertools.combinations ( l1, 2 ) )
  c2 = {}
  l2 = {}
  for iter1 in L1:
    count = 0
    for iter2 in records:
      if ( sublist ( iter1, iter2 ) ):
        count = count + 1
    c2[iter1] = count

  for key, value in c2.items():
    if ( minimum_support_count <= value ):
      if ( check_subset_frequency ( key, l1, 1 ) ):
        l2[key] = value

  return c2, l2

def check_subset_frequency ( itemset, l, n ):

  import itertools

  if ( 1 < n ):
    subsets = list ( itertools.combinations ( itemset, n ) )
  else:
    subsets = itemset

  for iter1 in subsets:
    if ( not ( iter1 in l ) ):
      return False

  return True

def sublist ( lst1, lst2 ):
  return set ( lst1 ) <= set ( lst2 )

def support_count(itemset, itemlist):
  return itemlist[itemset]

if ( __name__ == '__main__' ):
  apriori_test ( )

