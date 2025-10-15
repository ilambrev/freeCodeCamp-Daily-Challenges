def strip_tags(html):
    result = html

    begin_index = result.find("<")

    while begin_index > -1:
        end_index = result.find(">")
        result = result[:begin_index] + result[end_index + 1:]
        begin_index = result.find("<")

    return result

# print(strip_tags('<a href="#">Click here</a>'))
# print(strip_tags('<p class="center">Hello <b>World</b>!</p>'))
# print(strip_tags('<img src="cat.jpg" alt="Cat">'))
# print(strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>'))