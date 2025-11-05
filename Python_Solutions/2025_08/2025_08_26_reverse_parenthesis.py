def decode(s):
    open_par_indexes = []
    close_par_indexes = []
    letters_in_begining = ""
    letters_in_end = ""
    i = 0
    end_index = len(s)
    result = ""

    if s[0] == "(" and s[-1] == ")":
        i = 1
        end_index = len(s) - 1

    while i < end_index:
        if s[i] == "(":
            open_par_indexes.append(i)
            
        if s[i] == ")":
            close_par_indexes.insert(0, i)
        
        if len(open_par_indexes) == 0:
            letters_in_begining += s[i]

        if open_par_indexes and len(open_par_indexes) == len(close_par_indexes):
            reversed_text = ""

            for j in range(len(open_par_indexes) - 1, -1, -1):
                if j == len(open_par_indexes) - 1:
                    reversed_text += s[open_par_indexes[j] + 1: close_par_indexes[j]][::-1]
                else:
                    reversed_text = (s[open_par_indexes[j] + 1: open_par_indexes[j + 1]] 
                                     + reversed_text 
                                     + s[close_par_indexes[j + 1] + 1: close_par_indexes[j]])[::-1]

            if i < end_index - 1:
                for j in range(i + 1, end_index):
                    if not s[j] == "(":
                        letters_in_end += s[j]
                    else:
                        i = j - 1
                        break
            
            reversed_text = (letters_in_begining + reversed_text + letters_in_end)
            letters_in_begining = ""
            letters_in_end = ""
            
            result += reversed_text
            
            open_par_indexes.clear()
            close_par_indexes.clear()
            
        i += 1

    if letters_in_end:
        result += letters_in_end

    if s[0] == "(" and s[-1] == ")":
        result = result[::-1]
            
    return result

# print(decode("(f(b(dc)e)a)"))
# print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
# print(decode("f(Ce(re))o((e(aC)m)d)p"))