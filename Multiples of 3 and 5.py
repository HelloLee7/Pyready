# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.

# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.



def sum_of_multiples(limit):
  """1부터 limit 미만의 자연수 중 3 또는 5의 배수의 합을 구합니다."""
  total = 0
  for i in range(1, limit):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total

# 1000 미만의 자연수에서 3, 5의 배수의 합을 계산합니다.
result = sum_of_multiples(1000)
print(result)  # 출력: 233168