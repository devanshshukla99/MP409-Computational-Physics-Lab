!==========================================
! particle3d.f90
! Author: Devansh Shukla
!------------------------------------------
program particle_3D
    ! Program to compute motion of a particle trapped in a 3d box

    implicit none
    real*8 :: x0, y0, z0, t0, tf, dt, t
    real*8 :: x, y, z, vx, vy, vz, lx0, lx1, ly0, ly1, lz0, lz1
    character(len=*), parameter :: fmt1 = "(F10.4,x,F10.4,x,F10.4,x,F10.4,x,F10.4,F10.4,x,F10.4)"

    open(unit=8, file="Particle3D.dat")

    print *, "---------------------------------------"
    print *, "Enter initial position x0, y0, z0"pe
    read *, x0, y0, z0

    print *, "Enter velocity vx, vy, vz"
    read *, vx, vy, vz

    print *, "Enter bounds lx0, lx1"
    read *, lx0, lx1

    print *, "Enter bounds ly0, ly1"
    read *, ly0, ly1

    print *, "Enter bounds lz0, lz1"
    read *, lz0, lz1

    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    print *, "---------------------------------------"

    print "(x,A,F10.4,F10.4,F10.4)", "x0, y0, z0=", x0, y0, z0
    print "(x,A,F10.4,F10.4)", "lx0, lx1=", lx0, lx1
    print "(x,A,F10.4,F10.4)", "ly0, ly1=", ly0, ly1
    print "(x,A,F10.4,F10.4)", "lz0, lz1=", lz0, lz1
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt=", t0, tf, dt
    print *, "---------------------------------------"

    print "(A10,A10,A10,xA10,xA10,xA10,xA10)", "time", "x(t)", "y(t)", "z(t)", "vx(t)", "vy(t)", "vz(t)"
    ! Formatting l0, l1 to our standards for fortran floating point arithmatic
    lx1 = lx1 - dt
    ly1 = ly1 - dt
    lz1 = lz1 - dt
    t = t0
    x = x0
    y = y0
    z = z0
    do while (t <= tf)
        write (*, fmt1) t, x, y, z, vx, vy, vz
        write (8, fmt1) t, x, y, z, vx, vy, vz
        x = x + vx * dt
        y = y + vy * dt
        z = z + vz * dt
        t = t + dt
        if (x < lx0 .or. x > lx1) vx = -vx
        if (y < ly0 .or. y > ly1) vy = -vy
        if (z < lz0 .or. z > lz1) vz = -vz
    enddo
    print *, "---------------------------------------"
    close(8)
end program particle_3D
