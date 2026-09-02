#! /usr/bin/env python3
#
from pulp import *
from typing import Tuple, Union

def pulp_test ( ):

#*****************************************************************************80
#
## pulp_test() tests the pulp() linear programming library.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import pulp

  print ( '' )
  print ( 'pulp_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  pulp version:   ' + pulp.__version__ )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  pulp() sets up and solves a variety of linear programming problems.' )

  pulp_test01 ( )
  pulp_test02 ( )
  pulp_test03 ( )
  pulp_test04 ( )
  pulp_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pulp_test():' )
  print ( '  Normal end of execution.' )
  return

def pulp_test01 ( ):

#*****************************************************************************80
#
## pulp_test01() solves a simple simplex problem.
#
#  Discussion:
#
#    Maximize 
#      x1 + 2 x2
#    Subject to
#      0 <= x1 <= 1
#      0 <= x2 <= 1
#      x1 + x2 <= 1.5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips and Stuart Mitchell.
#
  print ( '' )
  print ( 'pulp_test01():' )
  print ( '  Solve a simple simplex problem.' )
#
#  Initialize an LP problem in which we minimize the objective function.
#  pulp() complained when I had blanks in the problem name.
#
  prob = LpProblem ( "Simplex", LpMaximize )
#
#  Create two variables, upper and lower bounds.
#
  x1 = LpVariable ( "x1", 0.0, 1.0 )
  x2 = LpVariable ( "x2", 0.0, 1.0 )
#
#  Define the objective function, including a title,
#
  prob +=  x1 + 2.0 * x2, "Objective function"
#
#  Define the constraint.
#
  prob += x1 + x2 <= 1.5, "Constraint"
#
#  Write an LP file for this problem.
#
  prob.writeLP ( "pulp_test01.lp" )
#
#  Solve the problem. 
#  Instead of a blank, the argument list could specify a particular
#  solver, such as CPLEX().
#
  prob.solve ( )
#
#  Print status.
#
  print ( "Status:", LpStatus[prob.status] )
#
#  Print the optimal variable values.
#
  for v in prob.variables():
    print ( v.name, "=", v.varValue )
#
#  Print the objective value.
#
  print ( "Objective function value = ", value(prob.objective) )

  return

def pulp_test02 ( ):

#*****************************************************************************80
#
## pulp_test02() solves a blending problem to minimize cost of cat food.
#
#  Discussion:
#
#    Create a cat food by blending two ingredients, chicken and beef,
#    in such a way that minimal nutritional requirements for protein, 
#    fat, fiber, and salt are reached, while minimizing the cost of 
#    a can of the final product.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips and Stuart Mitchell.
#
  print ( '' )
  print ( 'pulp_test02():' )
  print ( '  Solve a simple linear programming problem for cat food.' )
#
#  Initialize an LP problem in which we minimize the objective function.
#  pulp() complained when I had blanks in the problem name.
#
  prob = LpProblem ( "Cat_Food", LpMinimize )
#
#  Create two variables, with lower limits of 0.
#
  x1 = LpVariable ( "ChickenPercent", 0, None, LpInteger )
  x2 = LpVariable ( "BeefPercent", 0 )
#
#  Define the objective function, including a title,
#  as the cost per gram of the two ingredients.
#  pulp() would not accept "prob = prob + ..."
#
  prob += 0.013 * x1 + 0.008 * x2, "Total Cost of Ingredients per can"
#
#  Define the nutrition constraints.
#
  prob +=  x1 + x2 == 100, "PercentagesSum"
  prob +=  0.100 * x1 + 0.200 * x2 >= 8.0, "ProteinRequirement"
  prob +=  0.080 * x1 + 0.100 * x2 >= 6.0, "FatRequirement"
  prob +=  0.001 * x1 + 0.005 * x2 <= 2.0, "FiberRequirement"
  prob +=  0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"
#
#  Write an LP file for this problem.
#
  prob.writeLP ( "pulp_test02.lp" )
#
#  Solve the problem. 
#  Instead of a blank, the argument list could specify a particular
#  solver, such as CPLEX().
#
  prob.solve ( )
#
#  Print status.
#
  print ( "Status:", LpStatus[prob.status] )
#
#  Print the optimal variable values.
#
  for v in prob.variables():
    print ( v.name, "=", v.varValue )
#
#  Print the objective value.
#
  print ( "Total Cost of Ingredients per can = ", value(prob.objective) )

  return

def pulp_test03 ( ):

#*****************************************************************************80
#
## pulp_test03() solves a set partitioning problem.
#
#  Discussion:
#
#    Wedding guests (elements of a set S) are to be assigned to specific
#    tables with limited seating.  It is desired to maximize the
#    "happiness" of the guests
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips and Stuart Mitchell.
#
  import pulp

  print ( '' )
  print ( 'pulp_test03():' )
  print ( '  Solve a set partitioning problem to seat wedding guests.' )
