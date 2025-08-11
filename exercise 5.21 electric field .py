import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, linspace
from scipy.constants import epsilon_0, pi

def electric_potential(charge, separation, scale, resolution):
    phi_point = lambda r: charge / (4 * pi * epsilon_0 * r)
    dist = lambda a, b: np.linalg.norm(np.array(a) - np.array(b))
    q1 = (-separation/2, 0.0)   # negative
    q2 = ( separation/2, 0.0)   # positive

    eps = 1e-3
    xs = linspace(-scale/2, scale/2, resolution)
    ys = linspace(-scale/2, scale/2, resolution)

    phi = np.empty((resolution, resolution), float)
    for iy, y in enumerate(ys):
        for ix, x in enumerate(xs):
            p = (x, y)
            r1 = max(dist(p, q1), eps)
            r2 = max(dist(p, q2), eps)
            phi[iy, ix] = phi_point(r2) - phi_point(r1)  # +q at q2, -q at q1
    return phi, xs, ys

def electric_field_from_phi(phi, xs, ys):
    dx = 0.01
    dy = 0.01
    dphidy, dphidx = np.gradient(phi, dy, dx)  # order: (y, x)
    Ex = -dphidx
    Ey = -dphidy
    Emag = np.hypot(Ex, Ey)
    return Ex, Ey, Emag

def main():
    charge = 1.0
    separation = 0.1
    scale = 1.0
    resolution = 100

    phi, xs, ys = electric_potential(charge, separation, scale, resolution)
    Ex, Ey, Emag = electric_field_from_phi(phi, xs, ys)

    extent = [xs[0], xs[-1], ys[0], ys[-1]]

    plt.figure()
    plt.title("Potential (phi)")
    plt.imshow(phi, extent=extent, cmap='seismic', vmin=-5e9, vmax=5e9)  # 調 vmin/vmax 讓對比清楚
    plt.colorbar()

    plt.figure()
    plt.title("|E| (field magnitude)")
    plt.imshow(Emag, extent=extent, cmap='magma', vmax=np.percentile(Emag, 99))  # 避免極端值壓色階
    plt.colorbar()

    # 疊加電場箭頭（稀疏抽樣一下，避免太密）
    step = max(1, resolution // 30)
    X, Y = np.meshgrid(xs, ys)
    plt.quiver(X[::step, ::step], Y[::step, ::step], Ex[::step, ::step], Ey[::step, ::step], color='white', scale=3e11)

    plt.show()

if __name__ == "__main__":
    main()
