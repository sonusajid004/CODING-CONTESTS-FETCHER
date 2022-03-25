import enum
from typing import Final


class CodingWebsite:
    LEETCODE:Final = "https://leetcode.com/"
    CODECHEF:Final = "https://www.codechef.com/"

class CodingPlatforms:
    LEETCODE:Final = "Leetcode"
    CODECHEF:Final = "Codechef"

class ContestType(str,enum.Enum):
    HIRING = "HIRING"
    RATED = "RATED"
    HACKATHON = "HACKATHON"
    CODING_CONTEST = "CODING_CONTEST"

class StatusValue(str,enum.Enum):
    SUCCESS="SUCCESS"
    FAILURE="FAILURE"