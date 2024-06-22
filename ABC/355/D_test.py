def schedule_problem(brackets, slotsize=3):
    # 時間枠をソート
    brackets = sorted(brackets)
    print(brackets)

    ans = 0
    ans_lst = []
    slots = [-1] * slotsize

    for b in brackets:
        end_time, begin_time = b

        # スロットの中から、begin_timeより小さい値を持つスロットを選ぶ
        able = max([t for t in slots if t < begin_time], default=None)

        if able is not None:
            slots[slots.index(able)] = end_time
            ans += 1
            ans_lst.append(b)

    return ans, ans_lst


# 使用例
brackets = [(5, 1), (6, 2), (8, 3), (9, 4)]
brackets = [(3, 4), (2, 5), (1, 6)]
slotsize = 3
print(schedule_problem(brackets, slotsize))

