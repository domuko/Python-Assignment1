arr_2d = np.array([[1, 2], [3, 4]])
arr_2d[0, 1] = 9
arr_2d = np.vstack([arr_2d, [5, 6]])
arr_2d = np.delete(arr_2d, 1, axis=0)