import sys
import time
import numpy as np

prev = []
fatprime = 10**9 + 7


def matrixToPower(recursiveMatrix, n):
    if n > 1:
        M = [[1, 1], [1, 0]]
        matrixToPower(recursiveMatrix, n // 2)
        multiply(recursiveMatrix, recursiveMatrix)
        if n % 2 != 0:
            multiply(recursiveMatrix, M)
    else:
        return


def multiply(m1, m2):
    x00 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % fatprime
    x01 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % fatprime
    x10 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % fatprime
    x11 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % fatprime

    m1[0][0] = x00
    m1[0][1] = x01
    m1[1][0] = x10
    m1[1][1] = x11


def count(k, used):
    l = used.copy()
    r = used.copy()
    if k == 0:
        return 1
    elif len(used) > 1:
        if (used[len(used) - 1] == 0) == (used[len(used) - 2] == 0):
            r.append(0)
            l.append(1)
            return count(k - 1, r) + count(k - 1, l)
        else:
            r.append(used[len(used) - 1])
            return count(k - 1, r)
    else:
        r.append(0)
        l.append(1)
        return count(k - 1, l) + count(k - 1, r)


def rec(k):
    if k == 1:
        return 2
    elif k == 2:
        return 4
    else:
        return rec(k - 1) + rec(k - 2)


def recwithstorage(k):
    if k == 1:
        return 2
    if k == 2:
        return 4

    if prev[k] != 0:
        return prev[k]
    else:
        # r1 = recwithstorage(k-1)
        # prev[k-1] = r1 % fatprime
        r2 = recwithstorage(k - 2)
        prev[k - 2] = r2 % fatprime
        return recwithstorage(k - 1) + r2 % fatprime


def recop(k):
    a1 = 2
    a2 = 4
    if k == 1:
        return a1
    if k == 2:
        return a2
    else:
        for i in range(3, k + 1):
            ak = a1 + a2 % fatprime
            a1 = a2
            a2 = ak
        return a2


def matver(k):
    a2 = [4, 2]
    if k == 1:
        return a2[1]
    elif k == 2:
        return a2[0]
    else:
        recursiveMatrix = [[1, 1], [1, 0]]
        matrixToPower(recursiveMatrix, k - 2)
        m = np.array(recursiveMatrix, dtype=object).reshape(2, 2) % fatprime
        a2 = np.array([4, 2], dtype=object) % fatprime
        return np.dot(m, a2)[0]


if __name__ == "__main__":
    n = sys.stdin.readline()
    n = int(n)
    used = []

    if n < 33:
        s = time.time()
        c = count(n, used)
        e = time.time()
        print(c)
        print(e - s)

    if n < 38:
        s = time.time()
        c = rec(n)
        e = time.time()
        print(c)
        print(e - s)

    if n < 5980:
        sys.setrecursionlimit(10**9)
        prev = [0] * (n + 1)
        s = time.time()
        c = recwithstorage(n) % fatprime
        e = time.time()
        print(c)
        print(e - s)

    if n < 100000000:
        s = time.time()
        c = recop(n) % fatprime
        e = time.time()
        print(c)
        print(e - s)

    s = time.time()
    c = matver(n) % fatprime
    e = time.time()
    print(c)
    print(e - s)
