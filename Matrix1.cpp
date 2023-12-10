def print_matrix(matrix):
   for i in range(len(matrix)):
     for j in range(len(matrix[0])):
       print("\t", matrix[i][j], end=" ")
     print("\n")
def init_matrix(matrix, m, n):
   matrix = [[0 for j in range(0, n)]for i in range(0, m)]
   return matrix
def read_matrix():
 mat = []
 r = int(input("Enter number of rows in First Matrix: "))
 c = int(input("Enter number of columns in First Matrix : "))
 mat = init_matrix(mat, r, c) 
 for i in range(0, r):
   for j in range(0, c):
     mat[i][j] = int(input("Enter an element : "))
 return mat, r, c
def mat_add(m1, m2, res, m, n):
  for i in range(0, m):
    for j in range(0, n):
      res[i][j] = m1[i][j] + m2[i][j]
  return res
def mat_sub(m1, m2, res, m, n):
  for i in range(0, m):
    for j in range(0, n):
     res[i][j] = m1[i][j] - m2[i][j]
  return res
def mat_mul(m1, m2, res, r1, c1, c2):
  for i in range(0, r1):
   for k in range(0, c2):
       for j in range(0, c1):
        res[i][k] += m1[i][j] * m2[j][k]
  return res
def trans_mat(m1, res, r1, c1):
  for i in range(0, r1):
   for j in range(0, c1):
     res[j][i] = m1[i][j]
  return res
matrix1 = []
matrix2 = []
res_matrix = []
print(" First Matrix : ")
matrix1, r1, c1 = read_matrix()
print(" Second Matrix : ")
matrix2, r2, c2 = read_matrix()
res_matrix = init_matrix(res_matrix, r1, c2) 
print(" matrix 1")
print_matrix(matrix1)
print(" matrix 2")
print_matrix(matrix2)
flag = 1
while flag==1:
  print("/*********MENU********/ \n")
  print(" 1. Addition of two matrices ")
  print(" 2. Subtraction of two matrices ")
  print(" 3. Multiplication of two matrices ")
  print(" 4. Transpose of a matrix ")
  choice = int(input("Enter Your Choice : "))
  if choice == 1:
    if r1 == r2 and c1 == c2:
      print("resultant matrix after addition")
      res_matrix = mat_add(matrix1, matrix2, res_matrix, r1, c1)
      print_matrix(res_matrix)
    else:
      print("Addition can't be performed ")
  elif choice == 2:
     if r1 == r2 and c1 == c2:
       print("resultant matrix after subtraction")
       res_matrix = mat_sub(matrix1, matrix2, res_matrix, r1, c1)
       print_matrix(res_matrix)
     else:
       print("Subtraction can't be performed ")
  elif choice == 3:
   if c1 == r2:
     print("resultant matrix after Multiplication ")
     res_matrix = mat_mul(matrix1, matrix2, res_matrix, r1, c1, c2)
     print_matrix(res_matrix)
   else:
     print("Multiplication can't be performed ")
  elif choice == 4:
     print("Transpose of First Matrix is ")
     res_matrix1 = []
     res_matrix1 = init_matrix(res_matrix1, c1, r1)
     res_matrix = trans_mat(matrix1, res_matrix1, r1, c1)
     print_matrix(res_matrix)

  else:
    print(" Wrong choice ")

  flag=int(input("Do You Want to Continue ? [ No=0 and yes=1] : "))
