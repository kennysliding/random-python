def sliding_window_sum(arr, window_length):
    window_sum = sum(arr[:window_length])
    total = window_sum
    current_index = window_length
    for i in range(len(arr) - window_length):
        window_sum = window_sum - arr[i] + arr[current_index]
        total += window_sum
        current_index += 1
    return total


class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        windows = len(arr) - (len(arr) + 1) % 2
        total = 0
        for window in range(1, windows + 1, 2):
            total += sliding_window_sum(arr, window)
        return total