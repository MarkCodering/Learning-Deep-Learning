import numpy as np
import random

from torch import le

def show_learning(w):
    print("w0 = %f, w1 = %f, w2 = %f" % (w[0], w[1], w[2]))

def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += w[i] * x[i]
        if z < 0:
            return -1
        else:
            return 1

random.seed(7)
LEARNING_RATE = 0.1
index_list = [0,1,2,3]

x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
y_train = [1.0, 1.0, 1.0, -1.0]

weight = [0.2, -0.6, 0.25]
#training loop
all_correct = False
while not all_correct:
    all_correct = True
    random.shuffle(index_list)
    for i in index_list:
        x = x_train[i]
        y = y_train[i]
        output = compute_output(weight, x)

        if output != y:
            for j in range(0, len(weight)):
                weight[j] =+ (LEARNING_RATE * y * x[j])
            all_correct = False
            show_learning(weight)