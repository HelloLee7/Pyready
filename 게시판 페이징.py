# A씨는 게시판 프로그램을 작성하고 있다.

# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수

# A씨가 필요한 프로그램을 작성하시오.

# 예) 프로그램 수행 시 다음과 같은 결과값이 나와야 함.

# m	n	출력
# 0	1	0
# 1	1	1
# 2	1	2
# 1	10	1
# 10	10	1
# 11	10	2




def calculate_total_pages(m, n):
    """
    총 게시물 수와 한 페이지에 보여줄 게시물 수를 입력받아 총 페이지 수를 계산하는 함수

    Args:
        m (int): 총 게시물 수
        n (int): 한 페이지에 보여줄 게시물 수 (n >= 1)

    Returns:
        int: 총 페이지 수
    """
    if m == 0:  # 총 게시물 수가 0이면 0 페이지 반환
        return 0
    elif m % n == 0:  # 총 게시물 수가 한 페이지에 보여줄 게시물 수로 나누어 떨어지면 몫을 반환
        return m // n
    else:  # 총 게시물 수가 한 페이지에 보여줄 게시물 수로 나누어 떨어지지 않으면 몫에 1을 더하여 반환
        return m // n + 1

# 입력 예시
m1, n1 = 0, 1
m2, n2 = 1, 1
m3, n3 = 2, 1
m4, n4 = 1, 10
m5, n5 = 10, 10
m6, n6 = 11, 10

# 함수 호출 및 결과 출력
print(f"m: {m1}, n: {n1}, 출력: {calculate_total_pages(m1, n1)}")  # m: 0, n: 1, 출력: 0
print(f"m: {m2}, n: {n2}, 출력: {calculate_total_pages(m2, n2)}")  # m: 1, n: 1, 출력: 1
print(f"m: {m3}, n: {n3}, 출력: {calculate_total_pages(m3, n3)}")  # m: 2, n: 1, 출력: 2
print(f"m: {m4}, n: {n4}, 출력: {calculate_total_pages(m4, n4)}")  # m: 1, n: 10, 출력: 1
print(f"m: {m5}, n: {n5}, 출력: {calculate_total_pages(m5, n5)}")  # m: 10, n: 10, 출력: 1
print(f"m: {m6}, n: {n6}, 출력: {calculate_total_pages(m6, n6)}")  # m: 11, n: 10, 출력: 2