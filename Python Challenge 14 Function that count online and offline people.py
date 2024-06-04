#A function that count the number of online and offline people.

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def Online_status_counter(dic):
    count_on=0
    count_off=0
    for key, value in dic.items():
        if value == "online":
            count_on = count_on + 1
        else:
            count_off = count_off + 1   
    print("The number of online person is: {}.".format(count_on))
    print("The number of offline person is: {}.".format(count_off))             

Online_status_counter(statuses)