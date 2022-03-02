import enum
from typing import Final


class CodingWebsite:
    LEETCODE:Final = "Leetcode"
    CODECHEF:Final = "Codechef"

class ContestType(str,enum.Enum):
    HIRING = "HIRING"
    RATED = "RATED"
    HACKATHON = "HACKATHON"
    CODING_CONTEST = "CODING_CONTEST"
