# создание и удаление каталогов
import os

def create_folders():
    for i in range(1,10):
        folder_name = (f'dir{i}')
        os.mkdir(folder_name)

def delete_folders():
    for i in range(1,10):
        folder_name = (f'dir{i}')
        os.rmdir(folder_name)


if __name__=='__main__':
    create_folders()
    delete_folders()

# выборка случаайного числа из масива
# import random
#
# def get_random(input_list):
#     if input_list:
#         result = random.choice(input_list)
#         return result
#
# print(get_random([2,5,6,6,8]))

# создать  main файл и с него запустить другие файлы с созданием и удалением директорий

