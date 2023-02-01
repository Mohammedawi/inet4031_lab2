#!/usr/bin/env python3

file = open('fileprocessor.input', 'r')
lines = file.readlines()

print("\nPrinting out User Data:\n")
for line in lines:
    if line[0] == '#':
        print(f"{line.split(':')[0].strip()[1:]} is skipped because it starts with a hashtag (is commented out)\n")
        continue
    text = line.strip().split(':')
    user = text[0]
    password = text[1]
    userid = text[2]
    groupid = text[3]
    print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")

print("End of User Data\n")

file.close()

