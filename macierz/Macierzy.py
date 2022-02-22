import numpy as np

A1 = np.array([[2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553],
               [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556],
               [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749],
               [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493],
               [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926]])

A2 = np.array([[2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473],
               [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589],
               [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923],
               [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124],
               [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678]])

b_transpose = np.expand_dims(np.array([5.40780228, 3.67008677, 3.12306266, -1.11187948, 0.54437218]), axis=1)
vector_transpose = np.expand_dims(np.array([1e-5, 0, 0, 0, 0]), axis=1)
b_prim = b_transpose + vector_transpose

y1 = np.linalg.solve(A1, b_transpose)
y2 = np.linalg.solve(A2, b_transpose)
print("A1y1 = b: \n", y1)
print("A2y2 = b: \n", y2)

y1_prim = np.linalg.solve(A1, b_prim)
y2_prim = np.linalg.solve(A2, b_prim)

print("A1y' = b': \n", y1_prim)
print("A2y' = b': \n", y2_prim)

delta1 = np.linalg.norm(y1 - y1_prim, ord=2)
delta2 = np.linalg.norm(y2 - y2_prim, ord=2)
print("delta1 = ", delta1)
print("delta2 = ", delta2)
