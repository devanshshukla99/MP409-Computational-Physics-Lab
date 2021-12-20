!==========================================
! particle1d.f90
! Author: Devansh Shukla
!------------------------------------------
program particle_1D
    ! Program to compute motion of a particle trapped in a one dimension box.

    implicit none
    real*8 :: x0=0.0, t0=0.0, tf=0.0, dt=0.0, t=0.0
    real*8 :: x=0.0, vx=0.0, l0=0.0, l1=0.0
    character(len=*), parameter :: fmt1 = "(F10.4, x, F10.4, x, F10.4)"

    open(unit=8, file="Particle1D.dat")

    print *, "---------------------------------------"
    print *, "Enter initial position x0"
    read *, x0

    print *, "Enter velocity vx"
    read *, vx

    print *, "Enter bounds l0, l1"
    read *, l0, l1

    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    print *, "---------------------------------------"

    print "(x,A,F10.4)", "x0=", x0
    print "(x,A,F10.4,F10.4)", "l0, l1=", l0, l1
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt=", t0, tf, dt
    print *, "---------------------------------------"

    print "(A10,A10,A10)", "time", "x(t)", "vx"

    ! Formatting l0, l1 to our standards for fortran floating point arithmatic
    l0 = l0
    l1 = l1 - dt
    t = t0
    x = x0
    do while (t .le. tf)
        write (*, fmt1) t, x, vx
        write (8, fmt1) t, x, vx
        x = x + vx * dt          
        t = t + dt
        if (x .lt. l0 .or. x .gt. l1) vx = -vx
    enddo
    print *, "---------------------------------------"
    close(8)
end program particle_1D
