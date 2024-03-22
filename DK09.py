def main(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True


if __name__ == '__main__':
    year = int(input())
    if year > 100000 or year <= 0:
        print("INVALID")
    else:
        if main(year):
            print("YES")
        else:
            print("NO")
