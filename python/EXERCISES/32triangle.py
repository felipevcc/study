# print triangle

def main():
    
    size = int(input("size: "))
    i = 0

    for line in range(size, 0, -1):
        for spaces in range(size, 0, -1):
            if i >= spaces:
                print("#", end="")
            else:
                print(" ", end="")
        print("\n")
        i += 1

if __name__ == "__main__":
    main()
