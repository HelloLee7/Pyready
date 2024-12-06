# n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.

# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.

# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.
# 파이썬으로 작성하고 주석으로 한줄씩 설명해줘
 

def special_sort(arr):
    """
    음수와 양수를 분리하여 정렬하되, 순서를 유지하는 함수

    Args:
        arr: 정수 배열

    Returns:
        정렬된 배열
    """
    negatives = []  # 음수를 저장할 리스트
    positives = []  # 양수를 저장할 리스트

    for num in arr:  # 배열을 순회하면서
        if num < 0:  # 음수이면
            negatives.append(num)  # 음수 리스트에 추가
        else:  # 양수이면
            positives.append(num)  # 양수 리스트에 추가

    return negatives + positives  # 음수 리스트와 양수 리스트를 합쳐서 반환

# 예시
arr = [-1, 1, 3, -2, 2]
sorted_arr = special_sort(arr)
print(sorted_arr)  # 출력: [-1, -2, 1, 3, 2]