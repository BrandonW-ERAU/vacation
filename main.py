"""
Brandon Willison CS 118
Project 2
"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}


HOTEL_BUDGET = 850

# ...

# ...

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    # ..
    print(f'Here is your best route: {None} the average of the daily max temp. is {None}F')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {None}, totaling ${None}')
