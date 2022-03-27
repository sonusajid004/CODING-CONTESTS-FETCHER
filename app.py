from contants import CodingPlatforms, StatusValue
from models.status import Status
from repositories.ContestRepo import ContestRepo
from utils.contestFetcher import ContestFetcher
import sys

if __name__ == "__main__":

    print("CLI ARGS:")
    print(sys.argv)
    contestFetcher = ContestFetcher()

    try:
        leetCodeContests = contestFetcher.getLeetCodeContests()
        ContestRepo.insert_contests(leetCodeContests,CodingPlatforms.LEETCODE)
        status = Status(CodingPlatforms.LEETCODE, StatusValue.SUCCESS, "Finished")
        ContestRepo.insert_status(status)
    except Exception as e:
        status = Status(CodingPlatforms.LEETCODE, StatusValue.FAILURE, e)
        ContestRepo.insert_status(status)

    try:
        codechefContests = contestFetcher.getCodechefContests()
        ContestRepo.insert_contests(codechefContests,CodingPlatforms.CODECHEF)
        status = Status(CodingPlatforms.CODECHEF, StatusValue.SUCCESS, "Finished")
        ContestRepo.insert_status(status)
    except Exception as e:
        status = Status(CodingPlatforms.CODECHEF, StatusValue.FAILURE, e)
        ContestRepo.insert_status(status)

    try:
        hackerEarthContest =contestFetcher.getHackerEarthContests();
        ContestRepo.insert_contests(hackerEarthContest,CodingPlatforms.HACKEREARTH)
        status = Status(CodingPlatforms.CODECHEF, StatusValue.SUCCESS, "Finished")
        ContestRepo.insert_status(status)
    except Exception as e:
        status = Status(CodingPlatforms.HACKEREARTH, StatusValue.FAILURE, e)
        ContestRepo.insert_status(status)