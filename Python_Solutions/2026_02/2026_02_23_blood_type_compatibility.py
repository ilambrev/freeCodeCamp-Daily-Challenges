def can_donate(donor, recipient):
    blood_types = {
        "O": ["A", "B", "AB", "O"],
        "A": ["A", "AB"],
        "B": ["B", "AB"],
        "AB": ["AB"]
    }

    donor_letter = donor[:-1]
    donor_sign = donor[-1]
    recipient_letter = recipient[:-1]
    recipient_sign = recipient[-1]

    is_sign_compatible = donor_sign == "-" or donor_sign == recipient_sign

    return recipient_letter in blood_types[donor_letter] and is_sign_compatible

# print(can_donate("B+", "B+"))
# print(can_donate("O-", "AB-"))
# print(can_donate("O+", "A-"))
# print(can_donate("A+", "AB+"))
# print(can_donate("A-", "B-"))
# print(can_donate("B-", "AB+"))
# print(can_donate("B-", "A+"))
# print(can_donate("O-", "O+"))
# print(can_donate("O+", "O-"))
# print(can_donate("AB+", "AB-"))