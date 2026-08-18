class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit_counts = {}
        left = 0
        max_picked = 0

        for right in range(len(fruits)):
            current_fruit = fruits[right]
            fruit_counts[current_fruit] = fruit_counts.get(current_fruit, 0) + 1

            while len(fruit_counts) > 2 :
                left_fruit = fruits[left]
                fruit_counts[left_fruit] -= 1

                if fruit_counts[left_fruit] == 0:
                    del fruit_counts[left_fruit]
                left += 1
            max_picked = max(max_picked, right - left + 1)
        return max_picked
        