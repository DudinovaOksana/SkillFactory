import redis
import json

red = redis.Redis(
    host = "redis-13122.c13.us-east-1-3.ec2.cloud.redislabs.com",
    port = "13122",
    password = "UFMRcxAU2ee24bUN87Qc0lryg3QkKvci"
)
# red.set('1', input("Введите имя "))
# red.set('2', input("Введите имя "))
# red.set('3', input("Введите имя "))
# print(red.get('1'))
# print(red.get('2'))
# print(red.get('3'))
# red.delete('1') # удаляются ключи с помощью метода .delete()
# red.delete('2')
# red.delete('3')
# print(red.get('1'))
# print(red.get('2'))
# print(red.get('3'))

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break