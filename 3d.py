slice1 = [[1, 2], [3, 4]]
slice2 = [[5, 6], [7, 8]]
arr_3d = np.array([slice1, slice2])
arr_3d[0, 1, 0] = 99
new_slice = np.array([[9, 10], [11, 12]])
arr_3d = np.append(arr_3d, [new_slice], axis=0)
arr_3d = np.delete(arr_3d, 0, axis=0)