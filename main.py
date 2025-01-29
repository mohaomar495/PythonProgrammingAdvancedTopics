import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	y = np.array(y)
	theta = np.linalg.inv(X.T @ X) @ X.T @ y
	return np.abs(theta.round())


X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X, y))
