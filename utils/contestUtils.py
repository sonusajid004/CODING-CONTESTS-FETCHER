import hashlib
import copy


def getHashForContest(c):
    from models.contest import Contest
    temp_contest = copy.deepcopy(c)
    return hashlib.md5(temp_contest.__dict__.__str__().encode()).hexdigest()

def objToDict(c):
    return list(map(lambda x:x.__dict__,c));
