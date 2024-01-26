import pprint

json_data = {
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

############################################ 적은 인자 받아서 modify ############################################################################
print('-'*100)
print('방법 1 - 편한 방법. 키값으로')

# def json_modify_easy(j_data, path: list, c_data) -> None:
#     try:
#         if isinstance(j_data, dict):
#             for k1, v1 in j_data.items():
#                 if k1 == path[0]: #
#                     if len(path) == 1: # 최종 키값 도달하면 데이터 바꾸기
#                         j_data[k1]= c_data
#                         return
#                     json_modify_easy(v1, path[1:], c_data) # 0번 키값 찾으면 그거 빼고 return
#     except IndexError as err:
#         print(err)
#         return
#
#
# path = []
# chg_data = [1001,1,200]
# json_modify_easy(json_data, ['project','shot','EP0002','EP002_0010','author'], chg_data)
# print('1차 >> ', json_data)
#
# chg_data = '안녕'
# json_modify_easy(json_data, ['project','shot','EP0001','EP0001_0010'], chg_data)
# print('2차 >> ', json_data)
#
# chg_data = {'fps': 24, 'frange': [1123], 'author': 'person'}
# json_modify_easy(json_data, ['project','shot','EP0002','EP002_0010'], chg_data)
# print('3차 >> ', json_data)

########################################## 주소값 받아오는 메서드 ##################################
print('-'*100)
print('방법 2를 위한 주소값 받아오기')
#
# def get_path(data, path, key, val):
#     for k1, v1 in data.items():
#         path.append(k1)
#         if key == k1 and val == v1:
#             # print(path)
#             return
#         if isinstance(v1, dict):
#             get_path(v1, path, key, val)
#     # return
#
# path = []
# a = get_path(json_data, path, 'EP003_0010',  {'fps': 24,'frange': [1001, 1050], 'author': 'adsfnon'})
# print(path)





##########################################  list 살린 방법 - 거쳐가는걸 다 적어줘야 함. 즉, 귀찮.. 주소 얻어오는 메소드를 하나 만든다..##################################
print('-'*100)
print('방법2 - list 살리기 ')
# def json_modify(d, path, location, chg_data):
#     word = location[-1]
#     for k, v in d.items():
#         path.append(k)
#         if location == path:
#             if word == k:
#                 if isinstance(v, dict) or isinstance(v, list) or isinstance(v, str):
#                     # print(real_path, '탈출')
#                     d[k] = chg_data
#                     return
#
#         if isinstance(v, dict):
#             json_modify(v, path, location, chg_data)
#
# chg_data = [1001,1200,351]
# json_modify(json_data, [], ['project', 'name', 'datetime', 'shot', 'EP0001', 'EP0001_0010', 'fps', 'frange', 'author', 'filepath', 'hipfile', 'nkfile', 'EP0002', 'EP002_0010', 'fps', 'frange'], chg_data)
# print(f'{chg_data}---------{json_data}')
# ddd = ['[project][name][datetime][shot][EP0001][EP0001_0010][fps][frange][author][filepath][hipfile][nkfile][EP0002][EP002_0010][fps][frange][author]']
# # print(json_data.get('project').get('name').get(''))
#
# chg_data = [1001,1200]
# json_modify(json_data, [], ['project', 'name', 'datetime', 'shot', 'EP0001', 'EP0001_0010', 'fps', 'frange'], chg_data)
# print(f'{chg_data} ------ {json_data}')


#################################### dict 형태로 데이터 받아서 modify 하기 #################################################
print('-'*100)
print('방법3 - get dict type data / modify')

def json_modify_dict(d, path: dict, chg_data):
    print(d)
    for d_key, d_val in d.items(): # json data에서 key, val 분리
        for p_key, p_val in path.items(): # path dict에서 key val 분리
            # print(p_val)
            if d_key == p_key: # 두 dict의 키값 같으면
                # print(d_key, p_key)
                # print(p_val,'\n')
                if p_val is None: # path dict의 목적지 키값은 None 인거 이용해서 도착여부 잡기
                    d[d_key] = chg_data # 데이터 바꾸기
                    print(chg_data, '값 바꾸기')
                    return
                json_modify_dict(d_val, p_val, chg_data)
    return d


key_data1 = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}
c_data1 = [1200,51200321]

# pprint.pprint(json_data)
json_modify_dict(json_data, key_data1, c_data1)
pprint.pprint(json_data)

