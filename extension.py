import sys
import time
import numpy as np

prev = []
fatprime = 10**9 + 7


def matrixToPower(recursiveMatrix, n):
    if n > 1:
        M = [[3, 6, 7], [1, 0, 0], [0, 1, 0]]
        matrixToPower(recursiveMatrix, n // 2)
        multiply(recursiveMatrix, recursiveMatrix)
        if n % 2 != 0:
            multiply(recursiveMatrix, M)
    else:
        return


def multiply(m1, m2):
    mat1 = np.array(m1, dtype=object)
    mat2 = np.array(m2, dtype=object)
    k = mat1 @ mat2 % fatprime
    m1[0][0] = k[0, 0]
    m1[0][1] = k[0, 1]
    m1[0][2] = k[0, 2]
    m1[1][0] = k[1, 0]
    m1[1][1] = k[1, 1]
    m1[1][2] = k[1, 2]
    m1[2][0] = k[2, 0]
    m1[2][1] = k[2, 1]
    m1[2][2] = k[2, 2]


def matver(k):
    a2 = [7, 3, 1]
    if k < 4:
        return a2[3 - k]
    else:
        recursiveMatrix = [[3, 6, 7], [1, 0, 0], [0, 1, 0]]
        matrixToPower(recursiveMatrix, k - 3)
        m = np.array(recursiveMatrix, dtype=object) % fatprime
        base = np.array(a2, dtype=object) % fatprime
        return np.dot(m, base)[0]


if __name__ == "__main__":
    n = sys.stdin.readline()
    n = int(n)
    used = []

    s = time.time()
    c = matver(n) % fatprime
    e = time.time()
    print(c)
    print(e - s)
