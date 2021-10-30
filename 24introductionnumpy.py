import numpy as np


def intonumpy():
    a = np.arange(15).reshape(3,5) # we can think this like a matrix
    print(a)

    b = np.arange(10)
    print(b.shape)
    print(a.ndim) # dimension count of a

def numpyExample():
    countOfMatrix = input("Kaça kaç matris oluşturmak istersiniz(örn: '3,4'): ")

    m = int(countOfMatrix.split(",")[0])
    n = int(countOfMatrix.split(",")[1])
    myMatrix = np.arange(m*n).reshape(m,n)
    for i in range(m):
        for j in range(n):
            myMatrix[i][j] = int(input(f" {i+1}.satır {j+1}.sütun için değer giriniz: "))
    print(f"Oluşturduğunuz Matris : \n{myMatrix}")
numpyExample()