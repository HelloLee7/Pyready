# 현우는 축구를보다가 우리나라선수들의몸값을 알고싶었다

# 그래서 검색을해서 메모장에 적는데 키보드가 조그만하고 안좋은지라

# 자꾸 숫자가아닌 문자를 같이입력해버린다

# ex: xxx : 1627000000 > xxx : 1w627r00o00p00 만 (특수문자제외)

# 현우는 왜인지모르지만 뜻대로안되는것에

# 너무화가나서 자신이수량을입력하면 문자열만 딱빼서 숫자만 반환하는 코드를 만들고싶어한다

# 화가난 현우를위해 코드를 만들어보자!

def extract_number_from_string(input_string):
    """
    문자열에서 숫자 부분만 추출하여 정수로 변환하는 함수

    Args:
        input_string: 숫자가 포함된 문자열 (특수문자 제외)

    Returns:
        추출된 숫자를 정수로 변환한 값, 숫자가 없으면 None 반환
    """
    number_string = ""  # 숫자 부분을 저장할 문자열 초기화
    for char in input_string:  # 문자열의 각 문자에 대해
        if char.isdigit():  # 문자가 숫자인 경우
            number_string += char  # 숫자 문자열에 추가

    if number_string:  # 숫자 문자열이 비어있지 않으면 (숫자가 존재하면)
        return int(number_string)  # 숫자 문자열을 정수로 변환하여 반환
    else:  # 숫자가 없으면
        return None  # None 반환

# 사용자로부터 문자열 입력 받기
input_str = input("문자열을 입력하세요 (숫자 + 문자 혼합): ")

# 문자열에서 숫자 추출 및 정수 변환
extracted_number = extract_number_from_string(input_str)

# 결과 출력
if extracted_number is not None:
    print(f"추출된 숫자: {extracted_number}")
else:
    print("문자열에서 숫자를 찾을 수 없습니다.")