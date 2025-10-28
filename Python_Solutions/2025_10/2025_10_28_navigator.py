def navigate(commands):
    start_page = "Home"
    history = [start_page]
    current_index = 0

    for command in commands:
        if command.startswith("Visit"):
            history = history[:current_index + 1]
            history.append(command[len("Visit "):])
            current_index += 1
        elif command.startswith("Back"):
            if len(history) > 1:
                current_index -= 1
        elif command.startswith("Forward"):
            if current_index < len(history) - 1:
                current_index += 1

    return history[current_index]

# print(navigate(["Visit About Us", "Back", "Forward"]))
# print(navigate(["Forward"]))
# print(navigate(["Back"]))
# print(navigate(["Visit About Us", "Visit Gallery"]))
# print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]))
# print(navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]))
# print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))