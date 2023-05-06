print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    n = input("Please input a sequence of numbers with a comma between each number ")
    numbers = n.split(",")
    nums = [float(i) for i in numbers]
    return nums


def calc_average_temperature():

    avg = sum(numbers) / len(numbers)
    print("The average temperature is "+ str(avg))
    return avg

def calc_min_max_temperature():

    minmax = [min(numbers),max(numbers)]
    print("The minimum temperature is "+ str(minmax[0]))
    print("The maximum temperature is "+ str(minmax[1]))
    return minmax

def sort_temperature():
    x = numbers.sort(reverse=False)
    #Ascending order
    return x

def calc_median_temperature():
    # n = len(numbers)
    # sortedlist = sort_temperature()
    # y = (n-1) / 2
    # median = sortedlist[y]
    # print("Hi" + str(median))
    median = statistics.median(numbers)
    print(median)
    return median

numbers = [19.0,5.0,10.0,1.0,3.0]
#numbers = get_user_input()

calc_median_temperature()