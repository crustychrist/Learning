# Notes
# 1) 12 AM --> 0
# 2) 1 AM to 12 PM --> Do nothing
# 3) 1 PM to 11 PM --> Take Hour + 12. 
# Soln: parse the string in its relevant compoennts. (IE:1st col, 2nd col, 3rd col). Switch case based on time range.


# Military Time init:
mil_hrs = ''
mil_mins = ''
mil_secs = ''
semicolon = ':'
mil_time = ''


# segmenting normal time
time = '3:05:45AM'
time_arr = time.split(':')
time_ampm = time[-2:]
first_col = time_arr[0]
second_col = time_arr[1]
third_col = time_arr[2]
third_col = third_col[0:2]


# Switch Cases
# 12 AM --> 0
if (first_col == "12" and time_ampm == "AM"):
    mil_hrs = '00'
    mil_time = mil_hrs + semicolon + second_col + semicolon + third_col
    print(mil_time)

# remove 
elif((int(first_col) <= 11 and time_ampm == "AM") or (int(first_col) == 12) and time_ampm == "PM" ):
    mil_time = first_col + semicolon + second_col + semicolon + third_col
    print(mil_time)


elif(int(first_col) <= 11 and time_ampm == "PM"):
    time_add = int(first_col) + 12 
    time_add = str(time_add)
    mil_time = time_add + semicolon + second_col + semicolon + third_col
    print(mil_time)
    
