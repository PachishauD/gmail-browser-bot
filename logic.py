import random
import time
import threading

from src.utilities.select_message_for_sending import read_file_line_by_line

sender = ["a", "b", "c"]
reciver = ["1", "2", "3", "4", "5", "6", "7", "8"]

def match(x, y):
    print(sender[x], reciver[y])

def watching():
    print("watching....")
    time.sleep(5)

def one(x):
    while True:
        num_reciver = len(reciver)
        if num_reciver == 0:
            watching()
        else:
            print(num_reciver)
            num = random.randrange(0, num_reciver)
            match(x, num)
            reciver.remove(reciver[num])
            watching()

def main():
    # num_sender = len(sender)
    # num_reciver = len(reciver)
    # for i in range(0, num_sender):
    #     time.sleep(1)
    #     threading.Thread(target=lambda:one(x=i)).start()
    temps = print(len(read_file_line_by_line("temp.txt")))
    print(temps)


if __name__ == "__main__":
    main()