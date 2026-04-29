import numpy as np
import pandas as pd

a = np.arange(1,15,3)
print(a)
arr_randoom= np.random.randint(1,11,50)
arr_reshape = arr_randoom.reshape(5,10)
print(arr_randoom)

x = np.array([1,3,4,5,6])
def test(x):
    if x >2:
        return True
    else:
        return False

# for i in x:
#     w = test(x = i)
#     print(w)
# print()
# vectorization
test_vectorizations = np.vectorize(test)
print(test_vectorizations(x))
