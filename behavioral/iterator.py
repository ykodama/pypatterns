def count_to(count):
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number

if __name__ == "__main__":
    count_to_two = lambda: count_to(2)
    count_to_five = lambda: count_to(5)

    print('Counting to two...')
    for n in count_to_two():
        print(n)

    print('Counting to five...')
    for n in count_to_five():
        print(n)
