# 숫자를 입력받으면 그에해당하는 자릿수를 출력하는 코드를 작성하라.

# 입력 : 156 출력 : 100의자리수

# 입력 : 18961 출력 : 10000의자릿수

def get_place_value(number):
  """
  숫자를 입력받아 해당 숫자의 자릿수를 문자열로 반환하는 함수

  Args:
    number: 양의 정수

  Returns:
    자릿수 문자열 (예: "100의 자리수", "10000의 자리수")
    입력이 0 또는 음수일 경우 "잘못된 입력입니다." 반환
  """
  if number <= 0:
    return "잘못된 입력입니다."

  num_str = str(number)  # 숫자를 문자열로 변환
  num_length = len(num_str)  # 숫자의 길이 계산
  place_value = 10**(num_length - 1)  # 자릿수 계산 (10의 (길이-1) 제곱)

  return f"{place_value}의 자리수"

# 사용자 입력 받기
num = int(input("숫자를 입력하세요: "))

# 자릿수 출력
place_value_str = get_place_value(num)
print(f"입력: {num} 출력: {place_value_str}")