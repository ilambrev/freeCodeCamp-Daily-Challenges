def get_movie_night_cost(day, showtime, number_of_tickets):
    days = {
        "Monday": {"price": 10, "discount": 2},
        "Tuesday": {"price": 10, "discount": 5},
        "Wednesday": {"price": 10, "discount": 2},
        "Thursday": {"price": 10, "discount": 2},
        "Friday": {"price": 12, "discount": 2},
        "Saturday": {"price": 12, "discount": 2},
        "Sunday": {"price": 12, "discount": 2}
    }

    part_of_day = showtime[-2:]
    hours = [int(t) for t in showtime[:-2].split(":")][0]

    ticket_price = days[day]["price"]

    if day == "Tuesday" or part_of_day == "am" or hours < 5:
        ticket_price -= days[day]["discount"]
    
    total_price = number_of_tickets * ticket_price

    return f"${total_price:.2f}"

# print(get_movie_night_cost("Saturday", "10:00pm", 1))
# print(get_movie_night_cost("Sunday", "10:00am", 1))
# print(get_movie_night_cost("Tuesday", "7:20pm", 2))
# print(get_movie_night_cost("Wednesday", "5:40pm", 3))
# print(get_movie_night_cost("Monday", "11:50am", 4))
# print(get_movie_night_cost("Friday", "4:30pm", 5))
# print(get_movie_night_cost("Tuesday", "11:30am", 1))