# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

def sum_even_fibonacci(limit):
    """
    피보나치 수열에서 짝수이면서 limit 이하인 항들의 합을 구하는 함수
    """
    a, b = 1, 2 # 피보나치 수열의 첫 두 항 초기화
    total_sum = 0 # 짝수 항들의 합을 저장할 변수 초기화
    while b <= limit: # b가 limit 이하인 동안 반복
        if b % 2 == 0: # b가 짝수인 경우
            total_sum += b # 짝수 항을 합에 더하기
        a, b = b, a + b # 다음 피보나치 항 계산
    return total_sum # 짝수 항들의 합 반환

# limit 값을 4백만으로 설정
limit_value = 4000000

# sum_even_fibonacci 함수 호출 및 결과 출력
result = sum_even_fibonacci(limit_value)
print(result)