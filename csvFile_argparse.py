import argparse
from function.func import read_csv
parser = argparse.ArgumentParser()
parser.add_argument('-csv', "--csvFile", required = True, help = "opening csv file")
args = parser.parse_args()
# def read_csv(file):
#     f = open(file)
#     data = reader(f)

dataset = read_csv(args.csv)
print(dataset)