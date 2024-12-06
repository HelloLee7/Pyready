# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5

# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개


def count_digits(start, end):
    """start부터 end까지 각 숫자의 개수를 세는 함수"""
    digit_counts = {i: 0 for i in range(10)}  # 0부터 9까지 각 숫자의 개수를 저장할 딕셔너리 초기화,  예: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(start, end + 1):  # start부터 end까지(포함)의 숫자를 순회합니다. 예: start가 1이고 end가 3이면 1, 2, 3을 순회
        for digit in str(num):  # 각 숫자를 문자열로 변환하고, 그 문자열의 각 자리수를 순회합니다. 예: num이 12이면 '1', '2'를 순회
            digit_counts[int(digit)] += 1  # 각 자리수를 정수로 변환하고, digit_counts 딕셔너리에서 해당 숫자의 개수를 1 증가시킵니다. 예: digit이 '1'이면 digit_counts[1]의 값을 1 증가

    return digit_counts  # 각 숫자의 개수가 저장된 딕셔너리를 반환합니다. 예: {0: 192, 1: 301, 2: 300, 3: 300, 4: 300, 5: 300, 6: 300, 7: 300, 8: 300, 9: 300}

# 1부터 1000까지 각 숫자의 개수 계산
result = count_digits(1, 1000)  # count_digits 함수를 호출하여 1부터 1000까지 각 숫자의 개수를 계산하고, 그 결과를 result 변수에 저장

# 결과 출력
for digit, count in result.items():  # result 딕셔너리의 각 키(digit)와 값(count)을 순회합니다.
    print(f"{digit}: {count}개")  # 각 숫자와 그 숫자의 개수를 출력합니다. 예: 0: 192개