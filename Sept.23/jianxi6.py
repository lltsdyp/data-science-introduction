import random
import time

# 选择排序函数
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 生成随机数组
def generate_random_array():
    length = random.randint(50, 12306)
    return ([random.randint(1, 1000) for _ in range(length)],length)


for _ in range(42):
    (arr,length) = generate_random_array()
    
    start_time = time.time()  # 记录开始时间
    selection_sort(arr)       # 排序
    end_time = time.time()    # 记录结束时间
    
    elapsed_time = end_time - start_time
    print(f"Array length: {length}, Execution time: {elapsed_time:.6f} seconds")