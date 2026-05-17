import numpy as np

scores = np.array([[85, 90, 88],
                   [78, 82, 80],
                   [92, 95, 90],
                   [70, 75, 72]])

print(scores.mean(axis=1))
print(scores.mean(axis=0))
print(np.max(scores))