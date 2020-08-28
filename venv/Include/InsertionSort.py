"""
插入排序
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 测试数据
arr = [1, 243, 5, 4, 6, 34, 3, -2, -1, 4, 456, 34, 1, 45, 7, 78, 765, 856, 86, 56, 54]
insertionSort(arr)
print(arr)