#
#  Define parameters, including 18 guests labeled A through R.
#
  max_tables = 5
  max_table_size = 4
  guests = "W B S D E U G Y I T K L Z N X V Q R".split()
#
#  List all possible tables.
#
  possible_tables = [ tuple(c) \
    for c in pulp.allcombinations ( guests, max_table_size ) ]
#
#  A binary variable reports that a particular table setting is used.
#
  x = pulp.LpVariable.dicts(
    "table", possible_tables, lowBound = 0, upBound = 1, cat = pulp.LpInteger )
#
#  Name the problem and specify it is a minimization.
#
  prob = pulp.LpProblem ( "Wedding", pulp.LpMinimize )
#
#  The objective function is the total happiness.
#
  prob += pulp.lpSum ( [ happiness(table) * x[table] \
    for table in possible_tables ] )
#
#  Constraint: No more than max_tables tables can be used.
#
  prob += (
    pulp.lpSum ( [ x[table] for table in possible_tables]) <= max_tables, \
    "Maximum_number_of_tables" )
#
#   Constraint: Each guest must be seated at one and only one table.
#
  for guest in guests:
    prob += (
      pulp.lpSum ( 
      [ x[table] for table in possible_tables if guest in table ] ) == 1,
      f"Must_seat_{guest}", )
#
#  Write an LP file for this problem.
#
  prob.writeLP ( "pulp_test03.lp" )
#
#  Request solution.
#
  prob.solve()
#
#  Print status.
#
  print ( "Status:", LpStatus[prob.status] )
#
#  Report the results.
#
  print ( "The number of possible tables is", len ( possible_tables ) )
  for table in possible_tables:
    if ( x[table].value() == 1.0 ):
      print ( table )

  h = 0
  for table in possible_tables:
    if ( x[table].value() == 1.0 ):
      h = h + happiness ( table )
  print ( '  Total happiness = ', h )

  return

def happiness ( \
  table: Union[ \
    Tuple[str, str], Tuple[str, str, str, str], Tuple[str], \
    Tuple[str, str, str] ], ) -> int:

#*****************************************************************************80
#
## happiness() evaluates the "happiness" of a table of wedding guests.
#
#  Discussion:
#
#    Calculate the distance between the letters representing
#    the first seated person and the last.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips, Stuart Mitchell, Nathan Sudermann-Merx.
#
#  Input:
#
#    table: a representation of the table seating arrangement.
#
#  Output:
#
#    h: the happiness function.
#
  h = abs ( ord ( table[0] ) - ord ( table[-1] ) )

  return h

def pulp_test04 ( ):

#*****************************************************************************80
#
## pulp_test04() solves a Sudoku puzzle.
#
#  Discussion:
#
#    Create 729 binary variables of the form [v][r][c] where 
#    v is True if the corresponding digit occurs in row r and column c.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips, Stuart Mitchell, Nathan Sudermann-Merx.
#
  print ( '' )
  print ( 'pulp_test04():' )
  print ( '  Solve a Sudoku.' )
#
#  All values, rows, and columns must take on a value between 1 and 9.
#
  VALS = range ( 1, 10 )
  ROWS = range ( 1, 10 )
  COLS = range ( 1, 10 )
#
#  Boxes is a list of nine lists.
#  Each list gives the coordinates of the squares in a box of the Sudoku grid.  
#  The first list is:
#    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
#  The second is:
#    [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
#
  Boxes = [
    [ ( 3 * i + k + 1, 3 * j + l + 1 ) for k in range(3) for l in range(3) ]
    for i in range(3)
    for j in range(3)
  ]
#
#  Create a name for the problem.
#
  prob = LpProblem ( "Sudoku" )
#
#  Define the variables which will indicate which digit shows up in which location.
#  These are binary, and will each be either 0 or 1.
#
  choices = LpVariable.dicts ( "Choice", ( VALS, ROWS, COLS), cat = "Binary" )
#
#  For each square, only one of the 9 possible values can be chosen.
#
  for r in ROWS:
    for c in COLS:
       prob += lpSum ( [ choices[v][r][c] for v in VALS ] ) == 1
#
#  Each value occurs exactly once in each row, column, and box.
#
  for v in VALS:

    for r in ROWS:
      prob += lpSum ( [ choices[v][r][c] for c in COLS ] ) == 1

    for c in COLS:
      prob += lpSum ( [ choices[v][r][c] for r in ROWS ] ) == 1

    for b in Boxes:
      prob += lpSum ( [ choices[v][r][c] for (r, c) in b ] ) == 1
