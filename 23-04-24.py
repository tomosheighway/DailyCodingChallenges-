"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

def min_rooms(times):
    start_times = sorted(time[0] for time in times)  
    end_times = sorted(time[1] for time in times)
    #print(start_times)
    #print(end_times)

    required_rooms = 0
    start_num = 0 
    end_num = 0 

    while start_num < len(times): 
        if start_times[start_num] < end_times[end_num]:
            required_rooms +=1
        else: 
            end_num +=1
        start_num +=1

    return required_rooms

print("Min rooms required is: ", min_rooms([(30, 75), (0, 50), (60, 150)]))  # Ans 2
print("Min rooms required example 2 is: ", min_rooms([(10,40) , (45, 75), (90, 200)])) # Ans 1 