#coding=utf-8
# @Author: yangenneng
# @Time: 2018-05-05 20:28
# @Abstract： Newton Method based on backtracking line search
'''
Newton’s method.
given a starting point x ∈ domf, tolerance ǫ > 0.
repeat
    1. Compute the Newton step and decrement.
     xnt := −∇2f(x)−1∇f(x); λ2 := ∇f(x)T∇2f(x)−1∇f(x).
    2. Stopping criterion. quit if λ2/2 ≤ ǫ.
    3. Line search. Choose step size t by backtracking line search.
    4. Update. x := x + txnt.
'''
from matplotlib.pyplot import *
import numpy as np

def f(x):
    return (x-3)*(x-3)

def f_grad(x):
    return 2 * (x - 3)

def f_grad_2(x):
    return 2


# search step length
# x0: start point
def BacktrackingLineSearch(x0):
    # init data 0 < c < 0.5 (typical:10^-4 0) < rho <= 1
    alpha = 1
    x = x0
    rho = 0.8
    c = 0.0001

    # Armijo condition
    while f( x + alpha * (-f_grad(x)) ) > f(x) + c * alpha * f_grad(x) * (-f_grad(x)) :
        alpha *= rho

    return alpha

# Gradient Descent method
def NewtonMethod():
    x0 = 0
    error = 10
    curve_y = [f(x0)]
    curve_x = [x0]

    lambda_squre = 1
    error = 1e-4
    while lambda_squre/2 > error:
        stepLength = BacktrackingLineSearch(x0)
        xnt=- (1/f_grad_2(x0))*(f_grad(x0))
        x0 = x0 + stepLength * xnt
        y1 = f(x0)
        lambda_squre=(f_grad(x0)) * (1/(f_grad_2(x0))) * (f_grad(x0))

        curve_x.append(x0)
        curve_y.append(y1)

    plot(curve_y, 'g*-')
    plot(curve_x, 'r+-')
    xlabel('iterations')
    ylabel('objective function value')
    legend(['backtracking line search algorithm'])
    show()

if __name__ == "__main__":
    NewtonMethod()

