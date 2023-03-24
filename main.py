import function
add = function.addition(9,4)
print("addition is",str(add))

from function import subtraction, cube
sub = subtraction(9,4)
print("subtraction is : {}".format(sub))

cu_3= cube(3)
print(cu_3)


faculty_data = function.extract(3)
print(faculty_data)

faculties_ft = function.freq_table(input_list = faculty_data)
print(faculties_ft)