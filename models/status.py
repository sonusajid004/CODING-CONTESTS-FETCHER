import time

class Status:
    def __init__(self,codingPlatform:str,status:str,message:str):
        self.codingPlatform = codingPlatform
        self.status = status
        self.message = message
        self.timestamp = time.time()
