# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
hour = None

for line in handle:
    if 'From ' in line:
        sender_line = line.split()
        send_time = sender_line[5]
        send_hour = send_time[:2] # gets hour sent
        di[send_hour] = di.get(send_hour, 0) + 1
        
for key in sorted(di.keys()):
    print(key, di[key])
        
