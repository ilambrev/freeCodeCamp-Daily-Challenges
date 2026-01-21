def parse_inline_code(markdown):
    markdown = [s for s in markdown]
    counter = 1

    for i in range(len(markdown)):
        if (markdown[i] == "`"):
            markdown[i] = "</code>" if counter % 2 == 0 else "<code>"
            counter += 1

    return "".join(markdown)

# print(parse_inline_code("Use `let` to declare the variable."))
# print(parse_inline_code("Use `let` or `const` to declare a variable."))
# print(parse_inline_code("Run `npm install` then `npm start`."))