import requests
import os
import hashlib
import json
import urllib.parse
import time

base_path = "/Users/zhouyuan/data"
#base_path = "/data/eth/"

# files = os.listdir(base_path)
# for file in files:
current_file = "2020-12-01"
auth_token = "123.e55fd01e7b4daa383f43cd8516364773.YQ8NuMSGX7ZaG0qyZnOmjA_rpiC2Ogbee0fCDHe.WFQmiQ"
pre_url = "http://pan.baidu.com/rest/2.0/xpan/file?method=precreate&access_token=" + auth_token
upload_url = "https://d.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload&access_token=" + auth_token
up_root = "/apps/eth/eth"


def upload_file(path, real_file, size):
    block_list = []
    block_hash = []
    with open(real_file, "rb") as f:
        while True:
            values = f.read(4194304)
            if values:
                block_list.append(values)
                file_md5 = hashlib.md5(values).hexdigest()
                block_hash.append(file_md5)
                # with open(real_file + "_" + str(len(block_list)), "wb") as wf:
                #   wf.write(values)
                # # print(file_md5)
            else:
                break
        # start_at = real_file.find(base_path)
        # print(start_at)
        up_path = real_file[len(base_path): len(real_file)]
        real_up_path = up_root + up_path
        payload = {'path': real_up_path,
                   'size': size,
                   'isdir': '0',
                   'autoinit': '1',
                   'rtype': '3',
                   'block_list': json.dumps(block_hash)}
        print(payload)
        headers = {
            'Cookie': 'BAIDUID=56BE0870011A115CFA43E19EA4CE92C2:FG=1; BIDUPSID=56BE0870011A115CFA43E19EA4CE92C2; PSTM=1535714267'
        }

        response = requests.request("POST", pre_url, headers=headers, data=payload, files=[])
        # &path=/apps/test/test.jpg&type=tmpfile&uploadid=N1-NjEuMTM1LjE2OS44NDoxNTk2MTExNTczOjQ5MTMzMjgwNjk3MDYxODg3MzQ=&partseq=0
        res_value = response.text.encode('utf8')

        pre_res = json.loads(res_value)
        if pre_res["errno"] == 0:
            time.sleep(0.01)
            upload_id = pre_res["uploadid"]
            for i in range(len(block_list)):
                try_times = 0
                while try_times < 5:
                    try:
                        # real_up_url = upload_url + "&path=" + urllib.parse.quote(real_up_path) + "&type=tmpfile&uploadid=" + upload_id + "&partseq=" + str(i)
                        url_params = {"path": real_up_path, "type": "tmpfile", "uploadid": upload_id, "partseq": i}
                        pp = urllib.parse.urlencode(url_params)
                        print(pp)
                        # print(block_list[i])
                        real_up_url = upload_url + "&" + pp
                        print(real_up_url)
                        param_files = {'file': block_list[i]}
                        response = requests.request("POST", real_up_url, headers=headers, files=param_files, timeout=(5, 100))
                        print(response.text.encode('utf8'))
                        break
                    except Exception as e:
                        print(repr(e))
                        try_times += 1
                        if try_times >= 5:
                            raise e




for root, dirs, files in os.walk(base_path):

    for name in files:
        # global current_file
        if current_file < name:
            abs_path = os.path.join(root, name)
            print(abs_path)
            file_size = os.path.getsize(abs_path)
            print(file_size)
            upload_file(root, abs_path, file_size)
            break

# files = [
#
#
# ]
# headers = {
#   'Cookie': 'BAIDUID=56BE0870011A115CFA43E19EA4CE92C2:FG=1; BIDUPSID=56BE0870011A115CFA43E19EA4CE92C2; PSTM=1535714267'
# }
#
#
# response = requests.request("POST", url, headers=headers, data = payload, files = files)


# print(response.text.encode('utf8'))
