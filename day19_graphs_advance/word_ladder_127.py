from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        # End word must exist
        if endWord not in wordSet:
            return 0

        # BFS queue
        # (currentWord, transformationSteps)
        queue = deque()
        queue.append((beginWord, 1))

        # Visited words
        visited = set()
        visited.add(beginWord)

        # BFS
        while queue:

            word, steps = queue.popleft()

            # Target found
            if word == endWord:
                return steps

            # Try changing every position
            for i in range(len(word)):

                # Try all lowercase letters
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    # Create transformed word
                    newWord = word[:i] + ch + word[i + 1:]

                    # Valid unvisited word
                    if (
                        newWord in wordSet and
                        newWord not in visited
                    ):

                        visited.add(newWord)

                        queue.append((newWord, steps + 1))

        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = [
        "hot",
        "dot",
        "dog",
        "lot",
        "log",
        "cog" ]
    sol = Solution()
    result = sol.ladderLength(
        beginWord,
        endWord,
        wordList )

    print("Shortest Transformation Length:", result)