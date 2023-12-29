

#include <iostream>
#include <vector>

int CalcRace(int race_duration, int record_distance)
{
    int possibilities = 0;

    int min_speed_to_break_record = (record_distance / (race_duration - 1)) + 1;

    for (int speed = min_speed_to_break_record; speed < race_duration; ++speed)
    {
        if (speed * (race_duration - speed) > record_distance)
        {
            possibilities++;
        }
    }

    return possibilities;
}

int CalcAllRaces(const std::vector<int> &race_times, const std::vector<int> &race_records)
{
    int total = 1;

    for (size_t i = 0; i < race_times.size(); ++i)
    {
        total *= CalcRace(race_times[i], race_records[i]);
    }

    return total;
}

int main()
{
    std::vector<int> input_times = {56, 97, 78, 75};
    std::vector<int> input_dist = {546, 1927, 1131, 1139};

    std::cout << "Total possibilities: " << CalcAllRaces(input_times, input_dist) << std::endl;

    return 0;
}
