def elevator_stops(current_floor, stops):
    order = []
    floor = current_floor

    while stops:
        stops.sort(key=lambda s: (abs(floor - s), s))
        floor = stops[0]
        order.append(floor)
        stops.remove(floor)

    return order

# print(elevator_stops(5, [2, 8, 3, 9]))
# print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))
# print(elevator_stops(1, [4, 8, 3, 6, 9]))
# print(elevator_stops(12, [6, 10, 7, 3, 1, 4]))
# print(elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]))