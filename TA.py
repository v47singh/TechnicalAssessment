# A program to count the total number of line in a valid program file and
# calculate the total number of comments and further calculate the number
# of single line comments, block line comments, number of comments in block
# comments and the number of todo's in the file.
import os
import sys
import re

# variable to count number of todo lines
todo_lines = 0

# Function to read only one file at a time in the current directory with 
# a specific extension(in this for JAVA and JavaScript) which return total
# number of lines and the list consisting of all lines in a code file
def read_file():
    lines = 0 
    lines_list = []
    py_files = [f for f in os.listdir('.') if f.endswith('.java')] # for javascript need to change ".java" to ".jss"
    # checks if there is only one file in the current directory; if not
    # raises error
    if len(py_files) != 1:
        raise ValueError('should be only one txt file in the current directory')
    #stores the name of file
    filename = py_files[0]
    # Opens the file and read it line-by-line
    for line in open(filename):
        lines += 1
        lines_list.append(line) #copy the lines in a file in other list
    
    # print("lines", lines)
    # print("lines_list", lines_list)
    return lines, lines_list


# Function to calculate total number of single line comments and returns
# the count
def single_line_comments(lines_list):
    global todo_lines
    cmt_lines1 = 0
    for l in lines_list:
        # condition to check for single line comments
        if re.findall(r"//", l):
            cmt_lines1 += 1
            # condition to check an dcount todo comments
            if re.findall(r".(TODO:).", l):
                todo_lines += 1
    return cmt_lines1 # return the variable that counts single line comments

# Function to calculate and return total number of block line comments and 
# the total comments in a block comment
def block_line_comments(lines_list):
    global todo_lines
    cmt_lines2=0 # variable to count number of block line comment
    n = 0
    f = 0
    x = 0
    my_dict = {}
    for line in lines_list:
        # Checks if the line is a block line comment or not; if yes increase 
        # the counter
        if (not f):
            if re.findall(r"\/\*", line):
                cmt_lines2 += 1
                f = 1
        # Checks if the line in the block has end delimiter; if yes keep on
        # storing all the lines with val 1 in dictionary till the end of 
        # block line comment is found
        if f :
            my_dict[line] = 1
            if re.findall(r"\*\/", line):
                x += 1
                f = 0
    # Loop to check all the lines in which value for all lines stored in mydict 
    # is 1, and increase the counter to calculate all the block line comments
    for key, val in my_dict.items():
        if val != 0:
            n += 1
            #condition to check any TODOline comment
            if re.findall(r".(TODO:) .", key):
                todo_lines += 1
    return cmt_lines2, (cmt_lines2 + n + x) # returns number of block line comments  
                                            # and number of comment in a block

# main to call all the funcion and print all the values once calculated
if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    s = 0 
    s, lines_list = read_file() # calls the read_file()
    a = single_line_comments(lines_list) # calling the single_line_comments()
    b, c = block_line_comments(lines_list) # calling the block_line_comments()
    # variable to store total comments in a file
    cmt_lines = a + c
    # Print statements to output all the calculated values
    print("Total # of lines", s)
    print("Total # of comment lines", cmt_lines)
    print("Total # of single line comments", a)
    print("Total # of block line comments", b)
    print("Total # of comments in block line comments", c)
    print("Total # of TODO lines", todo_lines)