def main():
    from builtins import print, list, map, int, sorted, set, max
    from sys import stdin

    readline = stdin.readline

    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))

    candidate_set = sorted(set(a))
    vote = {candidate_set[i]:0 for i in range(len(candidate_set))}

    # print(vote)

    for A in a:
        vote[A] += 1
        print(max(vote, key=vote.get))

if __name__ == "__main__":
    main()
