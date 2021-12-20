!==============================================================
! Uniform circular motion in cartesian coordinates
! Author: Devansh Shukla
!==============================================================
program CircularMotion_Cartesian
    ! Program to compute motion of a particle moving with uniform angular velocity in cartesian coordinates.

    implicit none
    real, parameter :: PI=3.141593
    real :: x0=0.0, y0=0.0, R=0.0, omega=0.0
    real :: x, y, dx, dy, ddx, ddy
    real :: t0=0.0, tf=0.0, dt=0.0, t=0.0
    character(len=*), parameter :: fmt1 = "(F10.4,x,F10.4,x,F10.4,x,F10.4,x,F10.4,x,F10.4,x,F10.4)"
    
    x(t) = x0 + R*cos(omega*(t-t0))
    y(t) = y0 + R*sin(omega*(t-t0))

    dx(t) = -R*omega*sin(omega*(t-t0))
    dy(t) = R*omega*cos(omega*(t-t0))
    
    ddx(t) = -R*omega*omega*cos(omega*(t-t0))
    ddy(t) = -R*omega*omega*sin(omega*(t-t0))

    open(UNIT=8, FILE="CircleCartesian.dat")
    
    ! input
    print *, "Enter angular velocity(omega) and radius (R)"
    read *, omega, R
    if (omega .le. 0.0) stop "Illegal  value of omega"
    if (R .le. 0.0) stop "Illegal value of R"
    
    print *, "Enter the value of x0, y0"
    read *, x0, y0

    print *, "Enter t0, tf, dt"
    read *, t0, tf, dt
    if (dt .le. 0.0) stop "Illegal value of dt"

    print *, "---------------------------------------------------"
    print "(x,A,F10.4,F10.4)", "omega, R =", omega, R
    print "(x,A,F10.4)", "T =", 2.0*PI/omega
    print "(x,A,F10.4,F10.4)", "x0, y0 =", x0, y0
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt =", t0, tf, dt
    print *, "---------------------------------------------------"

    write (8, *) "# x0=", x0
    write (8, *) "# y0=", y0
    write (8, *) "# t0=", t0
    write (8, *) "# t x y dx dy ddx ddy"
    print "(xA10,A10,xA10,A10,A10,xA10,xA10)", "time", "x(t)", "y(t)", "vx(t)", "vy(t)", "ax(t)", "ay(t)"
    ! Computing
    t = t0
    do while (t <= tf)
        write (*, fmt1) t, x(t), y(t), dx(t), dy(t), ddx(t), ddy(t)
        write (8, fmt1) t, x(t), y(t), dx(t), dy(t), ddx(t), ddy(t)
        t = t + dt
    enddo
    print *, "---------------------------------------------------"
    close(8)

end program CircularMotion_Cartesian
