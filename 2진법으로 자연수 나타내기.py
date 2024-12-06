# 2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다. 예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 1001001으로 표현한다. 어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.

def decimal_to_binary(decimal_num):
    """
    10진수를 2진수로 변환하는 함수

    Args:
        decimal_num: 10진수 숫자

    Returns:
        2진수 문자열
    """
    if decimal_num == 0:  # 입력 숫자가 0이면
        return "0"  # 바로 "0" 반환

    binary_string = ""  # 2진수 문자열을 저장할 변수 초기화
    while decimal_num > 0:  # 입력 숫자가 0보다 클 동안 반복
        remainder = decimal_num % 2  # 2로 나눈 나머지를 구함 (0 또는 1)
        binary_string = str(remainder) + binary_string  # 나머지를 문자열 앞에 추가
        decimal_num //= 2  # 입력 숫자를 2로 나눔 (몫)

    return binary_string  # 2진수 문자열 반환

# 사용자로부터 숫자 입력 받기
decimal_input = int(input("10진수 숫자를 입력하세요: "))

# 10진수를 2진수로 변환하여 출력
binary_output = decimal_to_binary(decimal_input)
print(f"2진수 변환 결과: {binary_output}")