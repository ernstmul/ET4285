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

def divide_lists(list_t):
    list1 = []
    list2 = []

    for element in list_t:
        list1.append(element[0])
        list2.append(element[1])

    return [list1, list2]

#how many from list1 are missing in list2
def count_missing(list1, list2):

    missing = 0
    list1_set = set(list1)
    for element in list1_set:
        if not (element in list2):
            missing += 1

    return missing


def remove_previous(pkt, rec): 

    discarded = []
    while True: 
        if len(rec) != 0 and rec[0][0] < pkt[0]:
            discarded.append(rec.pop(0))
        else:
            break
    

    return discarded

def find_missing(sent, rec, window):
    
    unmatch_sent = []
    unmatch_rec = []
    match_sent = []

    while len(sent) != 0:
        pkt = sent.pop(0)
        match = 0

        unmatch_rec = unmatch_rec + remove_previous(pkt, rec)

        for i in range(window):
            if i < len(rec) and pkt[1] == rec[i][1]:
                rec.pop(i)
                match = 1
                break
        if match == 0:
            unmatch_sent.append(pkt)
        else:
            match_sent.append(pkt)


    unmatch_rec = unmatch_rec + rec

    return [unmatch_sent, match_sent, unmatch_rec]

def print_match_n(pkt, list_t):
    
    for el in list_t:
        if pkt[1] == el[1]:
            print(el)


    print("--")
    print(pkt)

def create_lost_not_list(lost, rec):
    
    return_list = []

    while True:
        if len(lost) == 0 and len(rec) == 0:
            break
        if len(lost) == 0:
            while len(rec) != 0:
                pkt = rec.pop(0)
                return_list.append([pkt[0], 0])
        if len(rec) == 0:
            while len(lost) != 0:
                pkt = lost.pop(0)
                return_list.append([pkt[0], 1])
        if len(rec) != 0 and len(lost) != 0:
            if rec[0][0] < lost[0][0]:
                pkt = rec.pop(0)
                return_list.append([pkt[0], 0])
            else:
                pkt = lost.pop(0)
                return_list.append([pkt[0], 1])

    return return_list

def write_list_to_csv(path, list_t):
    csvfile = open(path, 'wb')

    writer = csv.writer(csvfile)
    writer.writerows(list_t)



start_t = time.time()

csv_path = "/home/nas/simone_scripts/out_csv/server_rec_capture.csv"
server_received = csv_to_list(csv_path)

csv_path = "/home/nas/simone_scripts/out_csv/client_rec_capture.csv"
client_received = csv_to_list(csv_path)

csv_path = "/home/nas/simone_scripts/out_csv/client_sent_capture.csv"
client_sent = csv_to_list(csv_path)

csv_path = "/home/nas/simone_scripts/out_csv/server_sent_capture.csv"
server_sent = csv_to_list(csv_path)

print("Server sent: " + str(len(server_sent)) + ", client received: " + str(len(client_received)) + ", difference: " + str(len(server_sent) - len(client_received)))
print("Client sent: " + str(len(client_sent)) + ", server received: " + str(len(server_received)) + ", difference: " + str(len(client_sent) - len(server_received)))

[srv_snt_t, srv_snt_n] = divide_lists(server_sent)
[cln_rec_t, cln_rec_n] = divide_lists(client_received)
[srv_rec_t, srv_rec_n] = divide_lists(server_received)
[cln_snt_t, cln_snt_n] = divide_lists(client_sent)

#This will take a little uncomment only if you have time
#also passing the check does not give certainty of anything
#ghost_pkts_client = count_missing(cln_rec_n,srv_snt_n)
#ghost_pkts_server = count_missing(srv_rec_n,cln_snt_n)
#if ghost_pkts_client != 0 or ghost_pkts_server != 0:
#    print("There are: " + str(ghost_pkts_client) + " received from the client")
#    print("There are: " + str(ghost_pkts_server) + " received from the server")


#number of packets in which to search
pkt_w = 100


#server -> client
[mis_sent, sent_ok, mis_rec] = find_missing(server_sent, client_received, pkt_w)

#print(len(mis_sent), len(mis_rec))
print("Server -> Client")
print("Number of missing packets: " + str(len(mis_sent)))
print("Number of wrong/duplicated received packets: " + str(len(mis_rec)))

#print_match_n(mis_rec[0], mis_sent)

list_S_C = create_lost_not_list(mis_sent, sent_ok)
#Missing packets?
#print(len(list_S_C))

#Write on csv file
file_name = 'out_csv/pkt_loss_S_C.csv'
write_list_to_csv(file_name, list_S_C)


#client -> server
[mis_sent, sent_ok, mis_rec] = find_missing(client_sent, server_received, pkt_w)

#print(len(mis_sent), len(mis_rec))
print("Client -> Server")
print("Number of missing packets: " + str(len(mis_sent)))
print("Number of wrong/duplicated received packets: " + str(len(mis_rec)))

list_C_S = create_lost_not_list(mis_sent, sent_ok)

#Write on csv file
file_name = 'out_csv/pkt_loss_C_S.csv'
write_list_to_csv(file_name, list_C_S)


duration = time.time() - start_t
print("Duration: " + one_time(duration))






