import re

def get_played_time(start_t_str, end_t_str):
    start_t = [int(t) for t in start_t_str.split(':')]
    end_t = [int(t) for t in end_t_str.split(':')]

    return (end_t[0]-start_t[0])*60+(end_t[1]-start_t[1])

def get_played_code(played_time, src_codes):
    if len(src_codes) > played_time:
        return src_codes[:played_time]
    elif len(src_codes) == played_time:
        return src_codes
    else:
        played_code = src_codes*(played_time//len(src_codes))
        played_code += src_codes[:played_time%len(src_codes)]
        return played_code

def is_matched_codes(memory_code, info):
    played_code = get_played_code(info[0], info[2])
    index = played_code.find(memory_code)
    
    if index < 0:
        return False

    if index + len(memory_code) > len(played_code):
        if played_code[index + len(memory_code)] == "#":
            return False

    return True

def find_original_music(music_info):
    memory_code = music_info[0]
    info_list = [info.split(',') for info in music_info[1]]
    info_list = [[get_played_time(info[0], info[1]), info[2], info[3]] for info in info_list] # [[재생시간, 이름, 악보]]

    matched_codes = [info for info in info_list if is_matched_codes(memory_code, info)]
    
    if len(matched_codes) > 0:
        matched_codes.sort(key=lambda x: x[0], reverse=True)
        return matched_codes[-1][1]
    
    return "(None)"

if __name__ == "__main__":
    inputs = [("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB",
"13:00,13:05,WORLD,ABCDEF"]), ("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B",
"04:00,04:08,BAR,CC#BCC#BCC#B"]), ("ABC", ["12:00,12:14,HELLO,C#DEFGAB",
"13:00,13:05,WORLD,ABCDEF"])]

    outputs = [find_original_music(info) for info in inputs]

    print(outputs)

