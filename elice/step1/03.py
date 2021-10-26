def main():
    order_count, work_time = map(int,input().split())
    orders = list(map(int,input().split()))
    count = 0
    sum = 0
    for i in range(order_count):
        sum += orders[i]
        if work_time < sum:
            break;
        count += 1
    print(count)



if __name__ == "__main__":
    main()