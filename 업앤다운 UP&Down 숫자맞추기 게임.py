# 컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
# 사용자는 이 숫자를 맞추어야 합니다.
# 입력한 숫자보다 정답이 크면 → "UP" 출력,
# 입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
# 정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.



import random

def guess_the_number():
    """
    숫자 맞추기 게임 함수
    """
    secret_number = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자 생성
    guess_count = 0  # 시도 횟수 초기화

    while True:
        try:
            guess = int(input("숫자를 입력하세요 (1~100): "))  # 사용자로부터 숫자 입력 받기
        except ValueError:
            print("잘못된 입력입니다. 1~100 사이의 정수를 입력하세요.")  # 숫자가 아닌 경우 예외 처리
            continue

        guess_count += 1  # 시도 횟수 증가

        if guess < secret_number:  # 입력한 숫자가 정답보다 작으면
            print("UP")  # "UP" 출력
        elif guess > secret_number:  # 입력한 숫자가 정답보다 크면
            print("DOWN")  # "DOWN" 출력
        else:
            print("정답")  # 정답을 맞추면 "정답" 출력
            print(f"총 {guess_count}번 만에 맞추셨습니다.")  # 시도 횟수 출력
            break  # 게임 종료

# 게임 실행
guess_the_number()