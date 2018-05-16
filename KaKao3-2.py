"""
사전을 대문자들로 초기화. 사전은 {문자:index} 형태로 구성
while len(word) > 0:
    start를 0으로 초기화 end를 2로 초기화
    word[start:end]가 사전에 없을때까지 end를 늘림.
    if end == len(word):
        word[start:end]의 색인 출력
        break;
    word[start:end-1] 의 색인을 출력함.
    사전에 {word[start:end]:len(dict)}를 저장    
    word = word[end:]
"""

def init_dict():
    return {chr(c):i+1 for i, c in enumerate(range(ord('A'),ord('Z')+1))}

def compress(word):
    dic = init_dict()
    result = []
    while len(word) > 0:
        start, end = 0, 2
        while end <= len(word) and dic.get(word[start:end]) is not None:
            end += 1
        if end > len(word):
            result.append(dic[word])
            return result
        result.append(dic[word[start:end-1]])
        dic[word[start:end]] = len(dic)+1
        word = word[end-1:]

    return result

if __name__ == "__main__":
    print(compress("TOBEORNOTTOBEORTOBEORNOT"))
