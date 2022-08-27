# conditional statement

def main():
    x = 10
    y = 5

    if x > y:
        print("true")

    x = 20
    y = 20

    if x < y:
        print("x<y is true")

    if x > y:
        print("x>y is true")


# the else and elif clause
    if x < y:
        print("x<y is true")
    elif x > y:
        print("x>y is true")
    elif x == y:
        print("x==y is true")


# for looping over

ebooks = ['Python', 'Java', 'Javascript']
for item in ebooks:
    print("The books is : {}".format(item))

# we can control the iteration using range function

for x in range(6, 11):
    print(x)

# while loops repeats as much as
# specific condition is true

i = 0
while ebooks[i] != 'Java':
    print(ebooks[i])
    i += 1

# break statement & continue
for item in ebooks:
    if item == 'Javascript':
        break
    else:
        print(item)
        continue

# use of pass keyword for the synthetical purpose
# when no codes need to be executed
# uses to define null operation


def print_no_values(value):
    if value == '1':
        pass
    else:
        print(value)


if __name__ == '__main__':
    main()
