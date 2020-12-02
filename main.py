"""
Brandon Willison CS 118
Project 2
"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa Grande": [76, 69, 60, 64, 69],
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


def avg_route_temperature(route):
    temp = 0
    for c in range(len(route)):  # 0,1,2,3,4
        city = route[c]
        temp += city_temps[city][c]  # c = 0 => city_temps[Casa_Grande][0] === 76
    return temp/len(route)


def best_route(all_routes):
    highest_avg_temp = 0
    best_temp_route = None
    for route in all_routes:
        avg_temp = avg_route_temperature(route)
        if highest_avg_temp < avg_temp:
            highest_avg_temp = (avg_temp)
            best_temp_route = route
    return best_temp_route, highest_avg_temp


def cost_of_hotel_set(hotel_list_combo):
        total_cost = 0
        for hotel in hotel_list_combo:
            total_cost += hotel_rates[hotel]
        return total_cost


def best_set_of_hotels(all_hotel_sets):
    max = 0
    best = None
    for set in all_hotel_sets:
        total_hotel_cost = cost_of_hotel_set(set)
        if max < total_hotel_cost and total_hotel_cost <= HOTEL_BUDGET:
            max = (total_hotel_cost)
            best = total_hotel_cost
    return best

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    best_route(permutations(cities))
    best_set_of_hotels(combinations_with_replacement(hotel_rates, len(hotels)))

    print(f"Here is your best route: {None} the average of the daily max temp. is {None}F")
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {None}, totaling ${None}')


