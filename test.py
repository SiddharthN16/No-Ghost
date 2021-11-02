import keyboard
import time

messages = {"user1": "1:00", "user2": "2:00", "user3": "3:00", "user4": "4:00"}

# for key, value in enumerate(messages):
#     print(value, messages[value])

output = ""
for i in messages:
    output += f"{i}: {messages[i]}\n"
while True:
    if (keyboard.is_pressed('home')):
        print(output)
        break
