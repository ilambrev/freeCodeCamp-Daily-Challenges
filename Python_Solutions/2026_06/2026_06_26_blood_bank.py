def triage_blood(bank, patients):
    def set_quantity(keys):
        dic = {}
        
        for key in keys:
            dic[key] = dic.get(key, 0) + 1

        return dic
    
    def take_blood(blood_quantity, blood_needed_quantity, blood_in_bank, blood_needed):
            amount_taken = min(blood_quantity[blood_in_bank], blood_needed_quantity[blood_needed])
            blood_quantity[blood_in_bank] -= amount_taken
            blood_needed_quantity[blood_needed] -= amount_taken
            
            return amount_taken
    
    groups = ["O", "A", "B", "AB"]
    blood_quantity = set_quantity(bank)
    blood_needed_quantity = set_quantity(patients)
    
    patients_served = 0

    for group in groups:
        if group == "O" and group in blood_quantity and group in blood_needed_quantity:
            patients_served += take_blood(blood_quantity, blood_needed_quantity, group, group)
        
        elif (group == "A" or group == "B") and group in blood_needed_quantity:
            if group in blood_quantity:
                patients_served += take_blood(blood_quantity, blood_needed_quantity, group, group)

            if blood_needed_quantity[group] > 0 and "O" in blood_quantity and blood_quantity["O"] > 0:
                patients_served += take_blood(blood_quantity, blood_needed_quantity, "O", group)

        if group == "AB" and group in blood_needed_quantity:
            for blood in blood_quantity:
                if blood_quantity[blood] > 0:
                    patients_served += take_blood(blood_quantity, blood_needed_quantity, blood, group)
                
                if blood_needed_quantity[group] == 0:
                    break;

    return f"{patients_served} of {len(patients)} patients served"

# print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]))
# print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]))
# print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]))
# print(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]))
# print(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]))
# print(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]))