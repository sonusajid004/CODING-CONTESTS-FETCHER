from typing import List
from config.db import DB
from contants import StatusValue
from models.contest import Contest
from models.status import Status
from utils.contestUtils import objToDict


class ContestRepo:
    contests_collection_ref = DB["contests"]
    status_collection_ref = DB["status_jobs"]

    @classmethod
    def insert_contests(cls, contests: List[Contest],platform:str):
        try:
            contestsSerialized = objToDict(contests)
            query={"codingPlatform":platform}
            cls.contests_collection_ref.delete_many(query)
            res = cls.contests_collection_ref.insert_many(contestsSerialized)
            status = Status(platform,StatusValue.SUCCESS,"Finished")
            res = cls.status_collection_ref.insert_one(status.__dict__)
            print(f"Inserted contests from {platform}")
        except Exception as e:
            print(f"Error in inserting from {platform}: {e}")
            status = Status(platform, StatusValue.FAILURE, e)
            res = cls.status_collection_ref.insert_one(status.__dict__)


