# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자. 출처

# 입력 - 화면에서 숫자로 된 문자열을 입력받는다.
# "4546793"
# 출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
# "454*67-9-3"

def dash_insert(s):
    """
    숫자로 구성된 문자열을 입력받아 홀수 연속 사이에는 '-', 짝수 연속 사이에는 '*'를 추가하는 함수
    """
    result = "" # 결과를 저장할 빈 문자열 초기화
    for i in range(len(s)): # 문자열의 길이만큼 반복
        result += s[i] # 현재 숫자를 결과 문자열에 추가
        if i < len(s) - 1: # 현재 숫자가 마지막 숫자가 아닌 경우
            current_num = int(s[i]) # 현재 숫자
            next_num = int(s[i+1]) # 다음 숫자
            if current_num % 2 == 1 and next_num % 2 == 1: # 현재 숫자와 다음 숫자가 모두 홀수인 경우
                result += "-" # 사이에 '-' 추가
            elif current_num % 2 == 0 and next_num % 2 == 0: # 현재 숫자와 다음 숫자가 모두 짝수인 경우
                result += "*" # 사이에 '*' 추가
    return result # 결과 문자열 반환

# 사용자로부터 숫자 문자열 입력 받기
num_string = input()

# dash_insert 함수 호출 및 결과 출력
result_string = dash_insert(num_string)
print(result_string)