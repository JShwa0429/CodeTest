def main():
    num = int(input())
    num_list = []
    for x in range(num):
        if x % 3 == 0 or x % 5 == 0:
            num_list.append(x)
    print(sum(set(num_list)))

if __name__ == "__main__":
    main()