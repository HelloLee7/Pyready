# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다. 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다. 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

def is_palindrome(n):
    """
    숫자가 대칭수인지 확인하는 함수

    Args:
        n: 숫자

    Returns:
        대칭수이면 True, 아니면 False
    """
    return str(n) == str(n)[::-1]  # 숫자를 문자열로 변환하여 앞뒤를 비교

def largest_palindrome_product(digits):
    """
    주어진 자릿수의 두 숫자를 곱해 만들 수 있는 가장 큰 대칭수를 찾는 함수

    Args:
        digits: 자릿수

    Returns:
        가장 큰 대칭수
    """
    max_num = 10**digits - 1  # 주어진 자릿수의 최대값
    min_num = 10**(digits - 1)  # 주어진 자릿수의 최소값
    largest_palindrome = 0  # 가장 큰 대칭수를 저장할 변수 초기화

    for i in range(max_num, min_num - 1, -1):  # 큰 수부터 작은 수 순으로 반복
        for j in range(i, min_num - 1, -1):  # i부터 작은 수 순으로 반복
            product = i * j  # 두 수의 곱 계산
            if is_palindrome(product):  # 곱이 대칭수인지 확인
                largest_palindrome = max(largest_palindrome, product)  # 대칭수 중 최댓값 갱신
            if j * max_num < largest_palindrome:  # j가 더 작아져도 최대 대칭수보다 작아질 것이 확실하면 반복 중단
                break
    return largest_palindrome  # 가장 큰 대칭수 반환

# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수 찾기
result = largest_palindrome_product(3)
print(f"세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 {result}입니다.")