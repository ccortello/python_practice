# Author = CCortello
# Date = 8/12/2016

"""Description"""

import math
import urllib.request


def get_percentage(a, b):
    """
    Calculate and print the necessary 'perfect shots' needed in
    order to increase to the next percentage
    """

    # calculate percentage as a float
    percentage = float(a) / b * 100
    print("\nYour current percentage is", percentage)
    print("After a miss your percentage would be", float(a) / (b - 1) * 100)
    print("\n%\tHS Needed\tFinal Count")

    if percentage == int(percentage):
        current_percentage = percentage + 1
    else:
        current_percentage = math.ceil(percentage)

    while current_percentage <= 99:
        headshots = math.floor((a - b * current_percentage / 100) / (
            current_percentage / 100 - 1) + 1)
        print(str(current_percentage) + '\t' + str(headshots) + '\t\t' +
              str(headshots + a))
        current_percentage += 1


with urllib.request.urlopen("http://steamcommunity.com/id/mistletoed/inventory/json/440/2") as f:
    data = str(f.read())
    pos = data.find("Strange Specialized Killstreak Bazaar Bargain")
    kills = int(data[pos + 197:pos + 201])
    headshots = int(data[pos + 444:pos + 448])
    get_percentage(headshots, kills)
