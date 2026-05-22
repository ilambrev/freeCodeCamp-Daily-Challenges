def get_meeting_time(availability):
    def find_person_free_hours(person_availability):
        free_hours = []

        for interval in person_availability:
            free_hours += ([h for h in range(interval[0], interval[1])])
        
        return sorted(free_hours)
    
    def find_all_free_hours(availability):
        all_persons_free_hours = []

        for person_availability in availability:
            free_hours = find_person_free_hours(person_availability)
            all_persons_free_hours.append(free_hours)
        
        return all_persons_free_hours
    
    def find_first_shared_free_hour(all_persons_free_hours):
        first_shared_free_hour = -1

        for free_hour in range(24):
            is_free_for_all = True
        
            for person_free_hours in all_persons_free_hours:
                if not free_hour in person_free_hours:
                    is_free_for_all = False
                    break
        
            if is_free_for_all:
                first_shared_free_hour = free_hour
                break
        
        return first_shared_free_hour
        
    all_persons_free_hours = find_all_free_hours(availability)
    
    first_shared_free_hour = find_first_shared_free_hour(all_persons_free_hours)

    return first_shared_free_hour if first_shared_free_hour > -1 else "None"

# print(get_meeting_time([[[10, 12], [15, 16]], [[11, 14], [15, 16]]]))
# print(get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]]))
# print(get_meeting_time([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]]))
# print(get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]]))
# print(get_meeting_time([[[1, 3], [4, 6], [8, 10], [20, 23]], [[15, 16], [17, 18], [19, 22], [23, 24]], [[14, 16], [17, 23]], [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]]))