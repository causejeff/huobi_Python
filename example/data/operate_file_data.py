import os

base_path = "/Users/zhouyuan/data"
#base_path = "/data/eth/"
data_path = "/Users/zhouyuan/data1"

def operate_file(file_path):
    new_path = data_path + file_path[len(base_path): len(file_path)]
    print(new_path)
    index = file_path.rfind("/")
    print(index)
    file_name = file_path[index + 1:]
    print(file_name)
    new_index = new_path.rfind("/")
    try:
        print(new_path[0: new_index])
        os.makedirs(new_path[0: new_index], mode=0o770)
    except FileExistsError as e:
        repr(e)
        pass
    with open(file_path, "r") as f:
        lines = f.readlines()
        last = lines[0]
        last_time = last.split(",")[0].split(" ")[1]
        last_date = last.split(",")[0].split(" ")[0]
        with open(new_path, "w+") as wf:
            for i in range(1, len(lines)):
                values = lines[i].split(",")
                date_strs = values[0].split(" ")
                if last_time != date_strs[1] or i == len(lines) - 1:
                    if last_date == file_name:
                        wf.write(last)
                last = lines[i]
                last_time = date_strs[1]
                last_date = date_strs[0]





for root, dirs, files in os.walk(base_path):
    for name in files:
        # global current_file
        abs_path = os.path.join(root, name)
        print(abs_path)
        operate_file(abs_path)
