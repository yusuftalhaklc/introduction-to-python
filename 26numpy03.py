import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c = a-b
d = b**2

e = 10 * np.sin(a)
print(e<7)
print(a*b)
print(a@b) # matris çarpımı
print(a.dot(b))

f = np.ones((2,4))
g = np.zeros((2,4))