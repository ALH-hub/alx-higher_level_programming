#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    result = 0

    if count == 0:
        print("0")
    else:
        for i in range(count):
            result += int(sys.argv[i+1])
        print("{}".format(result))
