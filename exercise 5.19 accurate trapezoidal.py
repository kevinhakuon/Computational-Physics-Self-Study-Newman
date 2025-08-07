import numpy as np
from numpy import sin, pi
from pylab import scatter, show
from scipy.constants import k, hbar, c

# 被積分函數
def func(x):
    return sin(x)**2 / x**2

# 遞迴 adaptive trapezoidal 积分
def adaptive_trapezoidal(lower_bound, upper_bound, f_lower, f_upper, 
                         tolerance=1e-4, func=func, sample_points=None):

    if sample_points is None:
        sample_points = []

    width = upper_bound - lower_bound
    mid = (lower_bound + upper_bound) / 2
    f_mid = func(mid)
    sample_points.append(mid)

    # 單一 trapezoid
    integral_single = (f_lower + f_upper) * width / 2
    # 拆兩個 trapezoid
    integral_double = (f_lower + 2 * f_mid + f_upper) * width / 4
    error = abs(integral_single - integral_double) / 3

    if error > tolerance:
        left = adaptive_trapezoidal(lower_bound, mid, f_lower, f_mid, 
                                    tolerance / 2, func, sample_points)
        right = adaptive_trapezoidal(mid, upper_bound, f_mid, f_upper, 
                                     tolerance / 2, func, sample_points)
        return left + right
    else:
        return integral_double

# Main
def main():
    lower = 1e-4
    upper = 10
    sample_points = [lower, upper]  # 先放邊界點

    result = adaptive_trapezoidal(lower, upper, func(lower), func(upper), sample_points=sample_points)
    print("Integral result =", result)

    # 整理與畫圖
    sample_points = sorted(sample_points)
    y_list = func(np.array(sample_points))
    scatter(sample_points, y_list, s=0.5)
    show()

main()
