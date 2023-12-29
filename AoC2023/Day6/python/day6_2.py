def Calc_race(race_duration, record_distance):
    possibilities = 0

    for speed in range(1, race_duration):
        if speed*(race_duration-speed) > record_distance:
            possibilities += 1
    return possibilities


input_singlerace_time = 56977875
input_singlerace_dist = 546192711311139


print(Calc_race(input_singlerace_time, input_singlerace_dist))
