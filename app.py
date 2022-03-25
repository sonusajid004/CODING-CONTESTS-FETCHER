from contants import CodingPlatforms
from repositories.ContestRepo import ContestRepo
from utils.contestFetcher import ContestFetcher
import sys

if __name__ == "__main__":

    print("CLI ARGS:")
    print(sys.argv)
    contestFetcher = ContestFetcher()

    print("LeetCode:")
    leetCodeContests = contestFetcher.getLeetCodeContests();
    ContestRepo.insert_contests(leetCodeContests,CodingPlatforms.LEETCODE)

    print("Codechef:")
    codechefContests = contestFetcher.getCodechefContests();
    ContestRepo.insert_contests(codechefContests,CodingPlatforms.CODECHEF);

