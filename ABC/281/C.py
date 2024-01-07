def main():
    from builtins import print, map, int, list, exit
    from sys import stdin

    readline = stdin.readline

    n, t = map(int, readline().split())
    a = list(map(int, readline().split()))

    a_sum = sum(a)
    last_truck_sec = t-(a_sum*(t//a_sum))

    # print(last_truck_sec)

    sum_last_sec = 0
    for i in range(n):
        sum_last_sec += a[i]
        if sum_last_sec > last_truck_sec:
            print(i+1, last_truck_sec - (sum_last_sec - a[i]))
            exit()


if __name__ == "__main__":
    main()
