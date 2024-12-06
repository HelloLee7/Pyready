# 프로그램 실행 순서

# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.
# 요구사항

# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다.

def calculate_sum_and_average():
    """
    정수의 개수를 입력받아 합계와 평균을 계산하는 함수
    """
    try:
        count = int(input("입력할 정수의 개수를 입력하세요: "))  # 입력할 정수의 개수 입력받기
        if count <= 0:  # 입력된 정수의 개수가 0 이하일 경우
            print("1 이상의 정수를 입력하세요.")  # 오류 메시지 출력
            return

        total_sum = 0  # 합계를 저장할 변수 초기화
        for _ in range(count):  # 입력받은 정수의 개수만큼 반복
            while True:  # 올바른 정수가 입력될 때까지 반복
                try:
                    num = int(input("정수를 입력하세요: "))  # 정수 입력받기
                    total_sum += num  # 입력받은 정수를 합계에 더하기
                    break  # 정수가 입력되면 반복 종료
                except ValueError:
                    print("잘못된 입력입니다. 정수를 입력하세요.")  # 잘못된 입력일 경우 오류 메시지 출력

        average = total_sum / count  # 평균 계산

        print(f"입력받은 정수의 합: {total_sum}")  # 합계 출력
        print(f"입력받은 정수의 평균: {average}")  # 평균 출력

    except ValueError:  # 입력받은 정수의 개수가 정수가 아닌 경우
        print("잘못된 입력입니다. 정수를 입력하세요.")  # 오류 메시지 출력

    finally:
        # 메모리 공간을 비우는 작업은 파이썬에서 자동으로 처리되므로 별도의 코드가 필요 없음
        pass

# 함수 호출하여 프로그램 실행
calculate_sum_and_average()