import numpy as np
import time
import Test1
a = np.array([0.5, 1, 10, 100, 1000])
b = np.array([1, 2, 3, 4])
m = np.array([[2, 2, 2, 20],
              [2, 2, 2, 2],
              [2, 2, 2, 2]])
listy = [1, 2, 3, 4]
c = np.array([[1], [2], [3], [4], [5], [6]])            #är 6 x 1 matris
d = np.array([[10, 20, 30]])                            #är 1 x 3 materis, för att de kan matrix multipliceras
list1 = [1,2,3]
list2 = [3,4,5]
x = 0
m1 = np.random.randn(750)
m2 = np.random.randn(750, 16)
m3 = None

def main():
    start = time.time()
    #print(sigmoid(a))           #numpy smart
    #print(a**2)
    #print(sum(a))
    #print(a * b)
    #print(np.ones((a.shape[0], 1)))
    #print(np.hstack(([1], a)))
    #print(1 - a)
    #print(np.dot(m,b))
    #print(np.dot(d,1))
    #print(b[:, np.newaxis])
    #print(m[:, 1:])
    for _ in range(2000):
        m3 = np.dot(m1, m2)
    print(time.time() - start)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def timewaste():
    x = 1

main()