from datetime import datetime
import dateutil.parser as dparser
import re

#starttime, endtime in str format
def read_avg_val_customdf(filename, starttime, endtime):
    f = open(filename + '.csv')
    timestamp_l = []
    vals = []
    lines = f.readlines()

    vals_return = []
    index_start = 0
    index_end = 0


    for index, line in enumerate(lines):
        timestamp = re.split('\t', line)[0]
        timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
        #print(timestamp)
        
        #2-column format, append only the val
        timestamp_l.append(timestamp)
        if line[0]==starttime:
            index_start = index
        if line[0]==endtime:
            index_end = index
        #print(vals)
        vals.append(line[1])

    #print(timestamp)   
    #retrieve the most recent data point
    timestamp_latest = timestamp_l[-1]
    print(timestamp_latest)
    timestamp_oldest = timestamp_l[0]
    print(timestamp_oldest)
    #timestamp_latest = datetime.strptime(timestamp_latest, '%Y-%m-%dT%H:%M:%S.%f')
    #timestamp_oldest = datetime.strptime(timestamp_oldest, '%Y-%m-%dT%H:%M:%S.%f')
    time_period_absolute = timestamp_oldest - timestamp_latest
    #time_period = datetime.strptime(timestamp_latest, '%Y-%m-%dT%H:%M:%S.%f') - datetime.strptime(timestamp_latest, '%Y-%m-%dT%H:%M:%S.%f')
    

    #if time_period_absolute > time_period:
        #find latest datapoint
       # offset = timestamp_oldest
        #convert period to str format
        #ie. 6 months

    for i in range(index_start, index_end):
        print(vals[i])  

    avg_vals = vals[index_start:index_end] /(index_end-index_start)
    f.close()
    return avg_vals

if __name__ == "__main__":
    filename = '820_FT_170'
    start_time = '2021-04-16T15:55:54.143'
    end_time = '2021-04-16T15:56:57.15'
    avg_val = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%f') -  datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%f')
    print (avg_val)

    read_avg_val_customdf(filename, start_time, end_time)
