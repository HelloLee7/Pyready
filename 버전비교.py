# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.

# 버전은 다음처럼 "." 으로 구분된 문자열이다.

# 버전 예) 1.0.0, 1.0.23, 1.1

# 두 개의 버전을 비교하는 프로그램을 작성하시오.

# 다음은 버전 비교의 예이다.

# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1




def compare_versions(version1, version2):
    """
    두 버전 문자열을 비교하여 결과를 반환하는 함수

    Args:
        version1 (str): 첫 번째 버전 문자열 (예: "1.2.3")
        version2 (str): 두 번째 버전 문자열 (예: "1.2.4")

    Returns:
        int: version1 > version2 이면 1, version1 < version2 이면 -1, 같으면 0
    """

    def parse_version(version_str):
        """
        버전 문자열을 정수 리스트로 파싱하는 함수

        Args:
            version_str (str): 버전 문자열 (예: "1.2.3")

        Returns:
            list: 정수로 파싱된 버전 리스트 (예: [1, 2, 3])
        """
        return [int(part) for part in version_str.split(".")]  # "."으로 문자열을 나누고 각 부분을 정수로 변환하여 리스트 생성

    v1_parts = parse_version(version1)  # 첫 번째 버전 문자열을 파싱
    v2_parts = parse_version(version2)  # 두 번째 버전 문자열을 파싱

    # 두 버전 리스트의 길이를 맞추기 위해 짧은 쪽에 0을 추가
    max_length = max(len(v1_parts), len(v2_parts))  # 두 리스트 중 긴 길이 계산
    v1_parts += [0] * (max_length - len(v1_parts))  # 짧은 리스트에 0을 추가하여 길이 맞춤
    v2_parts += [0] * (max_length - len(v2_parts))  # 짧은 리스트에 0을 추가하여 길이 맞춤

    # 각 부분을 비교하여 버전 비교 결과 반환
    for i in range(max_length):
        if v1_parts[i] > v2_parts[i]:  # 첫 번째 버전의 i번째 부분이 두 번째 버전의 i번째 부분보다 크면
            return 1  # 1 반환 (version1 > version2)
        elif v1_parts[i] < v2_parts[i]:  # 첫 번째 버전의 i번째 부분이 두 번째 버전의 i번째 부분보다 작으면
            return -1  # -1 반환 (version1 < version2)

    return 0  # 모든 부분이 같으면 0 반환 (version1 == version2)

# 테스트 예시
print(compare_versions("0.0.2", "0.0.1"))  # 1 (0.0.2 > 0.0.1)
print(compare_versions("1.0.10", "1.0.3"))  # 1 (1.0.10 > 1.0.3)
print(compare_versions("1.2.0", "1.1.99"))  # 1 (1.2.0 > 1.1.99)
print(compare_versions("1.1", "1.0.1"))  # 1 (1.1 > 1.0.1)
print(compare_versions("1.0.0", "1.0.0"))  # 0 (1.0.0 == 1.0.0)
print(compare_versions("1.0", "1.0.1"))  # -1 (1.0 < 1.0.1)