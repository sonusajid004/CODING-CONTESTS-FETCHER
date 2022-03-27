import enum
from typing import Final


class CodingWebsite:
    LEETCODE:Final = "https://leetcode.com/"
    CODECHEF:Final = "https://www.codechef.com/"
    HACKEREARTH:Final = "https://www.hackerearth.com/"

class CodingPlatforms:
    LEETCODE:Final = "Leetcode"
    CODECHEF:Final = "Codechef"
    HACKEREARTH:Final = "HackerEarth"

class ContestType(str,enum.Enum):
    HIRING = "HIRING"
    RATED = "RATED"
    HACKATHON = "HACKATHON"
    CODING_CONTEST = "CODING_CONTEST"
    COMPETITIVE = "COMPETITIVE"

class StatusValue(str,enum.Enum):
    SUCCESS="SUCCESS"
    FAILURE="FAILURE"