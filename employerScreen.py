megalist = list()
with open("employers.txt", "r", encoding="utf8") as employers:
    for x in employers:
        megalist.append(x.replace("\t", " ").split(" "))
print("yeah it executed idk")
with open("internships.txt", "w", encoding="utf8") as intern:
    for y in megalist:
        if "CSE" in y or "CSE," in y:
            if y[-2] == "Yes":
                for z in y: 
                    print(z, end=' ')
                    intern.write(z + " ")
                #intern.write("\n")

