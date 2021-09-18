
Command = 0
store = open("List.txt", "a+")
store.seek(0)
Data = store.readlines()
print(Data)
# 1.ADD
# 2.MARK
# 3.Display
# 4.EXIT
while Command != 4:
    Command = int(input("Hey there you have for choices : \n1.Add Task \n2.Mark Task As Done \n3.Display Tasks \n4.Save and Exit\n"))
    if Command == 1:
        item = input("Please add your Task")
        item = item + "\n"
        Data.append(item)
        print("Task added : ", item)
        store.truncate(0)
        store.writelines(Data)
        # store.write("\n")


    elif Command == 2:
        print("Choose the task number to be removed:")
        for i in range(len(Data)):
            print(str(i+1),":",Data[i],end="")
        itemNo = int(input())
        if len(Data)+1 > itemNo > 0:
            print(Data[itemNo-1],"is Removed from the list")
            # print(Data[itemNo - 1])
            Data.remove(Data[itemNo - 1])
            store.truncate(0)
            store.writelines(Data)
        else:
            print("Wrong INPUT")
    elif Command == 3:
        print("Here are your tasks :")
        for i in range(len(Data)):
            print(str(i+1),":",Data[i],end="")

store.close()