# [3, 4, 5, 6, 7]
# = 홀수 3개, 짝수 2개
# [12, 16, 22, 24, 29]
# = 홀수 1개, 짝수 4개 
# [41, 43, 45, 47, 49]
# = 홀수 5개, 짝수 0개

# 홀수 : 2로 나누어 떨어지지 않는 정수
# 짝수 : 2로 나누어 떨어지는 정수


def count_odd_even():
    """
    사용자로부터 쉼표로 구분된 숫자들을 입력받아 홀수와 짝수의 개수를 세는 함수입니다.
    """
    while True:  # 무한 루프 시작: 'q'를 입력할 때까지 반복
        user_input = input("숫자들을 쉼표로 구분하여 입력하세요 (종료하려면 'q' 입력): ")  # 사용자로부터 숫자들을 쉼표로 구분하여 입력받음
        if user_input.lower() == 'q':  # 입력받은 문자열을 소문자로 변환하여 'q'와 비교 lower 는 모두 소문자행 시키는 것
            break  # 'q'이면 루프 종료

        try:
            numbers = [int(num.strip()) for num in user_input.split(',')]  # 쉼표로 분리된 문자열들을 정수 리스트로 변환
            # user_input.split(',') : 쉼표를 기준으로 문자열을 분리하여 리스트 생성
            # num.strip() : 각 문자열의 앞뒤 공백 제거
            # int() : 문자열을 정수로 변환
            # [ ... for num in ... ] : 리스트 컴프리헨션을 사용하여 각 숫자를 정수로 변환한 리스트 생성
        except ValueError:  # 정수로 변환할 수 없는 문자열이 있으면 ValueError 발생
            print("잘못된 입력입니다. 숫자와 쉼표를 올바르게 사용하거나 'q'를 입력하세요.")  # 오류 메시지 출력
            continue  # 루프의 처음으로 돌아가서 다시 입력받음

        odd_count = 0   # 홀수 개수를 저장할 변수 초기화
        even_count = 0  # 짝수 개수를 저장할 변수 초기화

        for number in numbers:  # 숫자 리스트의 각 숫자에 대해 반복
            if number % 2 == 0:  # 숫자를 2로 나눈 나머지가 0이면 짝수
                even_count += 1 # 짝수 개수 증가
            else:               # 나머지가 0이 아니면 홀수
                odd_count += 1  # 홀수 개수 증가

        print(f"입력한 숫자들: {numbers}")  # 입력받은 숫자 리스트 출력
        print(f"홀수 {odd_count}개, 짝수 {even_count}개") # 홀수와 짝수 개수 출력

# 함수 호출
count_odd_even()  # 함수 호출하여 실행 시작