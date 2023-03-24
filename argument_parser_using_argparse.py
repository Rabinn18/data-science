#step 1: importing argparse
import argparse

#step 2: Creating an parser object from argparse.ArgumentParser()
parser = argparse.ArgumentParser()

# #step 3: adding Arguments
# parser.add_argument('-f', "--file", required = True, help = "name of a file")

# #step 4: Parsing the argument parser
# args = parser.parse_args()

# file = open(args.file, 'r')
# data = file.read()
# print(data)
# file.close()

# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print('a*b')

parser.add_argument('-i', "--inumber", required = True, help = "first number")
parser.add_argument('-j', "--jnumber", required = True, help = "second number")

def addition(a, b):
    return (a*b)

add = addition(args.inumber, args.jnumber)
print(add)