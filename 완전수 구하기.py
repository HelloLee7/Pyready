# 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다. 예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수

# 입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.



def is_perfect_number(n):
    """자연수 n이 완전수인지 판별하는 함수"""  # 함수 is_perfect_number 정의 시작, 자연수 n을 입력받아 완전수 여부를 판별
    약수_합 = 0  # 변수 약수_합 초기화, n의 약수들의 합을 저장
    for i in range(1, n):  # 1부터 n-1까지의 숫자를 순회 (n은 제외, 자기 자신은 약수에 포함하지 않음)
        if n % i == 0:  # 만약 i가 n의 약수라면 (나머지가 0이라면)
            약수_합 += i  # 약수_합에 i를 더함
    return 약수_합 == n  # 약수들의 합(약수_합)이 n과 같으면 True, 아니면 False를 반환 (완전수 판별)

def find_perfect_numbers(N):
    """N 이하의 모든 완전수를 찾는 함수"""  # 함수 find_perfect_numbers 정의 시작, 자연수 N을 입력받아 N 이하의 완전수를 찾음
    perfect_numbers = []  # 빈 리스트 perfect_numbers 생성, N 이하의 완전수들을 저장할 리스트
    for i in range(1, N + 1):  # 1부터 N까지의 숫자를 순회 (N 포함)
        if is_perfect_number(i):  # 만약 i가 완전수라면 (is_perfect_number 함수 호출 결과가 True라면)
            perfect_numbers.append(i)  # i를 perfect_numbers 리스트에 추가
    return perfect_numbers  # N 이하의 모든 완전수가 저장된 리스트 perfect_numbers 반환

# 사용자로부터 자연수 N을 입력받음
N = int(input("자연수 N을 입력하세요: "))  # 사용자로부터 입력을 받아 정수형으로 변환하여 N 변수에 저장

# N 이하의 모든 완전수를 찾아서 출력
perfect_numbers = find_perfect_numbers(N)  # find_perfect_numbers 함수를 호출하여 N 이하의 완전수 리스트를 구하고 perfect_numbers 변수에 저장
print(f"{N} 이하의 완전수: {perfect_numbers}")  # 결과 출력, N과 N 이하의 완전수 리스트를 출력