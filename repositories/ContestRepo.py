from typing import List
from config.db import DB
from models.contest import Contest
from utils.contestUtils import contestToDict


class ContestRepo:
    contests_collection_ref = DB["contests"]

    @classmethod
    def insert_contests(cls,contests: List[Contest]):
        contestsSerialized = contestToDict(contests)
        print(type(contestsSerialized[0]))
        res = cls.contests_collection_ref.insert_many(contestsSerialized)
        print(res)

