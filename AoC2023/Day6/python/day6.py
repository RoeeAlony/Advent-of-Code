def calc_race(race_duration, record_distance):
    possibilities = 0

    for speed in range(1, race_duration):
        if speed*(race_duration-speed) > record_distance:
            possibilities += 1
    return possibilities


input_times = [56, 97, 78, 75]
input_dist = [546, 1927, 1131, 1139]


def Calc_all_races(races_times, races_records):
    total = 1
    for time, record in zip(races_times, races_records):
        total *= calc_race(time, record)
    return total


print(Calc_all_races(input_times, input_dist))
