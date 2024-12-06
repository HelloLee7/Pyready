# input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.

# 입력 예시: 6

# 출력 예시:

# OOOOOX

# OOOOXX

# OOOXXX

# OOXXXX

# OXXXXX

# XXXXXX

def print_pattern(n):
    """
    입력된 숫자 n에 따라 특정 패턴을 출력하는 함수

    Args:
        n: 출력할 패턴의 행 수
    """
    for i in range(1, n + 1):  # 1부터 n까지 반복 (각 행을 나타냄)
        o_count = n - i  # 현재 행에서 'O'의 개수 계산
        x_count = i  # 현재 행에서 'X'의 개수 계산
        print('O' * o_count + 'X' * x_count)  # 'O'와 'X'를 개수에 맞게 출력

# 입력 예시
n = 6
print_pattern(n)