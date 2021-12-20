!==========================================
! particle2d.f90
! Author: Devansh Shukla
!------------------------------------------
program particle_2D
    ! Program to compute motion of a particle moving in a circle with uniform velocity

    implicit none
    real*8 :: x0, y0, t0, tf, dt, t
    real*8 :: x, y, vx, vy, lx0, lx1, ly0, ly1
    character(len=*), parameter :: fmt1 = "(F10.4,x,F10.4,x,F10.4,x,F10.4,x,F10.4)"

    open(unit=8, file="Particle2D.dat")

    print *, "---------------------------------------"
    print *, "Enter initial position x0, y0"
    read *, x0, y0

    print *, "Enter velocity vx, vy"
    read *, vx, vy

    print *, "Enter bounds lx0, lx1"
    read *, lx0, lx1

    print *, "Enter bounds ly0, ly1"
    read *, ly0, ly1

    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    print *, "---------------------------------------"

    print "(x,A,F10.4,F10.4)", "x0, y0=", x0, y0
    print "(x,A,F10.4,F10.4)", "lx0, lx1=", lx0, lx1
    print "(x,A,F10.4,F10.4)", "ly0, ly1=", ly0, ly1
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt=", t0, tf, dt
    print *, "---------------------------------------"

    print "(A10,A10,A10,xA10,xxA10)", "time", "x(t)", "y(t)", "vx(t)", "vy(t)"
    t = t0
    x = x0
    y = y0
    ! Formatting l0, l1 to our standards for fortran floating point arithmatic
    lx1 = lx1 - dt
    ly1 = ly1 - dt
    do while (t <= tf)
        write (*, fmt1) t, x, y, vx, vy
        write (8, fmt1) t, x, y, vx, vy
        x = x + vx * dt
        y = y + vy * dt
        t = t + dt
        if (x < lx0 .or. x > lx1) vx = -vx
        if (y < ly0 .or. y > ly1) vy = -vy
    enddo
    print *, "---------------------------------------"
    close(8)
end program particle_2D
