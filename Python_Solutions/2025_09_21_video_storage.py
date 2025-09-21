from math import floor

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    video_units = ['KB', 'MB', 'GB']
    drive_units = ['GB', 'TB']
    units = {
        'B': 0,
        'KB': 1,
        'MB': 2,
        'GB': 3,
        'TB': 4,
    }

    if not video_unit in video_units:
        return 'Invalid video unit'

    if not drive_unit in drive_units:
        return 'Invalid drive unit'

    return floor((drive_size * 1000 ** units[drive_unit]) / (video_size * 1000 ** units[video_unit]))

# print(number_of_videos(500, "MB", 100, "GB"))
# print(number_of_videos(2000, "B", 1, "TB"))
# print(number_of_videos(2000, "MB", 100000, "MB"))
# print(number_of_videos(500000, "KB", 2, "TB"))
# print(number_of_videos(1.5, "GB", 2.2, "TB"))