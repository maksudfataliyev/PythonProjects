string = ("######\n"
            "#S##E#\n"
            "# ## #\n"
            "# #  #\n"
            "#   ##\n"
            "######")
index_list = []
for i in range(len(string)):
    if string[i] == " ":
        index_list.append(i)

index_list = [15,22,29,30,31,24,25,18]
print(index_list)

def find_exit(string,count = 0):
    global index_list
    start_index = string.index("S")
    end_index = string.index("E")
    if start_index == end_index:
        return string
    else:
        string = list(string)
        string[start_index], string[index_list[count]] = string[index_list[count]], string[start_index]
        string = "".join(string)
        print(string)
        count = count + 1
        if count >= len(index_list):
            return None
        else:
            find_exit(string,count)
find_exit(string)