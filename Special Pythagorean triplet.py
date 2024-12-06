# 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ). 예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2 이므로 3, 4, 5는 피타고라스 수입니다.

# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
 
def find_pythagorean_triplet():
    """
    a + b + c = 1000 인 피타고라스 수 a, b, c를 찾아 a * b * c 값을 반환하는 함수
    """
    for a in range(1, 333):  # a는 1부터 333까지 (a < b < c 이므로 a는 최대 1000/3)
        for b in range(a + 1, 500):  # b는 a+1부터 500까지 (a < b 이므로 b는 a보다 커야하고, a+b+c=1000이므로 b는 최대 500)
            c = 1000 - a - b  # c는 1000 - a - b
            if c > b and a**2 + b**2 == c**2:  # c가 b보다 크고 피타고라스 정리를 만족하는 경우
                return a * b * c  # a * b * c 값 반환

# find_pythagorean_triplet 함수 호출 및 결과 출력
result = find_pythagorean_triplet()
print(result)