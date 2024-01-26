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
                        'hipfileapa/': '/home/rapa/down',
                        'nkfile': '/home/rnk',
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
# delete_key_data = {'project': {'shot': {'EP0005': None}}}
# json_delete(json_file, delete_key_data)
#
# del_key_data = ['project', 'shot', 'EP0002']
# del_key_data = ['project', ['shot', ['EP0002]]]
# del_key_data = {'project': {'shot': {'EP0002': None}}}

# recur(json_data, del_key_data)
import re


import pprint
import re
def deltem(json_data: dict):
    note = []
    for k, v in json_data.items():
        if isinstance(v, dict):
            note.append(f"{k}: {deltem(v)}")
        else:
            note.append(f"{k}: {v}")

    res =  ', '.join(note)
    dell = re.sub(r'project:|shot:|EP0002', '',res)
    return dell

# 결과 출력
pprint.pprint(deltem(json_data))
