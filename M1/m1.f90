
program newton_raphson
    ! Program to compute approximate roots of polynomials using Newton-Raphson method of iterations.
    ! Author: Devansh Shukla

    implicit none
    integer :: j, m=1, n=1, big=0, iterations=50
    real :: x, i, h, f, df, f_value, old_f_value, initial_counter=-100, final_counter=100, guess_increment=0.5, tolerance=0.001
    real, dimension(10) :: guesses, roots

    ! M1 (a) (i)
    ! f(x) = x**3 - 3*x**2 + 2*x - 1
    ! df(x) = 3*x**2 - 6*x + 2

    ! M1 (a) (ii)
    ! f(x) = -2*x**2 + 3*x + 2
    ! df(x) = -4*x + 3

    ! M1 (b)
    ! f(x) = x**3 - 9*x**2 + 28.6479
    ! df(x) = 3*x**2 - 18*x

    ! Computing initial guess(es)
    print *,"----------------------------------------------------"
    print *, "Computing inital guesses"
    i = initial_counter
    old_f_value = f(i)
10  i = i + guess_increment
    f_value = f(i)
    if (f_value <= 0 .and. old_f_value >= 0) then
        guesses(n) = i
        n = n + 1
        print "(xxxx, F10.4, x, F10.6, x, F10.6)", i, f_value, old_f_value
    elseif (f_value >= 0 .and. old_f_value <= 0) then
        guesses(n) = i
        n = n + 1
        print "(xxxx, F10.4, x, F10.6, x, F10.6)", i, f_value, old_f_value
    endif
    if (i<final_counter) then
        old_f_value = f_value
        GOTO 10
    endif

    print *, "Initial guess ranges are:"
    do big=1, n-1, 1
        print "(xxxx,I1,A,F10.4,A,F10.4,A)", big, ". (", guesses(big), ",", guesses(big)-guess_increment, ")" 
    enddo

    ! Newton-raphson method
    print *,"----------------------------------------------------"
    print "(A)", "Computing root(s) via Newton-Raphson method"
    do big=1, n-1, 1
        x = guesses(big)
        print "(x, A10,F10.4)", "Tying x = ", x
        do j=0,iterations,1
            f_value = f(x) 
            h = f_value/df(x)
            old_f_value = x
            x = x - h
            print "(xxxx,A6,I1,xxx,A3,F10.6,xxx,A3,F10.6)", "itr = ", j, "x =", x, "f =", f(x)
            if (abs(x-old_f_value) < tolerance) then
                roots(m) = x
                m = m + 1
                print "(A17, F10.6)", "Converged at x =", x
                exit
            endif
        enddo
    enddo
    print *,"----------------------------------------------------"
    if (m .ne. 1) then
        print *, "Roots are:"
        do big=1, m-1, 1
            print "(xxxx,A4,F10.6)", "x = ", roots(big)
        enddo
    else
        print *, "Not convergent"
    endif
    print *,"----------------------------------------------------"

end program newton_raphson
