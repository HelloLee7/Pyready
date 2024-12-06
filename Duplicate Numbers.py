# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789

# sample outputs: true false false true false


def check_unique_digits(input_string):
    """
    입력 문자열이 0~9까지의 숫자가 각각 한 번씩만 사용되었는지 확인하는 함수

    Args:
        input_string: 0~9 사이의 숫자로 이루어진 문자열

    Returns:
        유효성 여부 (True/False)
    """
    if len(input_string) != 10:  # 입력 문자열의 길이가 10이 아니면
        return False  # False 반환

    digit_counts = {}  # 각 숫자의 등장 횟수를 저장할 딕셔너리 초기화
    for digit in input_string:  # 입력 문자열의 각 문자에 대해
        if not digit.isdigit():  # 문자가 숫자가 아니면
            return False  # False 반환
        if digit in digit_counts:  # 이미 등장한 숫자이면
            return False  # False 반환
        digit_counts[digit] = 1  # 등장한 숫자를 딕셔너리에 추가하고 횟수 1로 설정

    for i in range(10):  # 0부터 9까지 숫자에 대해
        if str(i) not in digit_counts:  # 해당 숫자가 딕셔너리에 없으면 (등장하지 않았으면)
            return False  # False 반환

    return True  # 모든 조건을 만족하면 True 반환

# 샘플 입력 및 출력
sample_inputs = ["0123456789", "01234", "01234567890", "6789012345", "012322456789"]
for input_str in sample_inputs:
    result = check_unique_digits(input_str)
    print(f"{input_str}: {result}")