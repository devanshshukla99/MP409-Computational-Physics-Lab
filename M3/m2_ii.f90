!==============================================================
! Uniform circular motion in polar coordinates
! Author: Devansh Shukla
!--------------------------------------------------------------
program CircularMotion_Polar
    ! Program to compute motion of a particle moving in a circle with uniform velocity in polar coordinates.

    implicit none
    real*8, parameter :: PI = 3.141593
    real*8 :: R=0.0, omega=0.0, theta0=0.0, theta, x, y
    real*8 :: t0=0.0, tf=0.0, dt=0.0, t=0.0
    character(len=*), parameter :: fmt1 = "(F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6)"
    
    theta(t) = theta0 + omega*(t-t0)
    x(t) = R*cos(theta(t))
    y(t) = R*sin(theta(t))

    open(UNIT=8, FILE="CirclePolar.dat") 

    ! Input
    print *, "Enter angular velocity(omega) and radius (R)"
    read *, omega, R
    if (omega .le. 0.0) stop "Illegal  value of omega"
    if (R .le. 0.0) stop "Illegal value of R"

    print *, "Enter the value of theta0"
    read *, theta0

    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    if (dt .le. 0.0) stop "Illegal value of dt"

    print *, "----------------------------------------------------------"
    print "(x,A,F10.4)", "omega =", omega
    print "(x,A,F10.4)", "T =", 2.0*PI / omega
    print "(x,A,F10.4,F10.4,F10.4)", "theta0 =", theta0
    print "(x,A,F10.4)", "R =", R
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt =", t0, tf, dt
    print *, "----------------------------------------------------------"

    write (8, *) "# t0=", t0
    write (8, *) "# t R theta x y"
    print "(xA10,A10,xA10,A10,A10)", "time", "R", "theta(t)", "x(t)", "y(t)"
    ! Computing
    t = t0
    do while (t <= tf)
        write (*, fmt1) t, R, theta(t), x(t), y(t)
        write (8, fmt1) t, R, theta(t), x(t), y(t)   
        t = t + dt
    enddo
    print *, "----------------------------------------------------------"
    close(8)

end program CircularMotion_Polar
