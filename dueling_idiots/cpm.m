def cpm ( ):

#*****************************************************************************80
#
## cpm() executes the Critical Path Method.
#
#  Discussion:
#
#    This code executes the Critical Path Method (CPM) algorithm
#    for the project shown in figure 21.1 in the text.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2023
#
#  Author:
#
#    Original MATLAB version by Paul Nahin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Paul Nahin,
#    Dueling Idiots and Other Probability Puzzlers,
#    Princeton, 2012,
#    ISBN: 978-0691155005.
#
  import numpy as np

  print ( '' )
  print ( 'cpm():' )
  print ( '  Execute the Critical Path Method for a particular project.' )
#
#  number of tasks, where task #1 is the pseudo-task
#  BEGIN and the last task is the pseudo-task END
#  it is assummed that all tasks are numbered in
#  sequence, from BEGIN as task #1 to END
#
  ntasks = 8
#
#  enter individual task data, in the following format:
#  for task i, data(i,:)=
#  [ <# of immediate predecessors>, <task #'s of immediate predecessors>, <task time> ]
#
#  IMPORTANT POINT 1: all data statements must be
#  of the same length, so pad-out all statements
#  that have less than the maximum length with
#  zeros.
#
#  IMPORTANT POINT 2: the data statements MUST be
#  entered in sequence from BEGIN to END, i.e.,
#  all of the predecessor tasks of each task
#  must appear in earlier data statements
#
  data(1,:)=[0,0,0,0]
  data(2,:)=[1,1,2,0]
  data(3,:)=[1,1,1,0]
  data(4,:)=[2,2,3,1]
  data(5,:)=[2,2,3,2]
  data(6,:)=[1,4,2,0]
  data(7,:)=[2,5,6,1]
  data(8,:)=[1,7,0,0]
#
#  initialize matrix of important times
#
  time = np.zeros ( 50, 5 )
#
#  initialize immediate predecessor matrix
#
  p = np.zeros ( [ 50, 50 ] )       

  for i=1:ntasks
#
#  for task i, get number of immediate predecessors where data(i,2) 
#  to data(i,1+npred) are the task numbers of the immediate predecessors 
#  of task i.
#
    npred=data(i,1)

    k=1+npred

    for j=2:k
      p(i,data(i,j))=1  #tag the task pointed at by data(i,j) as
                          #an immediate predecessor of task i, i.e.,
                          #p(i,q)=1 if task q is an immediate
                          #predecessor of task i
    end
    time(i,5)=data(i,k+1)   #enter time to do task i into
                          #matrix of important times
  end
#
#  Start forward pass to determine the earliest start and finish times
#  for each task, stored as time(i,1) and time(i,2), respectively.
#
  for i=1:ntasks
    earlyctime=0         #initialize earliest possible completion
                          #time for immediate predecessors of task i
                          #(we are looking for the immediate predecessor
                          #with the MAXIMUM completion time, as task i
                          #cannot be started until ALL of its predecessors
                          #are done)
    for j=1:ntasks                   
      if p(i,j)==1    #if task j is an immediate                
                          #predecessor of task i then .....
        if earlyctime<time(j,2)    #if we have found a new
                                          #maximum completion time then .....
          earlyctime=time(j,2)   #up-date maximum
                                          #completion time of a predecessor task to task i
          end
        end
      end                              #have we checked for all
                                          #predecessor tasks?
    time(i,1)=earlyctime             #yes, so record earliest time task i can
    time(i,2)=earlyctime+time(i,5)   #start and record earliest time task i
                                  #can be finished
  end                               #repeat for next task
#
#  Start backward pass to determine the latest start and finish times
#  for each task, stored as time(i,3) and time(i,4), respectively.
#
  projectdone=time(ntasks,1)       #get the time required to do the project
  for i=ntasks:-1:1
#
#  initialize latest possible finish time for task i.
#  To do do this, look at all of the successor tasks for
#  task i and find the one that starts soonest, the successor
#  task that has the MINIMUM start time (if task i starts later than
#  that time then that successor task will be delayed)
#
    lateftime=projectdone  

    for j=1:ntasks
#
#  if task i is an immediate predecessor
#  task j (i.e., if task j is an immediate successor of task i) then ...
#
      if p(j,i)==1
#
#  if we found a new minimum start time for task j then
#  up-date late finish time for task i.
#
        if lateftime > time(j,3)    
          lateftime=time(j,3)   
#
#  Have we checked for all successor tasks?
#  yes, so record latest time task i can end
#  and latest time that task i can start.
#
    time(i,4) = lateftime            
    time(i,3) = lateftime - time(i,5)  
#
#  Report the results.
#
  print ( '' )
  print ( '  Total time required for the project = ', projectdone )
  print ( '' )
  print ( '           early start  ' )
  print ( '  task        time     slack' )
  print ( '' )

  for i = 2 : ntasks - 1
   slack = time(i,3) - time(i,1)
   fprintf ( '  %4d           %g         %g' % ( i, time[i,1], slack ) )

  return

