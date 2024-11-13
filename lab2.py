def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Splitting: " + str(num_list)) #cant print float so had to change temp into string
    num_sorted = sort_temperature(num_list)
    print("Sorted List: " + str(num_sorted))
    num_average = calc_average(num_list)
    print("Avg Calc: " + str(num_average)) 
    find_min_max(num_list)
    num_median = calc_median_temperature(num_list)
    print("Median: " + str(num_median))

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    inputstr = input("Enter the numbers: ")
    #split the input string in to segments of strings using commas as splitter
    splitlist = inputstr.split(", ")
    #convert each short string in list to float
    floatlist = [] #defines an empty list of float numbers
    for x in splitlist:
        floatnum = float(x) #convert string into float
        floatlist.append(floatnum) #add the float number to float list
    return floatlist

def calc_average(num_list):
    total = sum(num_list)
    n = len(num_list)
    avg = (total/n)
    return avg  

def find_min_max(num_list):
    sort_temperature(num_list)
    min = num_list[0]
    print("Min: " + str(min))
    max = num_list[-1]
    print("Max: " + str(max))


def sort_temperature(num_list):
    num_list.sort()
    return num_list

def calc_median_temperature(num_list):
    sort_temperature(num_list)
    n = len(num_list)
    if n % 2 is 1:
        median = (num_list[(n-1)//2])
    else:
        median = ((num_list[n//2] + num_list[(n//2)-1])//2)
    return median

if __name__ == "__main__":
    main()