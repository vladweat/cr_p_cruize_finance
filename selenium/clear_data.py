

with open("accounts.txt") as file:
    raw_data = file.readlines()
    raw_data = [x.strip() for x in raw_data]

for data in raw_data:
    mail = data.split("|")[1]
    with open("mails.txt", "a+") as file:
        file.write(mail + "\n")


for data in raw_data:
    twitter = data.split("|")[1].split("@")[0]
    with open("twitters.txt", "a+") as file:
        file.write(twitter + "\n")
