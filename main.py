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
    """Finds the average temp for a route. A route is a tuple from a list of permutations"""
    temp = 0
    for c in range(len(route)):
        city = route[c]
        temp += city_temps[city][c]
    avg_temp = temp/len(route)
    return avg_temp


def coldest_route(all_routes):
    """Finds the route that would have the lowest average daily temperature"""
    temp = 0
    coldest_route = min(all_routes, key=lambda x: route_avg_temp(x))
    for cities in range(len(coldest_route)):
        city = coldest_route[cities]
        temp += city_temps[city][cities]
    lowest_avg_temp = temp/len(coldest_route)
    return coldest_route, lowest_avg_temp


def warmest_route(all_routes):
    """Finds the route that would have the highest average daily temperature"""
    temp = 0
    warmest_route = None
    for route in all_routes:
        avg_temp = route_avg_temp(route)
        if temp < avg_temp:
            temp = avg_temp
            warmest_route = route

    return warmest_route, temp


def cost_of_hotel_combo(hotel_combo):
    """Finds the total cost of a combination of hotels from the hotel_rates dictionary"""
    total_cost = 0
    for hotel in hotel_combo:
        total_cost += hotel_rates[hotel]
    return total_cost


def best_combo_of_hotels(all_hotel_combos):
    """Finds the combination of hotels that when their rates are added is closest to the hotel budget"""
    total_cost = 0
    best_combo = None
    for hotel_combo in all_hotel_combos:
        total_hotel_cost = cost_of_hotel_combo(hotel_combo)
        if total_cost < total_hotel_cost <= HOTEL_BUDGET:
            total_cost = total_hotel_cost
            best_combo = hotel_combo
    return best_combo, total_cost


if __name__ == "__main__":

    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    warmest_route, highest_avg_temp = warmest_route(permutations(cities))
    coldest_route, lowest_avg_temp = coldest_route(permutations(cities))

    best_combo, total_cost = best_combo_of_hotels(combinations_with_replacement(hotels, len(cities)))

    print(f"Here is the best route for your {len(cities)} day trip: {warmest_route} the average daily max "
          f"temperature is {highest_avg_temp}F")
    print(f"Here is the worst route for your {len(cities)} day trip: {coldest_route}, with an average daily max temp "
          f"of {lowest_avg_temp}F")
    print(f'To max out your hotel budget, stay at these hotels: {best_combo}, totaling ${total_cost}')
