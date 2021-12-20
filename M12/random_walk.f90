!==========================================
! random_walk.f90
! Author: Devansh Shukla
!------------------------------------------
program walk
    implicit none
    ! Define the parameters
    real*8, dimension(1000000) :: X, Y
    real*8 :: pi=3.14159
    real*8 :: x_value=0.0, y_value=0.0, a=0.0, b=0.0, step=1, R=0.0
    integer :: i=0, j=0, n=0
    character(len=*), parameter :: fmt="(F12.3,xF12.3,xF12.3,F12.3)"

    ! open the data file
    open(unit=8, file="walk.dat")
    ! get input from user
    print *, "Enter the no. of steps (n)"
    read *, n

    ! initialize the array
    do j=1, n
       X(j) = 0.0
       Y(j) = 0.0
    enddo
    
    ! compute
    do i=1, n, 1
        call random_number(a)
        call random_number(b)
        x_value = step * cos(2*pi*a)
        y_value = step * sin(2*pi*b)
        X(i) = X(i-1) + x_value
        Y(i) = Y(i-1) + y_value
        write (8, fmt) x_value, y_value, X(i), Y(i)
        R = R + x_value**2 + y_value**2
    enddo
    ! print for the user
    print "(A, F10.3)", "The value of Radius, R =", sqrt(R)
    ! close the data file
    close(8)
end program walk
