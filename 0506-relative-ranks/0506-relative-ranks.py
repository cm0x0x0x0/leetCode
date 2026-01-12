class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = ["" for i in range(len(score))]
        rank = [
            "Gold Medal",
            "Silver Medal",
            "Bronze Medal"
        ]

        scoreToIndexTable = dict()
        for idx, n in enumerate(score):
            scoreToIndexTable[n] = idx

        sortedScore = sorted(score, reverse=True)

        for idx, n in enumerate(sortedScore):
            result[scoreToIndexTable[n]] = rank[idx] if idx < 3 else str(idx+1)

        return result