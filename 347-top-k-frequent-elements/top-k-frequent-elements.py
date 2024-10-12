class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_set = {}

        for num in nums:
            if num in n_set.keys():
                n_set[num] += 1
            else:
                n_set[num] = 1

        sorted_keys = sorted(n_set, key=n_set.get, reverse=True)

        return sorted_keys[:k]