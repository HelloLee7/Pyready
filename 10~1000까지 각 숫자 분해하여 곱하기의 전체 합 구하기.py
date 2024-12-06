# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.

# 10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 15 = 1 * 5 = 5

# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

def sum_of_digit_products(start, end):
    """
    start부터 end까지 각 숫자의 자릿수를 분해하여 곱한 값들의 합을 구하는 함수

    Args:
        start: 시작 숫자
        end: 끝 숫자

    Returns:
        각 숫자 자릿수 곱의 합
    """
    total_sum = 0  # 합계를 저장할 변수 초기화
    for num in range(start, end + 1):  # start부터 end까지 반복
        product = 1  # 각 숫자의 자릿수 곱을 저장할 변수 초기화
        for digit in str(num):  # 숫자를 문자열로 변환하여 각 자릿수를 순회
            product *= int(digit)  # 자릿수를 정수로 변환하여 곱셈
        total_sum += product  # 각 숫자의 자릿수 곱을 합계에 더함
    return total_sum  # 합계 반환

# 예시
start = 10
end = 15
result = sum_of_digit_products(start, end)
print(f"{start}부터 {end}까지 각 숫자의 자릿수 곱의 합은 {result}입니다.")