import json
import time

from bs4 import BeautifulSoup
from typing import List
from utils.date import convertDateTimeToEpoch
from utils.network import get, post
from contants import CodingWebsite, CodingPlatforms, ContestType
from models.contest import SpojContest, Contest


class ContestFetcher:

    def __init__(self):
        pass

    def getLeetCodeContests(self) -> List[Contest]:
        try:
            print("---Started fetching contests from Leetcode---")
            start = time.perf_counter();
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
                        Contest(CodingPlatforms.LEETCODE, contest['title'], contest['startTime'], contest['duration'],
                                CodingWebsite.LEETCODE, CodingWebsite.LEETCODE+"contest/"+contest['titleSlug']))
                res = list(filter(lambda x: x.isActive(), actualContestsData))
                print(f"---Fetched contests from Leetcode in {time.perf_counter() - start}")
                return res
            else:
                print("Error Occured while retreiving contests info from Leetcode.")
                print(f"Error Occured with status {response.status_code}: {response.content}")
                return []
        except Exception as e:
            print("Error Occured while retreiving contests info from Leetcode.")
            print("Error info: " + e)
            return []


    def getCodechefContests(self):
        try:
            print("---Started fetching contests from Codechef---")
            start = time.perf_counter();
            url = "https://www.codechef.com/api/list/contests/all"
            response = get(url)
            if (response.status_code == 200):
                json_data = json.loads(response.text)
                futureContests = json_data["future_contests"]
                presentContests = json_data["present_contests"]
                actualContestsData = []
                for contest in futureContests:
                    actualContestsData.append(
                        Contest(CodingPlatforms.CODECHEF, contest['contest_name'],
                                convertDateTimeToEpoch(contest['contest_start_date']), contest['contest_duration'],
                                CodingWebsite.CODECHEF,CodingWebsite.CODECHEF + contest['contest_code']))
                for contest in presentContests:
                    actualContestsData.append(
                        Contest(CodingPlatforms.CODECHEF, contest['contest_name'],
                                convertDateTimeToEpoch(contest['contest_start_date']), contest['contest_duration'],
                                CodingWebsite.CODECHEF, CodingWebsite.CODECHEF+ contest['contest_code']))
                print(f"---Fetched contests from Codechef in {time.perf_counter() - start}")
                return actualContestsData
            else:
                print("Error Occured while retreiving contests info from Codechef.")
                print(f"Error Occured with status {response.status_code}: {response.content}")
                return []
        except Exception as e:
            print("Error Occured while retreiving contests info from Codechef.")
            print("Error info: " + e)
            return []


    def getHackerEarthContests(self):
        try:
            print("---Started fetching contests from HackerEarth---")
            start = time.perf_counter();
            url = "https://www.hackerearth.com/challenges/"
            response = get(url)
            contests = []
            if (response.status_code == 200):
                soup = BeautifulSoup(response.content, 'html.parser')
                challengesCardWrapper = soup.select(".challenge-card-modern")
                for elem in challengesCardWrapper:
                    challengeAnchor = elem.select(".challenge-card-link")
                    if(len(challengeAnchor)==0):
                        continue
                    else:
                        challengeAnchor = challengeAnchor[0]
                    challengeLink = str(CodingWebsite.HACKEREARTH) + str(challengeAnchor.get("href"))
                    challengeContent = elem.select(".challenge-content")
                    if (len(challengeContent) == 0):
                        continue

                    challengeContent = challengeContent[0]
                    challengeTypeElement = challengeContent.select(".challenge-type")
                    if (len(challengeTypeElement) != 0):
                        challengeType = challengeTypeElement[0].text.strip()
                    else:
                        continue
                    if(challengeType not in [ContestType.HIRING,ContestType.COMPETITIVE,ContestType.RATED]):
                        continue
                    challengeDetailedInfo = get(challengeLink)
                    if(challengeDetailedInfo.status_code==200):

                        challengeSoup = BeautifulSoup(challengeDetailedInfo.content, 'html.parser')
                        eventTimings = challengeSoup.select(".event-timings")
                        if(len(eventTimings)==0):
                            continue
                        eventTimings = eventTimings[0].select(".timing")
                        if(len(eventTimings)!=3):
                            continue
                        challengeStartText = eventTimings[0].select(".timing-text")[0].text
                        challengeStartTimestamp = convertDateTimeToEpoch(challengeStartText)
                        durationtext = eventTimings[2].select(".timing-text")[0].text
                        durationArr = durationtext.split(" ")
                        duration = 0

                        for i in durationArr:
                            i = i.lower()
                            if(i.find("h")!=-1):
                                duration = duration + int(i.strip("h"))*60
                            elif(i.find("m")!=-1):
                                duration = duration + int(i.strip("m"))



                        challengeNameElement = challengeContent.select(".challenge-name")

                        challengeType = None
                        challengeName = None
                        challengeStartsOrEndsElement = challengeContent.select(".challenge-desc .smaller")
                        challengeDate = challengeContent.select(".challenge-desc .date")
                        # challengeDateText = None
                        # if (len(challengeStartsOrEndsElement) != 0):
                        #     if (challengeStartsOrEndsElement[0].text.strip() == "STARTS ON"):
                        #         challengeDateText = challengeDate[0].text
                        #     else:
                        #         continue
                        # else:
                        #     continue

                        if (len(challengeNameElement) != 0):
                            challengeName = challengeNameElement[0].text.strip()
                        else:
                            continue
                    contests.append(Contest(CodingPlatforms.HACKEREARTH, challengeName,
                            challengeStartTimestamp, duration,
                            CodingWebsite.HACKEREARTH, challengeLink,challengeType))
                print(f"---Fetched contests from Hackerearth in {time.perf_counter() - start}")
                return contests

            else:
                print("Error Occured while retreiving contests info from HackerEarth.")
                print("Response:"+response.status_code+" Message:"+response.content)
                return []
        except Exception as e:
            print(f"Error Occured while retreiving contests info from HackerEarth.")
            print("Error info: "+e)
            raise e;


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
