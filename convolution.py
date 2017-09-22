import matplotlib.pyplot as plt
from scipy import signal as sig


x = [1, 1]
h = [2, 2, 2, 2]

conv = sig.convolve(x, h, mode='full')

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3)

ax1.stem(x)
ax2.stem(h)
ax3.stem(conv)
plt.show()