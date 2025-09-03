def solution(nums: list) -> list:
    temp = sorted(nums)
    res = []
    last = (None, None)
    for i, n in enumerate(temp):
        if n == last[0]:
            temp.append(last[1])
        # else:
        #     temp = (n, i
        #     temp.append(i)

