import numpy as np

# X should be a matrix with N * k dimensions.
# y should be a vector with N dimensions.
# get a k dimensional vector.


def least_squares(x: list, y: list)->list:
    x = np.array(x)
    y = np.array(y)
    if np.linalg.det(np.dot(x.T, x)) == 0:
        return list(np.random.normal(loc=0, scale=0.01, size=(x.shape[1])))
    return list(np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y))


def gradient_descent(x: list, y: list, step: float)->list:
    x = np.array(x)
    y = np.array(y)
    w = np.zeros(x.shape[1])
    while True:
        loss = y - np.dot(x, w)
        grad = np.dot(x.T, loss)
        w += step * grad
        if np.sum(np.dot(grad.T, grad)) < 0.01:
            break
    return list(w)


def stochastic_gradient_descent(x: list, y: list, step: float)->list:
    x = np.array(x)
    y = np.array(y)
    w = np.zeros(x.shape[1])
    while True:
        for eachline in x:
            loss = y - np.dot(x, w)
            grad = np.dot(x.T, loss)
            w += step * grad
        if np.sum(np.dot(grad.T, grad)) < 0.01:
            break
    return list(w)





