json_file = {
    'project': {
        'name': 'mermaid',
        'datetime': '2024-02-01',
        'shot': {
            'EP0001': {
                'EP0001_0010': {
                    'fps': 24,
                    'frange': [1001, 1100],
                    'author': ['anon', 'aa'],
                    'filepath': {
                        'hipfile': '/home/rapa/down',
                        'nkfile': '/home/rapa/nk',
                    }
                }
            },
            'EP0002': {
                'EP002_0010': {
                    'fps': 24,
                    'frange': [1001, 1050],
                    'author': 'anon',
                }
            },
        }
    }
}

key_data = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}
def json_modify(file, data_before, data_after):
    return




def json_insert(file, data_insert):
    return





delete_key_data = {'project': {'shot': {'EP0005': None}}}
def json_delete(file, data_delete):
    return


# def json_get(file,data_get:str):
#     if isinstance(file,dict):#인자로 넣은 파일이 디렉토리면 for문 실행
#         for key,value in file.items():#인자의 key,value
#             # print(file.values())
#             if isinstance(value,list):
#                 # print(type(value))
#                 for i in range(len(value)):
#                     # print('리스트안의 값',value[i],'값의 타입 ',type(value[i]))
#                     if str(value[i]) == str(data_get):
#                         print(value[i],'이거다',value,'안에있어요')
#                         return value[i]
#             else: json_get(value,data_get)

import json
#
# def json_get(file, data_get):
#     if isinstance(file, dict):
#         for key, value in file.items():
#             if str(key) == data_get:
#                 print(value, '가 안에 있어요')
#             elif isinstance(value,dict):
#                     result = json_get(value, data_get)
#                     if result is not None:
#                         return result
#     return value
#     # elif isinstance(file, list):
#     #     for idx in file:
#     #         if str(idx) == str(data_get):
#     #             print(idx, '이 값은', file, '안에 있어요')
#

def json_get(file:dict,data_get):
    data = []
    for key, value in file.items():
        if key == data_get:
            data.append(value)
        elif isinstance(value,dict):
            # print(value,'\n')
            result = json_get(value,data_get)
            data.extend(result)
    return data
print(json_get(json_file,'EP002_0010'))




    # return None
#
# print(json_get(json_file,'/home/rapa/nk'))

# json_delete(json_file, delete_key_data)
# # insert, delete, modify, get
# json_modify(json_file, ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange'], [1001, 1100])
# json_modify(json_file, key_data, [1001, 1100])
#
# insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}
#
# json_insert(json_file, insert_key_data)
