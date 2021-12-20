!=====================================
! projectile.f90
! Author: Devansh Shukla
!-------------------------------------

program projectile
    ! Program to compute motion of a particle moving in projectile motion.

    implicit none
    real*8, parameter :: PI=3.141592, g=9.81
    real*8 :: x, y, vx, vy
    real*8 :: theta, v0x, v0y, v0
    real*8 :: t0, tf, dt, t
    character(len=*), parameter :: fmt1 = "(F12.4, F12.4, F12.4, F12.4, F12.4)"

    open(unit=8, file="Projectile.dat")

    print *, "----------------------------------------"
    print *, "Enter v0, theta(deg)"
    read *, v0, theta
    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    print *, "----------------------------------------"

    print *, "v0, theta =", v0, theta
    print *, "t0, tf, dt=", t0, tf, dt

    if (v0 .le. 0.0) stop "Illegal value of v0<=0"
    if (theta .lt. 0.0 .or. theta .gt. 90.0 ) &
    stop "Illegal value of theta"
    print *, "----------------------------------------"

    theta = (PI/180.0) * theta      ! theta radians
    v0x = v0*cos(theta)
    v0y = v0*sin(theta)

    print "(A12, A12, A12, A12, A12)", "time", "x(t)", "y(t)", "vx(t)", "vy(t)"
    t = t0
    do while(t <= tf)
        x = v0x * t
        y = v0y * t - 0.5*g*t*t
        vx = v0x
        vy = v0y - g*t
        write (*, fmt1) t, x, y, vx, vy
        write (8, fmt1) t, x, y, vx, vy
        if (y < 0.0) stop "y-ve"
        t = t + dt
    enddo
    print *, "----------------------------------------"
    close(8)
end program projectile
