# 无限循环
active = 1  # >0 为 true
while active == 1:  # 表达式永远为 true
    num = int(input("输入一个数字:"))
    if num == 100:
        active = 0
    else:
        print("你输入的数字是:", num)
print("Good bye!")

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
# 查询质数
print('=======查询质数=======')
num = int(input("输入一个数字："))
for n in range(2, num):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
input("点击 enter 键退出")

# quit loop
quit_str = 'quit'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\Enter " + quit_str + "to end program."
message = ""
while message != quit_str:
    message = input(prompt)
    if message != quit_str:
        print(message)

prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter " + quit_str + " when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# ====== Polling ======
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# ====== Restaurant Seating ======
party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)
if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

# ====== Movie Tickets ======
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

# ====== No Pastrami ======
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# ====== Dream Vacation ======
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
# Responses will be stored in the form {name: place}.
responses = {}
while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)
    # Store the response.
    responses[name] = place
    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
