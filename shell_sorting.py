#2021741062 김현준

import random

def shell_sort(arr):
    gaps = [57, 23, 10, 4, 1]

    for gap in gaps:
        print(f"Interval: {gap}")
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        print(f"Array after interval {gap}: {arr}") # gap 에 따른 정렬 출력

    return arr

# 100개 숫자 랜덤 생성
numbers = [random.randint(1, 1000) for _ in range(100)]

# 정렬 이전 리스트 출력
print("Unsorted list:")
print(numbers)

# 정렬
sorted_numbers = shell_sort(numbers)

# 정렬된 리스트 출력
print("Sorted list:")
print(sorted_numbers)
