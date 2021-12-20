!==========================================
! pi_calc.f90
! Author: Devansh Shukla
!------------------------------------------
program pi_estimate

    implicit none
    ! Defining the variables
    real*8 :: x=0.0, y=0.0, pi=0.0, dist=0.0
    integer :: i=0, hits=0, n=0
    character(len=*), parameter :: fmt = "(I4 F10.3 F10.3)"

    ! Opening the data file
    open(unit=8, file="random_no.dat")

    ! Getting input from the user for total no. of darts
    print *, "Enter the total no. of darts (n)"
    read *, n
    print *, "------------"

    ! Do-loop for computing
    do i=0, n, 1
        ! compute the random numbers
        call RANDOM_NUMBER(x)
        call RANDOM_NUMBER(y)
        ! compute the distance
        dist = sqrt(x**2 + y**2)
        ! Write the computed random numbers to the data file
        write (8,fmt) i, x, y
        ! Check if the distance is less than or equal to one
        ! if yes then increment `hits` by 1
        if (dist .le. 1.0) then
            hits = hits + 1
        endif
    enddo

    ! Compute the value of `pi` and write it to `stdout` for the user
    pi = 4.0 * hits/n
    print "(xA,F6.4)", "pi=", pi
    print *, "------------"

    ! Close the data file
    close(8)

end program pi_estimate
