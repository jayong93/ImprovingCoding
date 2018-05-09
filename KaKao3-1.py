"""
계속 반복:
    n 진법으로 현재 숫자의 digit을 구한다.
    구한 digit을 list에 모은다.
    튜브가 말할 t개의 문자가 모이려면 몇개의 digit이 모여야 하는지 계산한다 -> m*(t-1)+p
    튜브가 말할 t개의 문자가 모이면 반복을 중지한다.

튜브가 말해야 하는 문자들을 모은다. -> 이 문자들은 i*m+p 마다 있다. i는 [0,t) 의 범위를 갖는다.
1 2 3 4 5
"""

def digit_to_char(digit):
    if digit >= 10:
        digit = chr(ord('A') - 10 + digit)
    else:
        digit = str(digit)
    return digit

def num_to_digits(num, n):
    if n == 10:
        return list(str(num))
    digits = []
    while num >= n:
        digit = digit_to_char(num%n)
        digits.append(digit)
        num = num//n

    digits.append(digit_to_char(num))
    return reversed(digits)

def get_my_digits(n, t, m, p):
    i = 0
    digits = []
    while True:
        digits_of_n = num_to_digits(i, n)
        digits += digits_of_n
        if len(digits) >= m*(t-1)+p:
            print(digits)
            break
        i += 1

    return ''.join([digits[j*m+(p-1)] for j in range(0, t)])

if __name__ == "__main__":
    inputs = [(2,4,2,1),(16,16,2,1),(16,16,2,2)]
    for n,t,m,p in inputs:
        my_digits = get_my_digits(n,t,m,p)
        print(my_digits)
