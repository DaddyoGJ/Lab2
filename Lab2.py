import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    xlist = x.split(", ")
    intlist = list(map(int, xlist))
    return intlist

def calc_average():
    xinput = get_user_input()
    avg = sum(xinput)/len(xinput)
    print("Average: " + str(avg))

def find_min_max():
    xinput = get_user_input()
    min_value = min(xinput)
    max_value = max(xinput)
    minmaxlist = [min_value, max_value]
    print("[min_temp, max_temp]: " +str(minmaxlist))


def calc_median_temperature():
    xinput = get_user_input()
    xmedian = statistics.median(xinput)
    print(xmedian)