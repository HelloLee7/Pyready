# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

# 00:00 (60초간 표시됨)
# 00:01 
# 00:02 
# ...
# 23:59

def count_seconds_with_3():
    """
    하루 동안 디지털 시계에 3이 표시되는 시간을 초로 환산하여 계산하는 함수

    Returns:
        3이 표시되는 총 시간 (초)
    """
    total_seconds = 0  # 총 시간을 저장할 변수 초기화
    for hour in range(24):  # 0시부터 23시까지 반복
        for minute in range(60):  # 0분부터 59분까지 반복
            hour_str = str(hour).zfill(2)  # 시간을 두 자리 문자열로 변환 (예: 3 -> 03)
            minute_str = str(minute).zfill(2)  # 분을 두 자리 문자열로 변환 (예: 5 -> 05)
            time_str = hour_str + minute_str  # 시간과 분을 합쳐서 문자열 생성 (예: 0305)
            if '3' in time_str:  # 문자열에 '3'이 포함되어 있는지 확인
                total_seconds += 60  # 3이 포함된 시간이면 60초를 더함
    return total_seconds  # 총 시간 반환

# 결과 출력
seconds = count_seconds_with_3()
print(f"하루 동안 디지털 시계에 3이 표시되는 시간은 총 {seconds}초 입니다.")