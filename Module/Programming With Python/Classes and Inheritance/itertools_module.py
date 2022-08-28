# Python has an “itertools” module that provides built-in efficient iterator functions for high-speed looping (Beazley & Jones, 2013).
# For example, we will look at the count(), cycle(), and repeat() functions.


from itertools import count, cycle, repeat

# count(start=0, step=1) — Make an iterator that returns evenly spaced values starting with number start.

# cycle(iterable) — Make an iterator returning elements from the iterable and saving a copy of each.

# repeat(object[, times]) — Make an iterator that returns object over and over again.
# It runs indefinitely unless the times argument is specified.


def main():
    sequence = count(start=2.5, step=0.5)
    while (next(sequence) <= 8):
        print(next(sequence))


if __name__ == '__main__':
    main()


def main():
    person = cycle(["employee", "customer"])
    count = 0
    while (count != 6):
        print(next(person))
        count += 1


if __name__ == '__main__':
    main()


def main():
    person = repeat(object=1000, times=3)
    count = 0
    while (count != 3):
        print(next(person))
        count += 1


if __name__ == '__main__':
    main()
