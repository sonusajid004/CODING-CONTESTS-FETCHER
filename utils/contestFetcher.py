import json

from bs4 import BeautifulSoup
from typing import List
from utils.date import convertDateTimeToEpoch
from utils.network import get, post
from contants import CodingWebsite
from models.contest import SpojContest, Contest



class ContestFetcher:

    def __init__(self):
        pass

    def getLeetCodeContests(self) -> List[Contest]:

        payload = """
     {\n  brightTitle\n  currentTimestamp\n  allContests {\n    containsPremium\n    title\n    cardImg\n    titleSlug\n    description\n    startTime\n    duration\n    originStartTime\n    isVirtual\n    company {\n      watermark\n      __typename\n    }\n    __typename\n  }\n}\n
    """
        url = "https://leetcode.com/graphql"
        pld = {'query': payload}
        response = post(url, pld)

        if (response.status_code == 200):
            json_data = json.loads(response.text)

            contests = json_data["data"]["allContests"]
            actualContestsData = []
            for contest in contests:
                actualContestsData.append(
                    Contest(contest['title'], contest['startTime'], contest['duration'], CodingWebsite.LEETCODE))
            res = list(filter(lambda x: x.isActive(), actualContestsData))
            return res
        else:
            print(f"Error Occured with status {response.status_code}: {response.content}")
            return []



    def getCodechefContests(self):
        url = "https://www.codechef.com/api/list/contests/all"
        response = get(url)
        if (response.status_code == 200):
            json_data = json.loads(response.text)
            futureContests = json_data["future_contests"]
            presentContests = json_data["present_contests"]
            actualContestsData = []
            for contest in futureContests:
                actualContestsData.append(
                    Contest(contest['contest_name'], convertDateTimeToEpoch(contest['contest_start_date']), contest['contest_duration'],
                            CodingWebsite.CODECHEF))
            for contest in presentContests:
                actualContestsData.append(
                    Contest(contest['contest_name'], convertDateTimeToEpoch(contest['contest_start_date']), contest['contest_duration'],
                            CodingWebsite.CODECHEF))
            for contest in actualContestsData:
                print(contest)
        else:
            print(f"Error Occured with status {response.status_code}: {response.content}")

    def getHackerEarthContests(self):
        url = "https://www.hackerearth.com/challenges/"
        response = get(url)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.content, 'html.parser')
            challengesContent = soup.select(".challenge-content")
            # print(challengesContent)
            for elem in challengesContent:
                challengeTypeElement = elem.select(".challenge-type")
                challengeNameElement = elem.select(".challenge-name")

                challengeType = None
                challengeName = None
                challengeStartsOrEndsElement = elem.select(".challenge-desc .smaller")
                challengeDate = elem.select(".challenge-desc .date")
                if (len(challengeStartsOrEndsElement) != 0):
                    if (challengeStartsOrEndsElement[0].text.strip() == "STARTS ON"):
                        print(challengeDate[0].text)
                else:
                    continue
                if (len(challengeTypeElement) != 0):
                    challengeType = challengeTypeElement[0].text.strip()
                else:
                    continue
                if (len(challengeNameElement) != 0):
                    challengeName = challengeNameElement[0].text.strip()
                else:
                    continue
                # print(challengeType,challengeName)

        else:
            pass

    def getSpojContests(self):

        def generate_contest(columns):
            if len(columns) != 0:
                name = columns[0].text.strip()
                link = 'spoj.com' + columns[0].find_all('a')[0].get('href')
                start = columns[1].text.strip()
                end = columns[2].text.strip()
                return SpojContest(name, start, end, link)

        url = 'https://www.spoj.com/contests/'
        r = get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # with open("output1.html", "w") as file:
        #     file.write(str(soup))

        tables = soup.find_all('table', class_='table-condensed')
        # Collecting Ddata
        running_contests = tables[0]
        future_contests = tables[1]
        actualContestsData = []

        for row in running_contests.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')
            actualContestsData.append(generate_contest(columns))

        for row in future_contests.tbody.find_all('tr'):
            columns = row.find_all('td')
            actualContestsData.append(generate_contest(columns))

        for contest in actualContestsData:
            print(contest)

