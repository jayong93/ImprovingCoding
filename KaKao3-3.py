"""
파일 이름을 HEAD, BODY, TAIL 로 분리
분리된 파일 이름을 규칙에 따라 정렬
다시 파일 이름들을 문자열로 합치고 출력
"""

import re
from operator import itemgetter

def separate_name(name):
    patterns = [r'\D+', r'\d+']
    result = []
    for pat in patterns:
        mat_obj = re.search(pat, name)
        result.append(name[:mat_obj.end()])
        name = name[mat_obj.end():]

    if len(name) > 0:
        result.append(name)

    return result

if __name__ == "__main__":
    inputs = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    names = [separate_name(name) for name in inputs]
    print(names)

    # names.sort(key=lambda x: x[0].lower())
    # names.sort(key=lambda x: int(x[1]))
    names.sort(key=lambda x: (x[0].lower(), int(x[1])))

    names = [''.join(name) for name in names]

    print(names)

