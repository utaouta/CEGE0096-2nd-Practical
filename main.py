
def main():

    n = int(input('Please enter an integer: '))
    while 1<= n <=7:
        if n == 1:
            print('Monday')
            n = int(input('Please enter an integer: '))
        elif n == 2:
            print('Tuesday')
            n = int(input('Please enter an integer: '))
        elif n == 3:
            print('Wednesday')
            n = int(input('Please enter an integer: '))
        elif n == 4:
            print('Thursday')
            n = int(input('Please enter an integer: '))
        elif n == 5:
            print('Friday')
            n = int(input('Please enter an integer: '))
        elif n == 6:
            print('Saturday')
            n = int(input('Please enter an integer: '))
        elif n == 7:
            print('Sunday')
            n = int(input('Please enter an integer: '))
        else:
            print('The provided integer does not correspond to a day!')
            n = 8
    print("program ends")
    
    
if __name__ == '__main__':
    main()
