from Apriori import Apriori
import tools
import numpy as np

model = Apriori()

data = np.array([
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]])


model.train(data=data)

print(model.k_frequent_sets_list)

data2 = np.array([
    [1.1, 0.3, 0.7, 1.1],
    [1.0, 0.2, 0.3, 0.1],
    [0.9, 0.8, 1.7, 1.3],
    [0.0, 0.0, 1.0, 1.0],
    [1.2, 1.2, 1.1, 1.5],
    [0.4, 0.4, 0.6, 0.6]])

y2 = [2, 1, 0.8, 0.2, 1.7, 1.3]

print(tools.least_squares(data2, y2))

print(tools.gradient_descent(data2, y2, 0.01))

print(tools.stochastic_gradient_descent(data2, y2, 0.01))
