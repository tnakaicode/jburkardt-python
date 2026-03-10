def pert ( totalruns ):

#*****************************************************************************80
#
## pert() implements the Critical Path Method for a randomized problem.
#
#  Discussion:
#
#    This code executes the Critical Path Method (CPM) algorithm
#    modified to incorporate random task completion times for Fig.21.5
#    in the text.
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
#  Input:
#
#    integer TOTALRUNS, the number of iterations of the algorithm.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'pert():' )
  print ( '  Execute the Critical Path Method algorithm' )
  print ( '  modified to incorporate random task completion times for Fig.21.5' )
  print ( '  in the text.' )
#
#  number of tasks, where task #1 is the pseudo-task
#  BEGIN and the last task is the pseudo-task END
#  it is assummed that all tasks are numbered in
#  sequence, from BEGIN as task #1 to END
#
  ntasks = 8
#
#  initialize vector of critical tasks
#
  critical=zeros(1,15)
#
#  initialize vector of project completion times.
#
  duration=zeros(1,20)
                     
  data(1,:)=[0,0,0,0,0]  #enter individual task data, in the following
  data(2,:)=[1,1,2,4,0]  #format: for task i, data(i,:)=
  data(3,:)=[1,1,1,2,0]  #[<# of immediate predecessor tasks>,
  data(4,:)=[2,2,3,1,2]  #<task #'s of immediate predecessors>,
  data(5,:)=[2,2,3,2,4]  #<min time to do task>, <max time to do task>]
  data(6,:)=[1,4,2,4,0]  #IMPORTANT POINT 1: all data statements must be
  data(7,:)=[2,5,6,1,2]  #of the same length, so pad-out all statements
  data(8,:)=[1,7,0,0,0]  #that have less than the maximum length with
                          #zeros.
                        #IMPORTANT POINT 2: the data statements MUST be
                        #entered in sequence from BEGIN to END, i.e.,
                        #all of the predecessor tasks of each task
                        #must appear in earlier data statements
#                
  for run=1:totalruns   #run the cpm algorithm totalruns times            
  time=zeros(50,5)     #initialize matrix of important times
  p=zeros(50,50)       #initialize immediate predecessor matrix
  for i=1:ntasks            #for task i, get number of immediate predecessors
    npred=data(i,1)        #where data(i,2) to data(i,1+npred) are the task
                            #numbers of the immediate predecessors of task i
    k=1+npred
      for j=2:k
         p(i,data(i,j))=1  #tag the task pointed at by data(i,j) as
                            #an immediate predecessor of task i, i.e.,
                            #p(i,q)=1 if task q is an immediate
                            #predecessor of task i
      end
  mintime=data(i,k+1)
  maxtime=data(i,k+2)
  randomtime=mintime+(maxtime-mintime)*rand
#
#  enter time to do task i into matrix of important times.
#
  time(i,5)=round(randomtime)     

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
                                          #completion time of a
                  else                    #predecessor task to task i
                end
               else
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
#  Get the time required to do the project.
#
  projectdone=time(ntasks,1)  
     
  for i=ntasks:-1:1
#
#  initialize latest possible finish time for task i.
#  to do do this, look at all of the successor tasks for task i.
#  Find the one that starts soonest, the successor task that has 
#  the MINIMUM start time (if task i starts later than that time 
#  then that successor task will be delayed)
#
    lateftime=projectdone 

    for j=1:ntasks
#
#  if task i is an immediate predecessor task j (i.e., if task j is an
#  immediate successor of task i) then ...
#
       if p(j,i)==1

           if lateftime>time(j,3)    #if we have found a new minimum
                                     #start time for task j then ...
              lateftime=time(j,3)   #up-date late finish time
             else                    #for task i
           end
          else
        end
      end                             #have we checked for all successor tasks?
      time(i,4)=lateftime            #yes, so record latest time task i can end
      time(i,3)=lateftime-time(i,5)  #and latest time that task i can start
    end
#
#  Store results
#
    duration(projectdone)=duration(projectdone)+1          

    for i = 2: ntasks - 1

      slack=time(i,3)-time(i,1)

      if ( slack == 0 ):
        critical(i) = critical(i) + 1

  critical = critical / totalruns
  duration = duration / totalruns 
#
#  Graphics
#
  plt.clf ( )
  plt.bar ( critical )
  plt.title ( 'Critical task likelihood for each task of Fig. 21.5' )
  plt.xlabel ( 'Task number' )
  plt.ylabel ( 'Probability task is critical' )
  filename = 'pert1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.bar ( duration )
  plt.title ( 'Range for project completion time' )
  plt.xlabel ( 'Completion time for the project' )
  plt.ylabel ( 'Likelihood' )
  filename = 'pert2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

