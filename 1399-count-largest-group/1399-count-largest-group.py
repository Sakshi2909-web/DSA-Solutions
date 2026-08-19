class Solution:
    def countLargestGroup(self, n):
        count = {}

        for num in range(1, n + 1):
            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            count[digit_sum] = count.get(digit_sum, 0) + 1

        max_size = max(count.values())

        return list(count.values()).count(max_size)     