def fib(n):
    
    #p268 피보나치 수 동적프로그래밍2 알고리즘을 활용
    
    fib_list = [0] * (n+1)

    if n == 1 or n == 2:
        fib_list[n] = 1
        return 1

    else:
        fib_list[1] = 1
        fib_list[2] = 1
        for i in range(3, n+1):
            fib_list[i] = fib_list[i-1] + fib_list[i-2]
        return fib_list[n]


def matrix_path(n, matrix):
    
    #p274 페이지 알고리즘을 활용
    # 합을 저장하게 될 2차원 배열
    C = [[0]*n for i in range(n)]

   
    for i in range(n):
        C[i][0] = matrix[i][0]

    
    for j in range(1, n):
        C[0][j] = C[0][j-1] + matrix[0][j]

    
    for i in range(1, n):
        for j in range(1, n):
            C[i][j] = max(C[i-1][j], C[i][j-1]) + matrix[i][j]

    # 파이썬 인덱스 규칙 때문에 C[n][n]은 불가능함
    return C[n-1][n-1]
