# Name: Garrett DesRosiers
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Crime Time
# Term: Winter 2019

import crimetime

first = crimetime.Crime(1, "ROBBERY")
second = crimetime.Crime(2, "ROBBERY")
third = crimetime.Crime(3, "ROBBERY")
crimes = [first, second, third]
assert first == crimetime.Crime(1, "Robbery")
assert not first == second
assert not first == third
assert str(first) == "1\tROBBERY\tNone\tNone\tNone\n"
assert str(second) == "2\tROBBERY\tNone\tNone\tNone\n"
assert str(third) == "3\tROBBERY\tNone\tNone\tNone\n"
assert not crimetime.create_crimes(["1 ROBBERY", "2 ROBBERY", "3 ARSON"]
) == [crimetime.Crime(1, "ROBBERY"), crimetime.Crime(2, "ROBBERY"
), crimetime.Crime(3, "ARSON")]
assert crimetime.create_crimes(["1 ROBBERY", "2 ROBBERY", "3 ARSON"]
) == [crimetime.Crime(1, "ROBBERY"), crimetime.Crime(2, "ROBBERY")]
assert crimetime.create_crimes(["3 ARSON"]) == []
assert crimetime.sort_crimes([third, second, first]) == [first, second, third]
assert crimetime.sort_crimes([third, first]) == [first, third]
assert crimetime.sort_crimes([first, third]) == [first, third]
assert crimetime.get_mode([1, 1, 2, 2]) == 1
assert crimetime.get_mode([1, 2, 3, 3]) == 3
assert crimetime.get_mode([1, 2, 3]) == 1
assert crimetime.find_crime(crimes, 1) == crimetime.Crime(1, "ROBBERY")
assert crimetime.find_crime(crimes, 2) == crimetime.Crime(2, "ROBBERY")
assert crimetime.find_crime(crimes, 4) == None
first.set_time("Sunday", 1, 1)
second.set_time("Monday", 2, 2)
third.set_time("Tuesday", 3, 3)
assert str(first) == "1\tROBBERY\tSunday\tJanuary\t1AM\n"
assert str(second) == "2\tROBBERY\tMonday\tFebruary\t2AM\n"
assert str(third) == "3\tROBBERY\tTuesday\tMarch\t3AM\n"
