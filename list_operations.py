def replace_element(list, k, m):
    "Заменяет все элементы в списке lst, равные k, на значение m."

    for i in range(len(list)):
        if list[i] == k:
            list[i] = m
    return list


from list_operations import replace_element

# Заданный список
N = [1, 2, 3, 4, 5, 2, 6, 2]

# Значения для замены
K = 2
M = 8

print("Исходный список N:", N)

# Замена значений элементов списка
new_list = replace_element(N, K, M)
print(f"Список после замены элементов со значением {K} на {M}: {new_list}")

