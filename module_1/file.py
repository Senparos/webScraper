#this file contains all of the functions to open, read, write, and close files
#it uses the os module
#this file uses the Single-Responsibility Principle by having each function do one task

import os

def op(filename, mode):
    return open(filename, mode)
def read(file):
    return file.readline().strip()
def wr(data, num):
    file = op(os.path.join(os.getcwd(), "Data", "processed", f"processed{num}.txt"), "w")
    file.write(data)
    cl(file)
def wrSum(data, num):
    file = op(os.path.join(os.getcwd(), "Data", "summary", f"summary{num}.txt"), "w")
    file.write(data)
    cl(file)
def cl(file):
    file.close()