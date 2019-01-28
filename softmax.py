# name : MOQORU(Youngjune Seo)
# date : 2019-01-28

import numpy as np

def softmax(a) : # can be used as probability
    c = np.max(a) # avoid overflow (ex : e^1000 => nearly infinite)
    exp_a = np.exp(a - c) # this data isn't zero, because e^(max - max) = 1
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

abig = np.array( [1010, 1000, 990] )
ybig = softmax(abig)

print("Bigger data error :", np.exp(abig) / np.sum(np.exp(a)))
print("Bigger data fixed :", abig, ybig, np.sum(ybig)) # sum is 1, so may think as '~~%'
