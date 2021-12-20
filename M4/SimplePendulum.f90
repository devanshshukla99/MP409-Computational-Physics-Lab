!==============================================================
! Simple Pendulum
! Author: Devansh Shukla
!==============================================================
program simple_pendulum
    ! Program to compute motion of a simple pendulum.

    implicit none
    real*8, parameter :: PI=3.141593, g=9.80665 !m/s^2
    real*8 :: l=0.0, omega=0.0, theta0=PI/4.0, theta, dtheta, ddtheta
    real*8 :: t0=0.0, tf=0.0, dt=0.0, t=0.0
    real*8 ::  x, y, vx, vy
    character(LEN=*), parameter :: FMT = "(F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6, x, F10.6)"
    character(len=*), parameter :: fmt1="(A10, A10, A10, xA10, xxxxA10, A10, A10, A10, xA10)"

    theta(t) = theta0*cos(omega*(t-t0))
    dtheta(t) = -omega * theta0 * sin(omega*(t-t0))
    ddtheta(t) = -omega * omega * theta0 * cos(omega*(t-t0))
    x(t) = l * sin(theta(t))
    y(t) = -l * cos(theta(t))
    vx(t) = l * dtheta(t) * cos(theta(t))
    vy(t) = l * dtheta(t) * sin(theta(t))

    open(UNIT=8, FILE="SimplePendulum.dat")

    print *, "Enter length (l)"
    read *, l
    omega = sqrt(g/l)

    print *, "Enter the value of theta0"
    read *, theta0

    print *, "Enter time: initial (t0), final (tf), increment (dt)"
    read *, t0, tf, dt
    if (dt .le. 0.0) stop "Illegal value of dt"

    print *, "------------------------------------------------------"
    print "(x,A,F10.4,F10.4,F10.4)", "l, omega, T =", l, omega, 2.0*PI / omega
    print "(x,A,F10.4,F10.4,F10.4)", "theta0 =", theta0
    print "(x,A,F10.4,F10.4,F10.4)", "t0, tf, dt =", t0, tf, dt
    print *, "------------------------------------------------------"
    print *, "Computing..."

    write (8, *) "# t0=", t0
    write (8, *) "# t l theta(t) dtheta(t) ddtheta(t) x(t) y(t) vx(t) vy(t)"

    print fmt1, "time", "length", "theta", "dtheta", "ddtheta(t)", "x(t)", "y(t)", "vx(t)", "vy(t)"
    t = t0
    do while (t <= tf)
        write (*, FMT) t, l, theta(t), dtheta(t), ddtheta(t), x(t), y(t), vx(t), vy(t)
        write (8, FMT) t, l, theta(t), dtheta(t), ddtheta(t), x(t), y(t), vx(t), vy(t)
        t = t + dt
    enddo
    print *, "------------------------------------------------------"
    close(8)

end program simple_pendulum
