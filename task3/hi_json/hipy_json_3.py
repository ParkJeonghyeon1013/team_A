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




delete_key_data = {'project': {'shot': {'EP0005': None}}}
def json_delete(file, data_delete):
    return



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
