def solution(sequence, k):
    left, right = 0, 0
    curr_sum = sequence[0]
    shortest_len = float('inf')
    shortest_subseq = []

    while right < len(sequence):
        if curr_sum == k:
            curr_len = right - left + 1
            if curr_len < shortest_len:
                shortest_len = curr_len
                shortest_subseq = [left, right]

            curr_sum -= sequence[left]
            left += 1
        elif curr_sum < k:
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        else:
            curr_sum -= sequence[left]
            left += 1
    return shortest_subseq
