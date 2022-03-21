# Name: Garrett DesRosiers
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Crime Time
# Term: Winter 2019

class Crime:


    def __init__(self, crime_id: int, category: str):
        self.crime_id = crime_id
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None


    def __eq__(self, other):
        return (self.crime_id == other.crime_id)


    def __repr__(self):
        return ("{0}\t{1}\t{2}\t{3}\t{4}\n".format(
        self.crime_id, self.category, self.day_of_week,
        self.month, self.hour))


    def set_time(self, day_of_week: str, month: int, hour: int):
        hours = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", 
        "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", 
        "7PM", "8PM", "9PM", "10PM", "11PM"]
        months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]
        self.day_of_week = day_of_week
        self.month = months[month - 1]
        self.hour = hours[hour]


def main():
    cp = open("crimes.tsv", "r", encoding = "utf-8")
    cp.readline()
    crimelines = cp.readlines()
    cp.close()
    tp = open("times.tsv", "r", encoding = "utf-8")
    tp.readline()
    timelines = tp.readlines()
    tp.close()
    crimes = create_crimes(crimelines)
    crimes = sort_crimes(crimes)
    update_crimes(crimes, timelines)
    rp = open("robberies.tsv", "w")
    rp.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")
    for i in crimes:
        rp.write(str(i))
    rp.close()
    days = [j.day_of_week for j in crimes]
    months = [k.month for k in crimes]
    hours = [x.hour for x in crimes]
    day_mode = get_mode(days)
    month_mode = get_mode(months)
    hour_mode = get_mode(hours)
    print("NUMBER OF PROCESSED ROBBERIES: {0}".format(len(crimes)))
    print("      DAY WITH MOST ROBBERIES: {0}".format(day_mode))
    print("    MONTH WITH MOST ROBBERIES: {0}".format(month_mode))
    print("     HOUR WITH MOST ROBBERIES: {0}".format(hour_mode))
    

def create_crimes(lines: list):
    crimes = []
    for i in range(len(lines)):
        crimelist = lines[i].split()
        if crimelist[1] == "ROBBERY" and Crime(
        int(crimelist[0]), crimelist[1]) not in crimes:
            crimes.append(Crime(int(crimelist[0]), crimelist[1]))
    return crimes


def sort_crimes(crimes: list):
    lowest = None
    swap = None
    flag = False
    index = None
    for i in range(len(crimes)):
        lowest = crimes[i]
        for j in range(i, len(crimes)):
            if crimes[j].crime_id < lowest.crime_id:
                lowest = crimes[j]
                flag = True
        if flag:
            index = crimes.index(lowest)
            swap = crimes[i]
            crimes[i] = lowest
            crimes[index] = swap
        flag = False
    return crimes
        

def update_crimes(crimes: list, lines: list):
    for i in lines:
        line = i.split()
        crime = find_crime(crimes, int(line[0]))
        if str(type(crime))[1:17] != "class 'NoneType'" :
            crime.set_time(line[1], int(line[2][:2]), int(line[3][:2]))

        
def find_crime(crimes: list, crime_id: int):
    lower = 0
    higher = len(crimes) - 1
    index = None
    flag = False
    crime = None
    while (lower <= higher and not flag):
        index = (lower + higher) // 2
        if crimes[index].crime_id < crime_id:
            lower = index + 1
        elif crimes[index].crime_id > crime_id:
            higher = index - 1
        else:
            crime = crimes[index]
            flag = True
    return crime


def get_mode(l: list):
    mode = None
    occurs = 0
    for i in l:
        if l.count(i) > occurs:
            occurs = l.count(i)
            mode = i
    return mode


if __name__ == "__main__":
    main()
