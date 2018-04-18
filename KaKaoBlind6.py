def print_mat(mat):
    for item in mat:
        print(item)
    print('')

def list_to_mat(b_list):
    return list(map(lambda s: list(s), b_list))

def check_to_destroy(mat, x, y):
    window = list(mat[y][x:x+2])
    window += mat[y+1][x:x+2]
    window = list(set(window))
    return len(window) == 1 and ' ' not in window

def get_remove_blocks(mat, w, h):
    removed_list = []
    for y in range(h-1):
        for x in range(w-1):
            if check_to_destroy(mat, x, y):
                removed_list += [(x, y), (x+1, y), (x,y+1), (x+1,y+1)]
    return list(set(removed_list))

def remove_blocks(mat, removed_list):
    for r in removed_list:
        mat[r[1]][r[0]] = ' '

def reconstruct_mat(mat, w, h):
    # 빈칸을 찾아서 위의 것들을 내린다.
    for y in range(1, h):
        for x in range(w):
            if mat[y][x] == ' ':
                for t in range(0, y):
                    mat[y-t][x] = mat[y-(t+1)][x]
                mat[0][x] = ' '

if __name__ == "__main__":
    inputs = [[4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
            [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]]
    
    for i in inputs:
        total_removed_count = 0
        mat = list_to_mat(i[2])
        w, h = i[1], i[0]
        print_mat(mat)

        while True:
            removed_list = get_remove_blocks(mat, w, h)
            if len(removed_list) == 0: break
            total_removed_count += len(removed_list)
            remove_blocks(mat, removed_list)
            reconstruct_mat(mat, w, h)
            print_mat(mat)

        print(total_removed_count)
        print("-"*w*6)
            