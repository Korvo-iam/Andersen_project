def first_input():
    print("Please, type a number ")
    Val1 = input()
    if int(Val1) > 7:
        print('Hello')
def second_input():
    print("Please, type a name ")
    Val2 = input()
    if str(Val2) == 'John':
        print('Hello, John')
    else:
        print('There is no such name')
def third_input():
    print("Please, type an array like this : '3 18 45' ")
    try:
        Val3 = list(map(int, input().split()))
        sequence=[]
        for number in Val3:
            if int(number) % 3 == 0:
                sequence.append(number)
        if len(sequence) == 0:
            print('nothing to print')
        else:
            print(sequence)
    except ValueError:
        print('Incorrect value type')

def start():
    first_input()
    second_input()
    third_input()

start()
