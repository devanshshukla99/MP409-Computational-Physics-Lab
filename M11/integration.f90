!==========================================
! integration.f90
! Author: Devansh Shukla
!------------------------------------------
program integration
    implicit none
    ! Define the variables
    real*8 :: x, y, a=0.0, b=0.0, max=0.0, min=0.0, step=0.1, t=0, i=0.0, r=0.0
    real*8 :: f, area, int_area, j
    integer :: hits=0, n=0
    character(len=*), parameter :: fmt="(xF10.3,xF10.3,xF10.3)"

    ! Define the function
    f(x) = (x**2 + 4*x + 9)**3 * (2*x + 4)
    
    ! Open the data file
    open(unit=8, file="int_area.dat")

    ! Get input from the user
    print *, "Enter a, b"
    read *, a, b
    print *, "Enter step, n"
    read *, step, n
    print *, "-------------------"

    ! Max of f(x) in [a, b]
    i = a
    max = f(i)
    min = f(i)
    do while (i .le. b)
        t = f(i)
        if (max .lt. t) then
            max = t
        endif
        if (min .gt. t) then
            min = t
        endif
        i = i + step
    enddo
    print "(A,F10.3,xxA,F10.3)", "MIN:", min, "MAX:", max
    j = 0.0
    ! Compute the integration
    do while(j .le. n)
        call random_number(r)
        x = a + (b-a)*r
        call random_number(r)
        y = abs(max*r)
        ! print "(F10.3, xxF10.3)", y, f(x)
        write (8, fmt) x, y, f(x)
        if (y .le. abs(f(x))) then
                hits = hits + 1
        endif
    j = j + step
    enddo
    
    area = (b-a) * max
    int_area = area * hits * step / real(n)
    ! Print for the user
    print "(A,I6)", "HITS=", hits
    print "(A,F10.3)", "INTEGRATION AREA=", int_area
    print *, "-------------------"

    ! Close the data file
    close(8)

end program integration
