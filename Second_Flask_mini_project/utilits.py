from csv import reader
import os


def get_avr_data(file="hw.csv"):
    cm = 2.54  # on inc it's 2.54 cm
    kg = 0.45  # one pound it's 0,45 kg
    dir_containing_file = r'/Users/nick_mokrytskyi/PycharmProjects/Hillel /first_project/Second_Flask_mini_project'
    os.chdir(dir_containing_file)
    with open(file, 'r') as csv_file:
        csv_reader = reader(csv_file)
        lst = []
        for row in csv_reader:
            lst.append(row)
    delete_text = lst.pop(0)  # Delete the first list with the string;
    delete_last_empty_element = lst.pop(-1)  # Delete the last empty string;
    height_list = list(map(lambda x: x[1], lst))
    weight_list = list(map(lambda x: x[2], lst))
    result_height = round((sum([eval(item) for item in height_list]) * cm) / len(height_list))
    result_weight = round((sum([eval(item) for item in weight_list]) * kg) / len(weight_list), 1)
    return result_height, result_weight


average = get_avr_data()
