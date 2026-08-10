import numpy as np
# arr_1  = np.array([1,2,3,4])

# arr_2 =  np.array([
#     [50 ,60 ,70],
#     [80 , 90 , 100],
#     [40 ,45 ,50],
#     [30 ,35 ,40]
#  ])
# print (arr_2)
# print (arr_2.shape) # it give the size of array .
# print (arr_2.ndim) #it has give the dimension .


# list_1 = [10,20,30]
# arr_3 = np.array([10,20,30])

# print(list_1 * 2)
# print(arr_3 * 2)



# Let creat 1d ,2d ,3d array  :

# arr_1d = np.array([1,2,3,4])
# arr_2d = np.array([
#  [1,2],
# [3,4]
# # ])
# arr_3d = np.array([
#  [
#      [1,2],
#      [3,4]
#  ],
#  [
#      [5,6],
#      [7,8]
#  ],
#  ])
# print(arr_1d)
# print(arr_2d)
# print(arr_3d)



# Let's do the array attributes :


# arr_3d = np.array([
#  [
#      [1,2],
#      [3,4]
#  ],
#  [
#      [5,6],
#      [7,8]
#  ],
#  ])

# print(arr_3d.ndim)
# print(arr_3d.shape)
# print(arr_3d.dtype)
# print(arr_3d.itemsize)
# print(arr_3d.nbytes)


# print (np.zeros((2,3)))
# print(np.ones((2,3)))
# print(np.eye(3))
# print(np.zeros_like(arr_3d))
# print(np.ones_like(arr_3d))
# print(np.arange(1,11))
# print(np.arange(1,10,2))
# print(np.diag([10,20,30]))


# arr_2d = np.array([
#  [1,2],
#  [3,4]
#  ])
# print(arr_2d[1,0])
# print(arr_2d[::-1])


# arr_3d = np.array([
# [
# [1,2],
# [3,4]
# ],
# [
# [5,6],
# [7,8]
# ],
# ])

# print(arr_3d[0:1])
# print(arr_3d[:,0:1])
# print(arr_3d[0:1,1:2])

# arr_d = np.array([10.2,13.40,45.30])
# arr_c = arr_d.astype(int)
# print(arr_c)


# arr_d = np.array([102,1340,4530])
# arr_c = arr_d.astype(float)
# print(arr_c)

# arr_1 =np.arange(1,13)
# print(arr_1)

# arr_reshaped = arr_1.reshape(4,3)
# print(arr_reshaped)
# print(arr_reshaped.flatten())
# print(arr_reshaped.ravel())


# a = np.array([10,20,30,40,50])

# print(a+20)

# print(np.sum(a))
# print(np.mean(a))
# print(np.median(a))
# print(np.var(a))
# print(np.percentile(a ,75))
# print(a > 30)


a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [4,5],
    [6,7]
])

print(np.concatenate((a,b),axis = 1))

print(np.sum(a , axis = 1))

print("hstack:")
print(np.hstack((a,b)))

print("vstack:")
print(np.vstack((a,b)))

print("hsplit a:")
print(np.hsplit(a,2))

print("vsplit a:")
print(np.vsplit(a ,2))