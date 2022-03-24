from repositories.ContestRepo import ContestRepo
from utils.contestFetcher import ContestFetcher


if __name__ == "__main__":

    # res = contests_collection_ref.insert_one({"name":"sajid"})
    # print(res.inserted_id)
    contestFetcher = ContestFetcher()

    print("LeetCode:")
    leetCodeContests = contestFetcher.getLeetCodeContests();
    ContestRepo.insert_contests(leetCodeContests)
    while(True):
      pass