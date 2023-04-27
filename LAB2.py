print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    n = input("Please input a sequence of numbers with a comma between each number ")
    numbers = n.split(",")
    nums = [float(i) for i in numbers]
    return nums



def calc_average_temperature():

    numbers = get_user_input()
    avg = sum(numbers) / len(numbers)
    print("The average temperature is "+ str(avg))
    return avg

def calc_min_max_temperature():
    numbers = get_user_input()
    minmax = [min(numbers),max(numbers)]
    print("The minimum temperature is "+ str(minmax[0]))
    print("The maximum temperature is "+ str(minmax[1]))
    return minmax

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")


calc_min_max_temperature()