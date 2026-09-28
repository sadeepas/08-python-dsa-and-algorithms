"""
Two Pointers & Sliding Window Algorithms in Python
"""
from typing import List, Tuple

def two_sum_sorted(nums: List[int], target: int) -> Tuple[int, int]:
    """Finds indices (1-based) of two numbers that add up to target in O(N) time."""
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left + 1, right + 1)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)

if __name__ == "__main__":
    sorted_arr = [2, 7, 11, 15, 20, 25]
    tgt = 26
    idx1, idx2 = two_sum_sorted(sorted_arr, tgt)
    print(f"Two Sum result for target {tgt}: indices ({idx1}, {idx2}) -> values ({sorted_arr[idx1-1]}, {sorted_arr[idx2-1]})")
