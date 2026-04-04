def get_browser_history(commands):
    history = []
    index = 0

    for command in commands:
        if command == "Back":
            index = max(0, index - 1)
        elif command == "Forward":
            index = min(len(history) - 1, index + 1)
        else:
            del history[index+1:]
            history.append(command)
            index = len(history) - 1

    return [history, index]

# print(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]))
# print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]))
# print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))
# print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]))
# print(get_browser_history(["example.com", "example.com/about", "Back", "Back"]))
# print(get_browser_history(["example.com", "example.com/about", "Forward"]))