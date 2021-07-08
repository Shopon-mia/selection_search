# Number : 01
# def selection_sort(data_list):
#     length = len(data_list)

#     for i in range(length - 1):
#         min_index = i
#         for j in range(i+1, length):
#             if data_list[j] < data_list[min_index]:
#                 min_index = j


#         if min_index != i:
#             temp = data_list[i]
#             data_list[i] = data_list[min_index]
#             data_list[min_index] = temp


# if __name__ == '__main__':
#     data_list = [80, 50, 40, 10, 15, 30]
#     selection_sort(data_list)
#     print("Sorted List : ", data_list)

# Number : 02
# def selection_sort(data_list):
#     length = len(data_list)

#     for i in range(length - 1):
#         min_index = i
#         for j in range(i+1, length):
#             if data_list[j] < data_list[min_index]:
#                 min_index = j


#         if min_index != i:
#             temp = data_list[i]
#             data_list[i] = data_list[min_index]
#             data_list[min_index] = temp


# if __name__ == '__main__':
#     data_list = [20, 70, 90, 25, 15, 35]
#     selection_sort(data_list)
#     print("Sorted List : ", data_list)


# Number : 03
# def selection_sort(data_list):
#     length = len(data_list)

#     for i in range(length - 1):
#         min_index = i
#         for j in range(i+1, length):
#             if data_list[j] < data_list[min_index]:
#                 min_index = j


#         if min_index != i:
#             temp = data_list[i]
#             data_list[i] = data_list[min_index]
#             data_list[min_index] = temp


# if __name__ == '__main__':
#     data_list = [5, 20, 40, 80, 35, 28]
#     selection_sort(data_list)
#     print("Sorted List : ", data_list)


# Number : 04
# def selection_sort(data_list):
#     length = len(data_list)

#     for i in range(length - 1):
#         min_index = i
#         for j in range(i+1, length):
#             if data_list[j] < data_list[min_index]:
#                 min_index = j


#         if min_index != i:
#             temp = data_list[i]
#             data_list[i] = data_list[min_index]
#             data_list[min_index] = temp


# if __name__ == '__main__':
#     data_list = [35, 10, 78, 82, 95, 12]
#     selection_sort(data_list)
#     print("Sorted List : ", data_list)



# Number : 05
def selection_sort(data_list):
    length = len(data_list)

    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if data_list[j] < data_list[min_index]:
                min_index = j


        if min_index != i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp


if __name__ == '__main__':
    data_list = [15, 60, 30, 90, 25, 50]
    selection_sort(data_list)
    print("Sorted List : ", data_list)