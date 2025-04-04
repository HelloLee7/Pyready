# A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다. A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.

# A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.

def convert_tabs_to_spaces(code):
    """
    소스코드 내의 탭 문자를 공백 4개로 변환하는 함수

    Args:
        code: 소스코드 문자열

    Returns:
        탭이 공백 4개로 변환된 소스코드 문자열
    """
    converted_code = code.replace('\t', '    ')  # 탭 문자를 공백 4개로 변환
    return converted_code  # 변환된 코드 반환

# 예시
code = """
def my_function():
\tif x > 0:
\t\tprint("Positive")
\telse:
\t    print("Non-positive")
"""

converted_code = convert_tabs_to_spaces(code)
print(converted_code)
