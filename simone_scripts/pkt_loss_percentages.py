#!/usr/bin/env python3
import csv
import time

def csv_to_list(path):

    csv_file = open(path, "rb")

    reader = csv.reader(csv_file)

    list_t = []

    for line in reader:
        num_line = [float(line[0]), int(line[1])]
        list_t.append(num_line)


    return list_t


def one_time(t):
    sec = int(t)%60
    minutes = int(t/60)%60
    return str(minutes)+ "." + str(sec) + "m"

def div_list(list_t, delta):
    start_t = list_t[0][0]
    end_t = list_t[-1][0] + delta
    t = start_t
    pkts_in_delta = []
    i = 0
    temp = []
    while len(list_t) != 0 and t < end_t:
        if list_t[0][0] <= t + delta:
            temp.append(list_t.pop(0))
        else:
            pkts_in_delta.append(temp)
            temp = []
            t += delta

    return pkts_in_delta

def obtain_perc_list(list_t):
    
    perc_list = []
    for sub_list in list_t:
        count_lost = 0
        for element in sub_list:
            if element[1] == 1:
                count_lost += 1
        if len(sub_list) != 0:
            perc = float(count_lost)/len(sub_list)
        else:
            perc = 0
        t_start = sub_list[0][0]
        el = [t_start, perc]
        perc_list.append(el)

    return perc_list

def write_list_to_csv(path, list_t):
    csvfile = open(path, 'wb')

    writer = csv.writer(csvfile)
    writer.writerows(list_t)


#Server -> client

file_d = "/home/nas/simone_scripts/out_csv/pkt_loss_S_C.csv"

S_C_list = csv_to_list(file_d)

delta = 1.000 #s

#dividing the list in deltas
divided_S_C = div_list(S_C_list, delta)

#computing the packet loss percentage of each delta
perc_list = obtain_perc_list(divided_S_C)

file_d = "/home/nas/simone_scripts/out_csv/pkt_loss_perc_S_C.csv"

write_list_to_csv(file_d, perc_list)


#Client -> server

file_d = "/home/nas/simone_scripts/out_csv/pkt_loss_C_S.csv"

C_S_list = csv_to_list(file_d)

#dividing the list in deltas
divided_C_S = div_list(C_S_list, delta)

#computing the packet loss percentage of each delta
perc_list = obtain_perc_list(divided_C_S)

file_d = "/home/nas/simone_scripts/out_csv/pkt_loss_perc_C_S.csv"

write_list_to_csv(file_d, perc_list)
























