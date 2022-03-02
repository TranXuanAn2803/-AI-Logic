from MyAlgorithms import *

from os.path import dirname, join


def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input/input_1.txt")
    my_algo = MyAlgorithms()
    my_algo.read_input_data(file_path)
    my_algo.pl_resolution()

        

if __name__ == '__main__':
    main()