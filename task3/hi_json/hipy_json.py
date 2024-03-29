import re
import pathlib
import os
import pprint
import json
# json_file = {
#     'project': {
#         'name': 'mermaid',
#         'datetime': '2024-02-01',
#         'shot': {
#             'EP0001': {
#                 'EP0001_0010': {
#                     'fps': 24,
#                     'frange': [1001, 1100],
#                     'author': ['anon', 'aa'],
#                     'filepath': {
#                         'hipfile': '/home/rapa/down',
#                         'nkfile': '/home/rapa/nk',
#                     }
#                 }
#             },
#             'EP0002': {
#                 'EP002_0010': {
#                     'fps': 24,
#                     'frange': [1001, 1050],
#                     'author': 'anon',
#                 }
#             },
#         }
#     }
# }
class Json_Parser:

    def __init__(self,s_path):
        self.__json_data = None
        self.__s_path = s_path

    @property
    def json_data(self):
        return self.__json_data
    @json_data.setter
    def json_data(self,val):
        self.__json_data = val


    @property
    def s_path(self):
        return self.__s_path
    @s_path.setter
    def s_path(self,val):
        self.__s_path = val


    def get_json_path(self):
        return pathlib.Path(self.s_path).as_posix()

    # @staticmethod
    def open_file(self) -> dict:
        # print(self.get_json_path())
        with open(self.get_json_path(),'r') as fp:
            self.json_data = json.load(fp)
            # print(self.json_data)
        return self.json_data


    def json_delete(self, dic: dict) -> list:
        note = []
        for k, v in dic.items():
            if isinstance(v, dict):
                note.append(f"{k}: {self.json_delete(v)}")
            else:
                note.append(f"{k}: {v}")

        res =  ', '.join(note)
        dell = re.sub(r'project:|shot:|EP0002', '',res)
        return dell


    def json_insert(self, data: dict, in_data: dict):
        for k, v in data.items():
            if k != 'shot':
                if isinstance(v, dict):
                    if not isinstance(v, dict):
                        return
                    self.json_insert(v, in_data)
            else:
                data[k].update(in_data)
                # self.json_insert(v, in_data)

        return data


    def json_modify(self, d, path: dict, chg_data):
        for d_k, d_v in d.items():  # dict 값 key / val
            for p_k, p_v in path.items():  # path 값 key / val
                if p_k == d_k and p_v is None:  # 서로 키값이 같고, p_v가 none이면
                    d[d_k] = chg_data
                    return
                if isinstance(d_v, dict) and p_k == d_k:  # dict의 val 값이 dict 형태고, 서로 키값 같으면
                    self.json_modify(d_v, p_v, chg_data)
        return d


    def json_get(self,data,getval):
        lst = []
        for key, value in data.items():
            if key == getval:
                lst.append(value)
            elif isinstance(value,dict):
                # print(value,'\n')
                result = self.json_get(value,getval)
                lst.extend(result)

        res = ''.join(lst)
        return res

if __name__ == '__main__':
    insert_key_data = {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}
    modify_key_data = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}
    c_data = [1200,51200321]
    key_data2 = {'project': {'shot': {'EP0002': {'EP002_0010': {'author': None}}}}}
    c_data2 = 'pakjdlfkjslkjdf'
    delete_key_data = {'project': {'shot': {'EP0005': None}}}
    dic = {'1':'modify',
           '2':'delete',
           '3':'insert',
           '4':'get',}
    f = Json_Parser('/home/rapa/clone/team_A/task3/hi_json/json_file.json')
    print(dic)
    a = input("어떤 실행을 하시겠습니까? = (ex : modify,delete,insert,get)\n>> ")

    data = f.open_file()
    if a == '1':
        print(f'Json Parser [{dic[a]}]를 실행합니다.\n{modify_key_data}를 {c_data}로 바꿉니다.\n')
        pprint.pp(f.json_modify(f.open_file(), modify_key_data, c_data))
    elif a == '2':
        pprint.pp(f.json_delete(data))
    elif a == '3':
        pprint.pp(f.json_insert(f.open_file(), insert_key_data), sort_dicts=False)
    elif a == '4':
        pprint.pp((f.json_get(f.open_file(), 'datetime')))




