!********************************************************************************
! This program shows how the heapsort works for a simple list:
!
!             list = [ 12, 11, 13, -9, 6, 7, 18, 1]
!
! which will be ordered in descending or ascending order, depending on
! the input (type = min or max):
!
! Min-heap -> list = [-9, -1, 6, 7, 11, 12, 13, 18]
! Max-heap -> list = [18, 13, 12, 11, 7, 6, -1, -9]
!
! and then it adds a new element (4) to the orderd list and re-order it.
!
!------------------------------------------------------------------------
! Inuput: 
!        type = min or max
!
! Output:
!        On-screen print of the ordered list of a min/max-heap.
!        On-screen print of the ordered list with a new element added.
!------------------------------------------------------------------------
!
! Note: Try it by typing in a terminal,
!       %gfortran heapsort_v1.f90
!       %a.out
!
! Note: The heapsort was used in the advancing-front agglomeration scheme
!       developed and implemeted in NASA's FUN3D as described in a series
!       of papers:
!
!       "Development and Application of Agglomerated Multigrid Methods
!        for Complex Geometries", AIAA 2010-4731.
!
!       "Development and Application of Parallel Agglomerated Multigrid Methods
!        for Complex Geometries", AIAA 2011-3232.
!
!       It was used to order the list of control-volumes to be agglomerated
!       based on the number of non-agglomerated neighbor volumes, so that
!       agglomeration can be performed from the volumes with the least #
!       of neighbors, which helps keep the front as convex as possible and
!       avoid creating holes. The front list changes every time a volume is
!       agglomerated with neighbors and it needs to be re-ordered with new
!       front members (the neighbors of the newly agglomerated volumes).
!       It was so fast that the agglomeration can be peformed quickly inside
!       the solver every time it reads a grid.
!
!-------------------------------------------------------------------------------
!
!        written by Dr. Katate Masatsuka (info[at]cfdbooks.com),
!
! the author of useful CFD books, "I do like CFD" (http://www.cfdbooks.com).
!
!
! This is Version 0 (November 2019).
!
! This F90 code is written and made available for an educational purpose.
! This file may be updated in future.
!
! Please report bugs to Hiro at hiro(at)nianet.org.
!
! Katate Masatsuka, November 2019. http://www.cfdbooks.com
!********************************************************************************
 program heapsort_program

 implicit none

!Local vriables
 integer                            :: n_mylist, i, mo
 integer, allocatable, dimension(:) ::   mylist
 integer, allocatable, dimension(:) :: mylist_original

!Input variable
 character(80)                      :: type

!----------------------------------------------------
! Allocate a list array. Just large enough, say 100.

  allocate( mylist(         100) )
  allocate( mylist_original(100) )

!----------------------------------------------------
! Input parameter: 
!   type = min for min-heap
!   type = max for max-heap

  write(*,*) 
  write(*,*) " Input: heap type = min or max"
   read(*,*) type

!----------------------------------------------------
! Define the list to be ordered with the size n_mylist,
! which cannot be larger than 100 since size(mylist)=100.
!
! (This is just an example. Use your own.)

  n_mylist  = 8

  mylist(1) = 12
  mylist(2) = 11
  mylist(3) = 13
  mylist(4) = -9
  mylist(5) =  6
  mylist(6) =  7
  mylist(7) = 18
  mylist(8) = -1

  mylist_original = mylist !Save the original list.

   write(*,*)
   write(*,*) "--------------------------------------------------------"
   write(*,*) "--------------------------------------------------------"
   write(*,*) "--- Let's generate ", trim(type), "-heap and sort the list below:" 
   write(*,*)

!----------------------------------------------------
! Print the original list.

   write(*,*)
   write(*,*) "---> Original list, list(:):"
  do i = 1, n_mylist
   write(*,*) i, mylist(i)
  end do

!----------------------------------------------------
! Build a heap, i.e., order the list.

  write(*,*)
  write(*,*) "---- Begin building a heap (sorting)....."
  call heap_build(type,n_mylist,mylist)
  write(*,*) "---- Finsihed  building a heap (sorting)....."
  write(*,*)

!----------------------------------------------------
! Print the ordered list.
! Note: Top is always the smallest/largest, and so
!       print the top, reordered and print the top.
!       Repeat this to print the elements in order.

   mo = n_mylist
   write(*,*)
   write(*,*) "---> Ordered list (print&delete the top from the heap):"
  do i = 1, n_mylist
   write(*,*) i, mylist(1)             !Always print the root (1) of the heap.
   call heap_delete(type,mo,mylist, 1) !Delete the top and re-order.
  end do

! At each heap_delete, the top is placed in the last and ignored(deleted).
! So, at the end, the list array contains actually the original list
! correctly ordered in the reverse order.

!----------------------------------------------------
! Once the above deletion is complete, the list is
! correctly ordered within the list array but with
! a reverse order. So, print them from n_mylist to 1.

   write(*,*)
   write(*,*) "---> Write list(:) from the last to the first:"
  do i = n_mylist, 1, -1
   write(*,*) i, mylist(i)
  end do

! In other words, deleting the min-heap creates a max-heap array,
! and vice versa.

!----------------------------------------------------
!----------------------------------------------------
! Let's add a new element to the existing min/max-heap.

   write(*,*)
   write(*,*) "--------------------------------------------------------"
   write(*,*) "--------------------------------------------------------"
   write(*,*) "--- Let's add a new element : ", 4
   write(*,*)

 !Initialize the list and heapify it.
 !  This is needed since "list" has been altered by
 !  heap_delete in the above.

   write(*,*) " ----- Initalizing the list..."
   mylist = mylist_original

   write(*,*) " ----- Min/max-heapify the original list: ", trim(type), "-heap." 
   call heap_build(type,n_mylist,mylist)

 !Add the new element 4 to the min/max heap of the orginal list.
  write(*,*)
  write(*,*) " ----- Adding a new element....."
  call heap_add(type,n_mylist,mylist, 4)
  write(*,*) " ----- Finsihed adding a new element......"
  write(*,*)

 !Print the result:
    mo = n_mylist
    write(*,*)
    write(*,*) "---> Ordered list (print&delete the top from the heap):"
   do i = 1, n_mylist
    write(*,*) i, mylist(1)             !Always print the root (1) of the heap.
    call heap_delete(type,mo,mylist, 1) !Delete the top and re-order.
   end do

!----------------------------------------------------
!----------------------------------------------------

   write(*,*)
   write(*,*) " Successfully finished."

 stop

!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------
!-----------------------------------------------------------------------------

 contains

!-----------------------------------------------------------------------------
!
! This builds a min/max-heap from an arbitrary list.
!
!  Ex. list=[12,11,13,-9,6,7,18,-1] forms the heap shown below:
!
!               12(1)
!              /     \ 
!          11(2)    13(3)
!           / \      /  \
!       -9(4) 6(5)  7(6) 18(7)
!         /
!     -1(8)
!
!  This subroutine will rearrange it into a min/max-heap.
!
!  If type="min", then a min-heap:
!
!               -9(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!         /
!     18(8)
!
!  If type="max", then a max-heap:
!
!               18(1)
!              /     \ 
!          13(2)     12(3)
!           / \      /  \
!       11(4) 7(5) 6(6) -1(7)
!         /
!     -9(8)
!
!
! The list is ordered by applying the rule: the parent value must be
! smaller(min-heap)/larger(max-heap) then the values of its two children.
! Below, we enforce this rule beginning from the parent (n/2) of
! the last element (n).
!
! Note that the ubroutine "heapify" is recursive and it calls itself
! to make sure the min/max-heap is maintained.
!
!-----------------------------------------------------------------------------
  subroutine heap_build(type,n,list)

  character(80),         intent(in)    :: type
  integer,               intent(in   ) :: n
  integer, dimension(:), intent(inout) :: list

 !Local variables
  integer :: i

  !Note: n/2 will be an integer, removing any fraction: e.g., 9/2=4, 7/2=3, etc.

   do i = n/2, 1, -1
    call heapify_down(type,n,list, i)
   end do

  end subroutine heap_build

!-----------------------------------------------------------------------------
!
! To make a subtree of the list rooted at the index i become a min/max-heap
! and continues down the tree.
!
!       list(i)
!        /   \      The tree on the left will become a min/max-heap.
!     left  right 
!    =2*i  =2*i+1
!
!
!  Ex. type = "min"
!           11(2)         -9(2)
!            / \     ->    / \
!        -9(4) 6(5)     11(4) 6(5)
!
!  Ex. type = "max"
!           11(2)         11(2)
!            / \     ->    / \      No change since the root is always max.
!        -9(4) 6(5)     -9(4) 6(5)
!
!  Then, it recursively calls itself as long as the root is replace by left
!  or right, and heapifies all the trees below.
!
!-----------------------------------------------------------------------------
  recursive subroutine heapify_down(type,n,list, i)

  character(80),         intent(in)    :: type
  integer,               intent(in   ) :: n
  integer, dimension(:), intent(inout) :: list
  integer,               intent(in)    :: i

 !Local variables
  integer :: l, r, smallest, largest

   if ( i == 0 ) return

  !Left and right children

          l = 2*i
          r = 2*i + 1

  !----------------------------------------------------------
  ! Min-heap

   if (trim(type) == "min") then

    !Let's assume the root is the smallest.
     smallest = i

    !Left element may be the smallest.
     if ( l <= n .and. list(l) < list(i) ) then
         smallest = l
     endif

    !Left element may be the smallest.
     if ( r <= n .and. list(r) < list(smallest) ) then
        smallest = r
     endif

    !Push up the smallest to the root (swap with the original root).
     if ( smallest == i ) then
      return
     else
      call swap_list(       list, i, smallest)
      call heapify_down(type,n,list, smallest) !Go down.
     endif

  !----------------------------------------------------------
  ! Max-heap

   elseif (trim(type) == "max") then
   
    !Let's assume the root is the largest.
     largest = i

    !Left element may be the largest.
     if ( l <= n .and. list(l) > list(i) ) then
         largest = l
     endif

    !Left element may be the largest.
     if ( r <= n .and. list(r) > list(largest) ) then
        largest = r
     endif

    !Push up the largest to the root (swap with the original root).
     if ( largest == i ) then
      return
     else
      call swap_list(       list, i, largest)
      call heapify_down(type,n,list, largest) !Go down.
     endif

  !----------------------------------------------------------

   else

    write(*,*) " Invalid input: type = ", trim(type), " Stop..."
    stop

   endif
  !----------------------------------------------------------

  end subroutine heapify_down

!-----------------------------------------------------------------------------
!
! Swap the elements in the list.
!
! For example,
!  list(i) = 10   -> list(i) = -1
!  list(j) = -1      list(j) = 10
!
!-----------------------------------------------------------------------------
  subroutine swap_list(list, i, j)

  integer, dimension(:), intent(inout) :: list
  integer,               intent(in)    :: i, j

 !Local variables
  integer :: temp

      temp = list(i)
   list(i) = list(j)
   list(j) = temp

  end subroutine swap_list

!-----------------------------------------------------------------------------
!
! This deletes an element from a min/max-heap out of an arbitrary list.
!
! For example, if i==1 is requested to be removed from the min-heap below,
!
!               -9(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!         /
!     18(8)
!
! (1)Switch it with the last element:
!          -9(1) -> -9(8)
!          18(8) -> 18(1)
!
!               18(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!         /
!     -9(8)
!
! (2)Delete the last (just to reduce the size: n=n-1).
!
!               18(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!
! (3)Make sure the resulting heap is the min heap by calling
!    heapify(type,n,list, 1). The result is shown below.
!
!               -1(1)
!              /     \ 
!          7(2)     6(3)
!           / \      /  \
!      18(4) 11(5) 12(6) 13(7)
!
!-----------------------------------------------------------------------------
  subroutine heap_delete(type,n,list, i)

  character(80),         intent(in)    :: type
  integer,               intent(inout) :: n
  integer, dimension(:), intent(inout) :: list
  integer,               intent(in   ) :: i

 !Local variables
  logical :: not_last_one

    not_last_one = .true.
   if (i == n) then
    not_last_one = .false.
   endif

   !If i is not the last element, then place it in the last.
    if (not_last_one) call swap_list(list, i, n)

   !Then, delete the last element.
     n = n - 1

   !Well, list(n) stays there, but will not be accessed since
   !the size has been reduced by 1 (with n=n-1).

   !Note: If you continue to delete the top root element, e.g.,
   !      do i = 1, n
   !       call heap_delete(type,n,list, 1)
   !      end do
   ! then, the list will become a reverse-ordered array.


   !If i=n, then it is easy to delete it.
   !If not, the heap has been altered by the swap (i<->n).
   !So, heapify the list.
   if (not_last_one) then

    !Make sure the subtrees rooted at i is mi/maxn-heap.
     call heapify_down(type,n,list, i)

   endif


  end subroutine heap_delete

!-----------------------------------------------------------------------------
!
! This adds a new element to the existing min/max-heap.
!
! For example, if the value 4 is added to the min-heap below,
!
!               -9(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!         /
!     18(8)
!
! (1)Store the 4 as the last element:
!
!               -9(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       7(4) 11(5) 12(6) 13(7)
!        / \
!    18(8) 4(9)
!
! (2)Make sure the resulting heap is the min heap by calling
!    heapify_up(type,n,list, n). The result is shown below.
!
!               -9(1)
!              /     \ 
!          -1(2)     6(3)
!           / \      /  \
!       4(4) 11(5) 12(6) 13(7)
!        / \
!    18(8) 7(9)
!
!-----------------------------------------------------------------------------
  subroutine heap_add(type,n,list, ivalue)

  character(80),         intent(in)    :: type
  integer,               intent(inout) :: n
  integer, dimension(:), intent(inout) :: list
  integer,               intent(in   ) :: ivalue

 !Expand the list by one and add the new element to the last place.

           n = n + 1
     list(n) = ivalue
 
 !Keep the min/max-heap by checking upwards from the bottom.

    call heapify_up(type,n,list, n/2) !Begin with the parent of n -> n/2.

  end subroutine heap_add

!-----------------------------------------------------------------------------
!
! To make a subtree of the list rooted at the index i become a min/max-heap,
! and continues to the parent and beyond.
!
!       list(i)
!        /   \      The tree on the left will become a min/max-heap.
!     left  right 
!    =2*i  =2*i+1
!
!
!  Ex. type = "min"
!           11(2)         -9(2)
!            / \     ->    / \
!        -9(4) 6(5)     11(4) 6(5)
!
!  Ex. type = "max"
!           11(2)         11(2)
!            / \     ->    / \      No change since the root is always max.
!        -9(4) 6(5)     -9(4) 6(5)
!
!  Then, it recursively calls itself as long as the root is replace by left
!  or right, and heapifies all the trees above.
!
!-----------------------------------------------------------------------------
  recursive subroutine heapify_up(type,n,list, i)

  character(80),         intent(in)    :: type
  integer,               intent(in   ) :: n
  integer, dimension(:), intent(inout) :: list
  integer,               intent(in)    :: i

 !Local variables
  integer :: l, r, smallest, largest

   if ( i == 0 ) return

  !Left and right children

          l = 2*i
          r = 2*i + 1

  !----------------------------------------------------------
  ! Min-heap

   if (trim(type) == "min") then

    !Let's assume the root is the smallest.
     smallest = i

    !Left element may be the smallest.
     if ( l <= n .and. list(l) < list(i) ) then
         smallest = l
     endif

    !Left element may be the smallest.
     if ( r <= n .and. list(r) < list(smallest) ) then
        smallest = r
     endif

    !Push up the smallest to the root (swap with the original root).
     if ( smallest == i ) then
      return
     else
      call swap_list(     list, i, smallest)
      call heapify_up(type,n,list,      i/2) !Go up to the parent.
     endif

  !----------------------------------------------------------
  ! Max-heap

   elseif (trim(type) == "max") then
   
    !Let's assume the root is the largest.
     largest = i

    !Left element may be the largest.
     if ( l <= n  .and. list(l) > list(i) ) then
         largest = l
     endif

    !Left element may be the largest.
     if ( r <= n .and. list(r) > list(largest) ) then
        largest = r
     endif

    !Push up the largest to the root (swap with the original root).
     if ( largest == i ) then
      return
     else
      call swap_list(     list, i, largest)
      call heapify_up(type,n,list,     i/2) !Go up to the parent.
     endif

  !----------------------------------------------------------

   else

    write(*,*) " Invalid input: type = ", trim(type), " Stop..."
    stop

   endif
  !----------------------------------------------------------

  end subroutine heapify_up


  end program heapsort_program

