class Solution:
    def maximumProduct(self, nums):
        min_list, max_list = [], []
        for num in nums:
            if len(max_list) < 3:
                min_list.append(num); max_list.append(num)
                if len(max_list) == 3: min_list.sort(); max_list.sort(reverse=True)
            else:
                if num < min_list[0]: min_list = min_list = [num, min_list[0], min_list[1]]
                elif min_list[0] <= num < min_list[1]: min_list = [min_list[0], num, min_list[1]]
                elif min_list[1] <= num < min_list[2]: min_list = [min_list[0], min_list[1], num]

                if max_list[0] < num: max_list = [num, max_list[0], max_list[1]]
                elif max_list[1] < num <= max_list[0]: max_list = [max_list[0], num, max_list[1]]
                elif max_list[2] < num <= max_list[1]: max_list = [max_list[0], max_list[1], num]

        return max(max_list[0] * max_list[1] * max_list[2], min_list[0] * min_list[1] * max_list[0])
