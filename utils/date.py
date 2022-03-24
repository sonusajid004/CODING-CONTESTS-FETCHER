from dateutil import parser

def convertDateTimeToEpoch(value)->int:
    return parser.parse(value).timestamp()




