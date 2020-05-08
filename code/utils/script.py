import urllib.request
import requests
import datetime
import os
import csv
import math
from functools import partial
from geopy import distance as gd


def euclidean(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_distance(lat, lng):
    init_date = datetime.datetime(2020, 4, 22)
    current_date = datetime.datetime.today()

    euc = partial(euclidean, lat, lng)

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
                current_location = (lat, lng)
                url = url.format(filename)

                r = requests.head(url)

                if r.status_code == 200:

                    filename, headers = urllib.request.urlretrieve(url, filename=filename_to_saved)

                    mycsv = csv.reader(open(filename))
                    dct = {}
                    mycsv = list(mycsv)[1:]
                    for lines in mycsv:
                        if lines[0] is not "FIPS" and lines[1] is not "Admin2":
                            dct[lines[11]] = gd.distance(current_location, (lines[5], lines[6])).kilometers

                    # distance = []
                    # for k in dct.keys():
                    #     if len(dct[k][0]):
                    #         d = euc(float(dct[k][0]), float(dct[k][0]))
                    #         distance.append((k, d))
                    #
                    distance = sorted(dct.items(), key=lambda x: x[1])
                    nearest_distance = distance[0][1]
                    return nearest_distance
                else:
                    current_date = current_date - datetime.timedelta(days=1)
            else:
                current_location = (lat, lng)
                mycsv = csv.reader(open(filename_to_saved))
                dct = {}
                mycsv = list(mycsv)[1:]
                for lines in mycsv:
                    if lines[0] is not "FIPS" and lines[1] is not "Admin2":
                        if len(lines[5]) and len(lines[6]):
                            dct[lines[11]] = gd.distance(current_location, (lines[5], lines[6])).kilometers

                # distance = []
                # for k in dct.keys():
                #     if len(dct[k][0]):
                #         d = euc(float(dct[k][0]), float(dct[k][0]))
                #         distance.append((k, d))
                #
                distance = sorted(dct.items(), key=lambda x: x[1])
                nearest_distance = distance[0][1]
                return nearest_distance
        except Exception as e:
            print(e)
            return 0.0
    return 0.0
