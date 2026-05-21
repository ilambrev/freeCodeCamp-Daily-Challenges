import re

def i_before_e(sentence):
    sentence = re.sub(r"(?<!c)ei", "ie", sentence)
    sentence = re.sub(r"(?<=c)ie", "ei",sentence)

    return sentence

# print(i_before_e("beleive"))
# print(i_before_e("recieve"))
# print(i_before_e("we recieved a breif"))
# print(i_before_e("she beleived the friendly niece could percieve the greif"))
# print(i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit"))