from csv import reader
def addition(a,b):
    result = a+b
    return result

def subtraction(a,b):
    result = a-b
    return result

def multipliction(a,b):
    result = a*b
    return result

def division(a,b):
    result = a/b
    return result

def square(a):
    return a*a

def cube(a):
    result = a*a*a
    return result

from student_datasets import Dataset.studentDataset
def extract(index_num):    
    empty_list = []
    for item in student_datasets[1:]:
        empty_list.append(item[index_num])
    return empty_list 


def freq_table(input_list): # using extracted data from above function as single parameter
    freq_dict = {}
    for item in input_list:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict


# def freq_table(datasets, index):
#     freq_dict = {}
#     for item in dataset:

def read_csv(file):
