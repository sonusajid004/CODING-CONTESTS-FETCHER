import time


from utils.contestUtils import getHashForContest


class Contest:

    def __init__(self, contestTitle: str, startTime: int, duration: int, website: str,
                 contestType: str = 'CODING CONTEST'):
        self.contestTitle = contestTitle
        self.startTime = startTime
        self.duration = duration
        self.website = website
        self.contestType = contestType
        self.hashValue = getHashForContest(self)

    def __str__(self) -> str:
        return f'ContestId: {self._id} Website: {self.website}, Contest: {self.contestTitle}, Start Time: {self.startTime}, Duration: {self.duration}, Hash: {self.hashValue} '

    def isActive(self) -> bool:
        return time.time() < self.startTime

class SpojContest(Contest):

    def __init__(self, contestTitle: str, startTime: int, endTime: int, website: str,
                 contestType: str = 'CODING CONTEST'):
        super(SpojContest, self).__init__(contestTitle, startTime, 'NA', website, contestType)
        self.endTime = endTime

    def __str__(self) -> str:
        return f'ContestId: {self.contestId} Website: {self.website}, Contest: {self.contestTitle}, ' \
               f'Start Time: {self.startTime}, End Time: {self.endTime}, ' \
               f'Duration: {self.duration} '
