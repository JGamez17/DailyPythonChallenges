# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)

sender_counts = {}

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    email = line.find("From")
    person = line[email:]
    wds = person.split()
    # extract the senders email address
    sender = wds[1]
    sender_counts[sender] = sender_counts.get(sender, 0) + 1
    # print(sender)
most_prolific_sender = None
max_count = 0

for sender, count in sender_counts.items():
    if count > max_count:
        most_prolific_sender = sender
        max_count = count
print(most_prolific_sender, max_count)
