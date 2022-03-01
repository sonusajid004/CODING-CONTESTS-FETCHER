import json
from models.contest import Contest
from contants import CodingWebsite
from apiUtils.network import *


def getLeetCodeContests():

    payload = """
 {\n  brightTitle\n  currentTimestamp\n  allContests {\n    containsPremium\n    title\n    cardImg\n    titleSlug\n    description\n    startTime\n    duration\n    originStartTime\n    isVirtual\n    company {\n      watermark\n      __typename\n    }\n    __typename\n  }\n}\n
"""
    url = "https://leetcode.com/graphql"
    pld = {'query': payload}
    response = post(url,pld)
    if(response.status_code == 200):
        json_data = json.loads(response.text)
        contests = json_data["data"]["allContests"]
        actualContestsData = []
        for contest in contests:
            actualContestsData.append(Contest(contest['title'],contest['startTime'],contest['duration'],CodingWebsite.LEETCODE))
        res = list(filter(lambda x: x.isActive(),actualContestsData))
        print(res[0])
    else:
        pass

def getCodechefContests():
    url = "https://www.codechef.com/api/list/contests/all"
    response = get(url)
    if (response.status_code == 200):
        json_data = json.loads(response.text)
        futureContests = json_data["future_contests"]
        presentContests = json_data["present_contests"]
        actualContestsData = []
        for contest in futureContests:
            actualContestsData.append(
                Contest(contest['contest_name'], contest['contest_start_date'], contest['contest_duration'], CodingWebsite.CODECHEF))
        for contest in presentContests:
            actualContestsData.append(
                Contest(contest['contest_name'], contest['contest_start_date'], contest['contest_duration'], CodingWebsite.CODECHEF))
        for contest in actualContestsData:
            print(contest)

getLeetCodeContests()
getCodechefContests()