# выборка случаайного числа из масива
import random

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result

if __name__=='__main__':
    print(get_random([2,5,6,6,8]))