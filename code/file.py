# IMPORT: 由于 python work directory 为 /Volumes/Data/GitHub/python_demo/code
# 所以 相对路径不能包含 code
filename = 'assets/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string + "\n" + str(len(pi_string)))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

filename = 'assets/guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        try:
            with open(filename, 'a') as f:
                f.write(name + "\n")
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write(name + "\n")
                print("Hi " + name + ", you've been added to the guest book.")
        else:
            print("Hi " + name + ", you've been added to the guest book.")

filename = 'assets/programming_poll.txt'
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
try:
    with open(filename, 'a') as f:
        for response in responses:
            f.write(response + "\n")
except FileNotFoundError:
    with open(filename, 'w') as f:
        for response in responses:
            f.write(response + "\n")

filenames = ['assets/cats.txt', 'assets/dogs.txt']
for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            contents = f.read()
            print(contents)

import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It's " + str(number) + ".")

# 获取目录文件
import os.path

# path = '/Volumes/Data/GitHub/python_demo'
ls = []


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'PY':  # 检索指定路径下后缀JPG的文件 PY -> JPG
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path, ls)
    # print(len(ls))
    print(ls)
    print(len(ls))


if __name__ == '__main__':
    main()
