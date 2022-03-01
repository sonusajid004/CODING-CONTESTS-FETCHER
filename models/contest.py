import time
import uuid

class Contest:

    def __init__(self,contestTitle:str,startTime:int,duration:int,website:str):
        self.contestId:str = uuid.uuid1()
        self.contestTitle = contestTitle
        self.startTime = startTime
        self.duration = duration
        self.website = website

    def __str__(self)->str:
        return f'ContestId: {self.contestId} Website: {self.website}, Contest: {self.contestTitle}, Start Time: {self.startTime}, Duration: {self.duration} '
    
    def isActive(self)->bool:
        return time.time() < self.startTime
