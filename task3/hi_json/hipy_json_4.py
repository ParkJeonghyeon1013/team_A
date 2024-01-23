# modify
# insert, delete, modify, get
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

# key_data = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}
#
# json_modify(json_file, ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange'], [1001, 1100])
# json_modify(json_file, key_data, [1001, 1100])
#
# insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}
#
# json_insert(json_file, insert_key_data)
#
# delete_key_data = {'project': {'shot': {'EP0005': None}}}
# json_delete(json_file, delete_key_data)

def json_modify(origin_data, v, word, path, location, chg_data):
    for k, v in v.items():
        path.append(k)
        if word == k:
            if path == location:
                real_path = ''
                for _ in path:
                    real_path += f'[{_}]'
                origin_data[real_path] = chg_data
                return

        if isinstance(v, dict):
            json_modify(origin_data, v, word, path, location, chg_data)

path = []
chg_data = [1001,1100]
json_modify(json_data, json_data, 'frange', path, ['project', 'name', 'datetime', 'shot', 'EP0001', 'EP0001_0010', 'fps', 'frange'], chg_data)

print(json_data)