def union_set(s1, s2):
    unique_elms = set(s1) | set(s2)
    new_set = []
    for e in unique_elms:
        a = [s_item for s_item in s1 if s_item == e]
        b = [s_item for s_item in s2 if s_item == e]
        if len(a) > len(b):
            new_set += a
        else:
            new_set += b
    return new_set

def cross_set(s1, s2):
    unique_elms = set(s1) | set(s2)
    new_set = []
    for e in unique_elms:
        a = [s_item for s_item in s1 if s_item == e]
        b = [s_item for s_item in s2 if s_item == e]
        if len(a) < len(b):
            new_set += a
        else:
            new_set += b
    return new_set

def check_alpha_num(c):
    return ('a' <= c <= 'z' or 'A' <= c <= 'Z')

def transform_input(ipt):
    return [(a+b).lower() for a, b in zip(ipt[:-1], ipt[1:]) if check_alpha_num(a) and check_alpha_num(b)]

def get_similarity(s1, s2):
    return int((len(cross_set(s1,s2))/len(union_set(s1,s2)))*65536)

if __name__ == "__main__":
    post_input = transform_input('aa1+aa2')
    post_input2 = transform_input('AAAA12')
    print(post_input)
    print(get_similarity(post_input, post_input2))