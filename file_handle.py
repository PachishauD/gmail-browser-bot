sellers = ["a", "b", "c"]

for seller in sellers:
    filename = "./assets/" + seller + ".txt"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(seller)