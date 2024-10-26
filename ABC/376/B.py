def main():
    n, q = map(int, input().split())
    h = []
    t = []
    for _ in range(q):
        ht, tt = input().split()
        h.append(ht)
        t.append(int(tt)-1)

    left = 0
    right = 1

    ring = [False] * n
    ring[0] = True
    ring[1] = True

    ring2 = [i for i in range(n)]

    def search(hand, num):
        if num < hand:
            num += n-1
        return any(ring[i%n] for i in range(hand+1, num))

    ans = 0
    for i in range(q):
        if h[i] == "R":
            # print(search(right, t[i]))
            if search(right, t[i]):
                j = right
                count = 0
                while ring2[j] != t[i]:
                    count += 1
                    j -= 1
                    if j == -1:
                        j = n-1
                ans += count
                ring[right] = False
                ring[t[i]] = True
                right = t[i]
            else:
                j = right
                count = 0
                while ring2[j%n] != t[i]:
                    count += 1
                    j += 1
                ans += count
                ring[right] = False
                ring[t[i]] = True
                right = t[i]
        else:
            # print(search(left, t[i]))
            if search(left, t[i]):
                j = left
                count = 0
                while ring2[j] != t[i]:
                    count += 1
                    j -= 1
                    if j == -1:
                        j = n-1
                ans += count
                ring[left] = False
                ring[t[i]] = True
                left = t[i]
            else:
                j = left
                count = 0
                while ring2[j%n] != t[i]:
                    count += 1
                    j -= 1
                ans += count
                ring[left] = False
                ring[t[i]] = True
                left = t[i]
    print(ans)


if __name__ == '__main__':
    main()
