from Resolution import *

from os.path import dirname, join
input=["input/input1.txt", "input/input2.txt", "input/input3.txt", "input/input4.txt", "input/input5.txt"]
output=["output/output1.txt", "output/output2.txt", "output/output3.txt", "output/output4.txt", "output/output5.txt"]

def main():
    for  i in range(0, len(input)):
        current_dir = dirname(__file__)
        print('File input '+str(i))
        fileIn = join(current_dir, input[i])
        fileOut = join(current_dir, output[i])
        resolution = Resolution()
        resolution.readFile(fileIn)
        resolution.resolution(fileOut)


        

if __name__ == '__main__':
    main()