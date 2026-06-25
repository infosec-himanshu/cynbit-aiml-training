import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:")
print(array_1d)
print("\n2D Array:")
print(array_2d)

print("\n--- Basic Operations ---")
print("Addition (add 5):", array_1d + 5)
print("Subtraction (sub 2):", array_1d - 2)
print("Multiplication (mul 3):", array_1d * 3)

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("\nArray Element-wise Addition:", array_a + array_b)
print("Array Element-wise Multiplication:", array_a * array_b)

print("\n--- Statistical Operations ---")
print("Sum:", array_1d.sum())
print("Mean (Average):", array_1d.mean())
print("Maximum Value:", array_1d.max())