#
#  The initial data imposes constraints on some of the variables.
#
  input_data = [
    (5, 1, 1),
    (6, 2, 1),
    (8, 4, 1),
    (4, 5, 1),
    (7, 6, 1),
    (3, 1, 2),
    (9, 3, 2),
    (6, 7, 2),
    (8, 3, 3),
    (1, 2, 4),
    (8, 5, 4),
    (4, 8, 4),
    (7, 1, 5),
    (9, 2, 5),
    (6, 4, 5),
    (2, 6, 5),
    (1, 8, 5),
    (8, 9, 5),
    (5, 2, 6),
    (3, 5, 6),
    (9, 8, 6),
    (2, 7, 7),
    (6, 3, 8),
    (8, 7, 8),
    (7, 9, 8),
    (3, 4, 9),
    (1, 5, 9),
    (6, 6, 9),
    (5, 8, 9),
  ]

  for v, r, c in input_data:
    prob += choices[v][r][c] == 1
#
#  Write the problem to an LP file.
#
  prob.writeLP ( "pulp_test04.lp" )
#
#  Solve the problem.
#
  prob.solve()
#
#  Print the solver status.
#
  print ( "Status:", LpStatus[prob.status] )
#
#  A file called sudoku.txt is created.
#
  sudoku = open ( "sudoku.txt", "w" )

  for r in ROWS:
    if r in [ 1, 4, 7 ]:
      sudoku.write ( "+-------+-------+-------+\n" )
    for c in COLS:
      for v in VALS:
        if value(choices[v][r][c]) == 1:
          if c in [ 1, 4, 7 ]:
            sudoku.write ( "| " )
          sudoku.write ( str(v) + " " )
          if c == 9:
            sudoku.write ( "|\n" )
  sudoku.write ( "+-------+-------+-------+"  )
  sudoku.close()

  print ( "Solution written to sudoku.txt" )

  return

def pulp_test05 ( ):

#*****************************************************************************80
#
## pulp_test05() solves a transportation problem to minimize the cost.
#
#  Discussion:
#
#    There are 2 warehouses of beer, and 5 bars needing to be supplied.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 April 2026
#
#  Author:
#
#    John Burkardt
#    Original PULP version by Antony Phillips and Stuart Mitchell.
#
  print ( '' )
  print ( 'pulp_test05():' )
  print ( '  Solve a transportation problem.' )
#
#  Create a list of warehouses.
#
  Warehouses = [ "A", "B" ]
#
#  Create a dictionary of the units of supply at each warehouse.
#
  supply = { "A": 1000, "B": 4000 }
#
#  List the bars.
#
  Bars = [ "1", "2", "3", "4", "5" ]
#
#  Create a dictionary of the units of demand at each bar.
#
  demand = { "1":500, "2": 900, "3": 1800, "4":200, "5": 700 }
#
#  Create a list of lists, the cost from Warehouse (row) to Bar (column).
#
  costs = [ \
    [ 2, 4, 5, 2, 1 ], \
    [ 3, 1, 3, 2, 3 ] ]
#
#  Turn the cost data into a dictionary.
#  costs_dict[A][3] = 5.  In the definition, the final 0 is the
#  default value returned for an unrecognized key.
#
  costs_dict = makeDict ( [ Warehouses, Bars ], costs, 0 )
#
#  Initialize an LP problem in which we minimize the objective function.
#  pulp() complained when I had blanks in the problem name.
#
  prob = LpProblem ( "Beer", LpMinimize )
#
#  List all possible routes.
#
  Routes = [ ( w, b ) for w in Warehouses for b in Bars ]
#
#  Create a dictionary of variables.
#  The data is the route.
#  The key is the warehouse and bar names.  
#  The limits are 0 and None.
#
  vars = LpVariable.dicts ( "Route", ( Warehouses, Bars), 0, None, LpInteger )
#
#  Define the objective.
#
  prob += (
    lpSum ( [ vars[w][b] * costs_dict[w][b] for (w, b) in Routes] ),
    "Sum_of_Transporting_Costs",
)
#
#  Define the supply and demand constraints.
#
  for w in Warehouses:
    prob += (
      lpSum([vars[w][b] for b in Bars]) <= supply[w],
      f"Sum_of_Products_out_of_Warehouse_{w}",
    )
#
#  The demand minimum constraints are added to prob for each demand node (bar)
#
  for b in Bars:
    prob += (
      lpSum([vars[w][b] for w in Warehouses]) >= demand[b],
      f"Sum_of_Products_into_Bar{b}",
    )
#
#  Write the problem to an LP file.
#
  prob.writeLP ( "pulp_test05.lp" )
#
#  Solve the problem.
#
  prob.solve()
#
#  Print the solver status.
#
  print ( "Status:", LpStatus[prob.status] )
#
#  Print the optimal variable values.
#
  for v in prob.variables():
    print ( v.name, "=", v.varValue )
#
#  Print the optimized cost.
#
  print ( "Total Cost of Transportation = ", value(prob.objective) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  pulp_test ( )
  timestamp ( )
 
