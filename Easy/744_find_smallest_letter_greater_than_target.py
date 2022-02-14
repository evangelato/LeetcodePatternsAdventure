class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_index = self.searchRecursive(
            letters, target, 0, len(letters) - 1, (len(letters) - 1) // 2
        )

        return letters[target_index]

    def searchRecursive(
        self,
        letters: List[int],
        target: str,
        left_index: int,
        right_index: int,
        mid_index: int,
    ):
        if left_index > right_index:
            return self.findNext(letters, mid_index, target)

        mid_index = (left_index + right_index) // 2

        if letters[mid_index] == target:
            return self.findNext(letters, mid_index, target)
        elif target < letters[mid_index]:
            return self.searchRecursive(
                letters, target, left_index, mid_index - 1, mid_index
            )
        else:
            return self.searchRecursive(
                letters, target, mid_index + 1, right_index, mid_index
            )

    def findNext(
        self,
        letters: List[int],
        mid_index: int,
        target: str,
    ):
        while mid_index < len(letters) and letters[mid_index] <= target:
            mid_index += 1
        return mid_index % len(letters)


class LinearSolution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]
