import urllib.request
import requests
import datetime
import os
import csv
import math
from functools import partial


class Distance:
    lng = 0.0
    lat = 0.0

    def __init__(self, lat, lng):
        self.lng = lng
        self.lat = lat

    @staticmethod
    def euclidean(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    euc = partial(euclidean, lat, lng)

    def get_distance(self):
        init_date = datetime.datetime(2020, 1, 22)
        current_date = datetime.datetime.today()

        while current_date > init_date:
            # current_date = current_date - datetime.timedelta(days=1)

            try:
                url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}"

                current_date_format = current_date.strftime("%m-%d-%Y")

                filename = "{}.csv".format(current_date_format)
                if not os.path.exists("files"):
                    os.mkdir("files")
                filename_to_saved = "files/" + filename

                if not os.path.exists(filename_to_saved):
                    url = url.format(filename)

                    r = requests.head(url)

                    if r.status_code == 200:

                        filename, headers = urllib.request.urlretrieve(url, filename=filename_to_saved)

                        mycsv = csv.reader(open(filename))
                        dct = {}
                        mycsv = list(mycsv)[1:]
                        for lines in mycsv:
                            if lines[0] is not "FIPS" and lines[1] is not "Admin2":
                                dct[lines[11]] = [lines[5], lines[6]]

                        # print(dct)
                        distance = []
                        for k in dct.keys():
                            if len(dct[k][0]):
                                d = self.euc(float(dct[k][0]), float(dct[k][0]))
                                distance.append((k, d))

                        distance = sorted(distance, key=lambda x: x[1])
                        nearest_distance = distance[0][1]
                        return nearest_distance
                    else:
                        current_date = current_date - datetime.timedelta(days=1)
                else:
                    mycsv = csv.reader(open(filename_to_saved))
                    dct = {}
                    mycsv = list(mycsv)[1:]
                    for lines in mycsv:
                        if lines[0] is not "FIPS" and lines[1] is not "Admin2":
                            dct[lines[11]] = [lines[5], lines[6]]

                    distance = []
                    for k in dct.keys():
                        if len(dct[k][0]):
                            d = self.euc(float(dct[k][0]), float(dct[k][0]))
                            distance.append((k, d))

                    distance = sorted(distance, key=lambda x: x[1])
                    nearest_distance = distance[0][1]
                    return nearest_distance
            except Exception as e:
                print(e)
                return 0


d = Distance(23.9535742, 90.14949879999999)
print(d.get_distance())
