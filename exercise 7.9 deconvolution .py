import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

def loaddata(name):
    return np.loadtxt(name)

def fft2D(y):   return fft.fft2(y)
def ifft2D(c):  return fft.ifft2(c)

def main():
    sigma = 25.0
    data  = loaddata("blur.txt").astype(float)
    H, W  = data.shape

    # 1) 在中心建立連續對稱座標
    y = np.arange(-H//2, H//2)
    x = np.arange(-W//2, W//2)
    X, Y = np.meshgrid(x, y)

    # 2) 以「中心為原點」建立高斯
    gauss_centered = np.exp(-0.5 * (X**2 + Y**2) / (sigma**2))
    gauss_centered /= gauss_centered.sum()

    # 3) 移回「左上角為原點」(與 data 一致) —— 注意是 ifftshift，不是 fftshift
    psf = fft.ifftshift(gauss_centered)

    # 4) 頻域除法（避免除以接近 0 的頻率；可用 Wiener 式的小常數）
    G = fft2D(psf)
    B = fft2D(data)
    eps = 1e-6                      # 或改成 Wiener：a_k = B * np.conj(G) / (np.abs(G)**2 + K)
    A_k = B / (G + eps)

    # 5) 反變換 & 取實部
    a = ifft2D(A_k).real

    # 顯示
    plt.imshow(data, cmap='gray'); plt.show()
    plt.imshow(psf, cmap="gray"); plt.title("PSF (peak at top-left)"); plt.show()
    plt.imshow(a, cmap="gray");   plt.title("Deconvolved"); plt.show()

main()