key_data2 = {'project': {'shot': {'EP0002': {'EP002_0010': {'author': None}}}}}
c_data2 = 'pakjdlfkjslkjdf'

# pprint.pprint(json_data)
a= json_modify_dict(json_data, key_data2, c_data2)
pprint.pprint(json_data)
# print(a)





########################################## json 보여주기 ##################################
# 오마이 모듈있었음... pprint ... 그래도 ㄱ재귀로 만들어보고싶음.
print('-'*100)
print('json 파일 레이어별로 보여주기')

# def show_layer(d):
#     if isinstance(d, dict):
#         for k1,v1 in d.items():
#             if isinstance(v1, dict):
#                 print(f'{k1}')
#                 for k2,v2 in v1.items():
#                     if k2 != 'shot':
#                         print('\t'*1, f'{k2} : {v2}')
#
#                     else:
#                         print('\t'*1, f'{k2}')
#                         if isinstance(v2, dict):
#                             for k3, v3 in v2.items():
#                                 print('\t'*2, f'{k3}')
#                                 if isinstance(v3, dict):
#                                     for k4, v4 in v3.items():
#                                         print('\t'*3, f'{k4}')
#                                         if isinstance(v4, dict):
#                                             for k5, v5 in v4.items():
#                                                 if isinstance(v5, dict):
#                                                     print('\t'*5, f'{k5}')
#
#                                                     for k6, v6 in v5.items():
#                                                         print('\t'*6, f'{k6} : {v6}')
#                                                     break
#
#                                                 print('\t'*5, f'{k5} : {v5}')
#
#     else:
#         return

# show_layer(json_data)

############################################################################################################################
##### 재귀로 딕셔너리 출력하기 ######
print('-'*100)
print('재귀 사용해서 json 파일 레이어별로 보여주기')
# def re_show_layer(idx, d):
#     if isinstance(d, dict):
#         for k1, v1 in d.items():
#             print('\t'*idx, k1)
#             idx += 1
#             print(idx)
#
#
#             if isinstance(v1, dict) :
#                 for k2, v2 in v1.items():
#                     print('\t'*idx, k2,' : ', v2)
#                     idx += 1
#                     re_show_layer(idx, v1)
#
#
#     else:
#         return
#
# re_show_layer(json_data)

###############################################delete lsit 사용해서#################################
def json_delete(j_data, path: list) -> None:
    # if isinstance(j_data, dict): # json data 레이어 타고타고 들어감. dict 형태면 item으로 k1, v1으로 분리
        for k1, v1 in j_data.items():
            # print(k1, v1 )
            # if len(path) == 0: # path list가 비어있으면 탈출
            #     return
            if k1 == path[0]: # json data의 key값이 path list에 있는 0번 데이터(목적지 키값)와 같은지 확인
                if len(path) == 1: # path list의 길이가 최종 도달해야 하는 키값만 남아있어서 1이 되면, 데이터 삭제
                    j_data.pop(k1)
                    print(len(path),'탈출')
                    return # 탈출
                json_delete(v1, path[1:]) # 재귀 - 0번 키값 찾으면 찾은 키값 제외한 경로를 path list 인자값으로 넣어주기


# pprint.pprint(json_data)
# print(json_delete(json_data, ['project','shot','EP0002','EP002_0010','author']))
pprint.pprint(json_data)
# print(deltem(json_data))
# pprint.pprint(deltem(json_data))



#####################################0126 ver

print('\n\n 0126 dict fin.. 여기까지가... 끝인가보오..')
def json_modify_dict0126(d, path: dict, chg_data):
    for d_k, d_v in d.items(): # dict 값 key / val
        for p_k, p_v in path.items(): # path 값 key / val
            if p_v is None:
                print(d[d_k])
                print('modify')
                return
            if isinstance(d_v, dict) and p_k == d_k: # dict의 val 값이 dict 형태고, 서로 키값 같으면
                print(d_v, p_v)
                json_modify_dict0126(d_v, p_v, chg_data )


key_data1 = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}
c_data1 = [1200,51200321]

# pprint.pprint(json_data)
json_modify_dict0126(json_data, key_data1, c_data1)
pprint.pprint(json_data)

key_data2 = {'project': {'shot': {'EP0002': {'EP002_0010': {'author': None}}}}}
c_data2 = 'pakjdlfkjslkjdf'