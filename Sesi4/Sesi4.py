# try:
#    file = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#    # perform file operations
# finally:
#    file.close()




with open("sample.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")


f = open("sample.txt",'r',encoding = 'utf-8')


# print(f.read(4))
# print(f.read(4))
# print(f.read())
# print(f.read())
# print(f.tell())
# f.seek(0)
# print(f.read())

# f.seek(0) 
# for line in f:
#   print(line, end = '')

# f.seek(0)
# print(f.readlines())


# with open('sample.txt', 'r') as reader:
#      print(reader.read())


# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

import sys
def os_interaction():
    # assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# try:
#     os_interaction()
# except:
#     pass

# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')


# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

# try:
#     os_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('os_interaction() function was not executed')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')