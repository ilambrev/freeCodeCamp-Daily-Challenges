import re

def is_spam(number):
    pattern = r"^\+\d{1,2} \((\d{3})\) (\d{3})-(\d{4})$"

    if not re.fullmatch(re.compile(pattern), number):
        return True
    else:
        result = re.search(pattern, number)

        if int(result.group(1)) < 200 or int(result.group(1)) > 900:
            return True

        sum_of_digits = sum([int(digit) for digit in result.group(2)])

        if str(sum_of_digits) in result.group(3):
            return True

        local_number = result.group(1) + result.group(2) + result.group(3)

        for i in range(10):
            if local_number.count(str(i)) > 3:
                return True

    return False

# print(is_spam("+0 (200) 234-0182"))
# print(is_spam("+091 (555) 309-1922"))
# print(is_spam("+1 (555) 435-4792"))
# print(is_spam("+0 (955) 234-4364"))
# print(is_spam("+0 (155) 131-6943"))
# print(is_spam("+0 (555) 135-0192"))
# print(is_spam("+0 (555) 564-1987"))
# print(is_spam("+00 (555) 234-0182"))