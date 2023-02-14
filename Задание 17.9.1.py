def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def sort(nums_list):
    for i in range(len(nums_list)):
        for j in range(len(nums_list) - i - 1):
            if nums_list[j] > nums_list[j + 1]:
                nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]
    return nums_list


nums_list = input('Введите последовательность чисел через пробел: ').split()
num = int(input('Введите любое число: '))

nums_list = list(map(int, nums_list))

if num not in nums_list:
    nums_list.append(num)

nums_list_sort = sort(nums_list)

index_element = binary_search(nums_list_sort, num, 0, len(nums_list_sort) - 1) - 1

if num is nums_list_sort[-1] or num is nums_list_sort[0]:
    print('Число не соответствует заданному условию.')
else:
    print(f'Номер позиции элемента, который меньше введенного числа:', index_element)