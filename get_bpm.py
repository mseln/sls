import numpy as np
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

import matplotlib.pyplot as plt
from scipy.io import wavfile

#[fs, s] = wavfile.read('viol.wav');
#s = s[10000:200000, 0];

fs = 100;
dt = 1/fs;
stop = 2;
n = stop*fs;

t = np.linspace(0, stop-dt, n);
print(dt, t);

f = 25;
x = np.cos(2*np.pi*f*t);

X = np.fft.fftshift(np.fft.fft(x));
df = fs / n;
f  = np.linspace(-1/(2*dt)+1, 1/(2*dt)-1, n);

plt.plot(f, np.abs(X))
plt.show()
"""
y = np.sin(10*2*np.pi*x);

Ryy = 1/(2*y.size)*np.abs(np.fft.fft(y))**2;

# print(str(x.size) + " " + str(y.size) );
w = np.hamming(11);
Ryy = np.convolve(Ryy, w, 'same')

"""
