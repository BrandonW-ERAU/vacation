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
HOTEL_BUDGET = 850
hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209

}


def route_avg_temp(route):
    temp = 0
    for c in range(len(route)):  # 0,1,2,3,4
        city = route[c]
        temp += city_temps[city][c]  # c = 0 => city_temps[Casa_Grande][0] === 76
    avg_temp = temp/len(route)
    return avg_temp


def coldest_route(all_routes):
    temp = 0
    coldest_route = min(all_routes, key=lambda x: route_avg_temp(x))
    for cities in range(len(coldest_route)):
        city = coldest_route[cities]
        temp += city_temps[city][cities]
    avg_lowest_temp = temp/len(coldest_route)
    return coldest_route, avg_lowest_temp


def warmest_route(all_routes):
    highest_avg_temp = 0
    best_temp_route = None
    for route in all_routes:
        avg_temp = route_avg_temp(route)
        if highest_avg_temp < avg_temp:
            highest_avg_temp = avg_temp
            best_temp_route = route
    return best_temp_route, highest_avg_temp


def cost_of_hotel_set(hotel_list_combo):
    total_cost = 0
    for hotel in hotel_list_combo:
        total_cost += hotel_rates[hotel]
    return total_cost


def best_set_of_hotels(all_hotel_sets):
    total_cost = 0
    best_set = None
    for hotel_Group in all_hotel_sets:
        total_hotel_cost = cost_of_hotel_set(hotel_Group)
        if total_cost < total_hotel_cost <= HOTEL_BUDGET:
            total_cost = total_hotel_cost
            best_set = hotel_Group
    return best_set, total_cost


if __name__ == "__main__":

    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    best_temp_route, highest_avg_temp = warmest_route(permutations(cities))
    coldest_route, avg_lowest_temp = coldest_route(permutations(cities))

    best, total_cost = best_set_of_hotels(combinations_with_replacement(hotels, len(cities)))

    print(f"Here is your best route for your {len(cities)} day trip: {best_temp_route} the average daily max "
          f"temperature is {highest_avg_temp}")
    print(f"Here is your worst route for your {len(cities)} day trip: {coldest_route}, with an average daily max temp "
          f"of {avg_lowest_temp}")
    print(f'To max out your hotel budget, stay at these hotels: {best}, totaling ${max}')
