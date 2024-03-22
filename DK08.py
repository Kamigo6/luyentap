def main():
    arg = input().split()

    a = int(arg[0])
    b = int(arg[2])

    match arg[1]:
        case '+':
            result = a + b
            print(f'{result:0.2f}')
        case '-':
            result = a - b
            print(f'{result:0.2f}')
        case '*':
            result = a * b
            print(f'{result:0.2f}')
        case '/':
            if b == 0:
                print("Math Error")

            else:
                result = a / b
                print(f'{result:0.2f}')


if __name__ == '__main__':
    main()
