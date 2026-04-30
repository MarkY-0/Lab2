def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
      

def get_user_input():
    entered_input = input("Enter your numbers: ")
    string_list = entered_input.split(",")
    float_list = []
    for num in string_list:
        ndata_type = float(num)
        float_list.append(ndata_type)
    return float_list




def calc_average_temperature(temperature_list):
    total = sum(temperature_list)
    average = total / len(temperature_list)
    return float(average)

def calc_min_max_temperature(list_temp):
    min_temp = min(list_temp)
    max_temp = max(list_temp)
    int_min = int(min_temp)
    int_max = int(max_temp)
    final_list = [int_min , int_max]
    return final_list

def calc_median_temperature(temp_list):
    asc_sorted_list = sorted(temp_list)
    middle_index = len(asc_sorted_list) //2
    median = asc_sorted_list[middle_index]
    return median
    

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

if __name__ == "__main__":
    main()



