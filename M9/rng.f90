!==========================================
! rng.f90
! Author: Devansh Shukla
!------------------------------------------
program rng_generator
    implicit none
    ! Define the variables
    integer :: A=0, C=0, M=0, x_0=0, x_1=0, i=0, n=10
    character(len=*), parameter :: fmt="(xI2,I6,I6)"
    ! Open data file
    open(unit=8, file="random_no.dat")
    ! Get input from user
    print *, "Enter A, C, M, x0"
    read *, A, C, M, x_0
    print *, "Enter no of random numbers(n)"
    read *, n
    print *, "-----------------"

    print "(xA2x, A6, xxA6)", "i", "I(i)", "I(i+1)"
    ! Compute
    do i = 0, n, 1
        ! Compute the pseudorandom number according to the
        ! given formula
        x_1 = mod(A*x_0 + C, M)
        write (*, fmt) i, x_0, x_1
        ! Writing the computed parameters to the data file
        write (8, fmt) i, x_0, x_1
        x_0 = x_1
    end do
    print *, "-----------------"
    ! Close file
    close(8)

end program rng_generator
