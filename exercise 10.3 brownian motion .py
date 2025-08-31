import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# lattice size and steps
L = 101
steps = 1_000_000
skip = 500  # 每隔多少步更新一次動畫

# 四個方向 (dx, dy)
dirs = np.array([[1,0], [-1,0], [0,1], [0,-1]])
rng = np.random.default_rng(0)

# 初始在中心
x = y = L//2
xs = [x]; ys = [y]

def step_once(x, y):
    # 抽方向；若要出界就重抽直到合法
    while True:
        dx, dy = dirs[rng.integers(0, 4)]
        nx, ny = x + dx, y + dy
        if 0 <= nx < L and 0 <= ny < L:
            return nx, ny

# 預先做步進，但只存動畫需要的節點（每 skip 步）
frames = steps // skip
for _ in range(frames):
    for _ in range(skip):
        x, y = step_once(x, y)
    xs.append(x); ys.append(y)

# 畫動畫（只顯示目前位置；想畫軌跡可加 line.set_data）
fig, ax = plt.subplots()
ax.set_xlim(-0.5, L-0.5); ax.set_ylim(-0.5, L-0.5)
ax.set_aspect('equal')
ax.set_title("2D Brownian Motion (Random Walk)")
dot, = ax.plot([], [], 'o', ms=6)

def init():
    dot.set_data([], [])
    return dot,

def update(i):
    dot.set_data([xs[i]], [ys[i]])
    return dot,

ani = FuncAnimation(fig, update, frames=len(xs), init_func=init,
                    blit=False, interval=20, repeat=False)
plt.show()

