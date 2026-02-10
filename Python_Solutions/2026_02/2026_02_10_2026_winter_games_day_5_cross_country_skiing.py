def time_string_to_seconds(time_string):
    hours, minutes, seconds = time_string.split(":")
    seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    return seconds

def seconds_to_time_string(seconds):
    minutes = int(seconds / 60)
    
    return f"+{minutes}:{seconds - (minutes * 60):02}"

def get_relative_results(results):
    best_result_in_seconds = time_string_to_seconds(results[0])
    differences = ["0"]

    for i in range(1, len(results)):
        result_in_seconds = time_string_to_seconds(results[i])
        diff_in_seconds = result_in_seconds - best_result_in_seconds

        differences.append(seconds_to_time_string(diff_in_seconds))

    return differences

# print(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]))
# print(get_relative_results(["1:00:01", "1:00:05", "1:00:10"]))
# print(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]))
# print(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]))
# print(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]))