def binarySearch(arr, start, end, targetElement):
    print(start, "---", end)
    if end >= start:
        middle = int((start + end) / 2)
        # 如果元素正好处于中间元素
        if arr[middle] == targetElement:
            return middle
        # 目标元素在中间元素的右面
        elif arr[middle] < targetElement:
            return binarySearch(arr, middle + 1, end, targetElement)
        # 目标元素在中间元素的左面
        else:
            return binarySearch(arr, start, middle - 1, targetElement)
    else:
        # 不存在
        return -1


# 创建测试数据
arr = [1, 3, 24, 35, 42, 56, 64, 73, 77, 100]
while True:
    targetElement = input("输入目标元素：")

    result = binarySearch(arr, 0, len(arr) - 1, int(targetElement))
    if result == -1:
        print("元素不存在")
    else:
        print("元素所在索引：", result)
