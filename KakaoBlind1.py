def decode(n, arr1, arr2):
    result = []
    for i in range(n):
        result.append(arr1[i] | arr2[i])

    print(result)

    result_str = []
    for num in result:
        s = ""
        check = 1 << n-1
        for _ in range(n):
            s += "#" if check & num else " "
            check = check >> 1
        result_str.append(s)

    print(result_str)

decode(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])