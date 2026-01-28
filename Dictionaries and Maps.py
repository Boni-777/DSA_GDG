# Enter your code
n = int(input())
phone_book = {}
for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone
while True:
    try:
        entry = input()
        if entry in phone_book:
            print(f"{entry}={phone_book[entry]}")
        else:
            print("Not found")
    except EOFError:
        break
