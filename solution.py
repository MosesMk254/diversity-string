def solution(N):
    if N <= 0:
        print (ValueError('N must be an integer'))
    
    letters_num = 26
    letters_count = N // letters_num
    remainder = N % letters_num
    
    result = []

    for i in range(letters_num):
        count = letters_count + 1 if i < remainder else letters_count
        result.append(chr(ord('a') + i) * count)

    return ''.join(result)
 
print(solution(3))
print(solution(5))
print(solution(0))
print(solution(10))
print(solution(1))
print(solution(15))