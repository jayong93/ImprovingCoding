# 입력을 분해해서 (완료 시각, 걸린 시간)으로 반환
def preprocess_input(inputs):
    splited_inputs = list(map(lambda i: i.split(), inputs))
    return list(map(lambda i: string_to_second(i[1],i[2]), splited_inputs))

def string_to_second(end_t, elapsed_t):
    splited_end_t = end_t.split('.')
    end_hms, end_ms = splited_end_t[0], splited_end_t[1]
    total_end_ms = int(end_ms)
    for i, t in enumerate(end_hms.split(':')):
        total_end_ms += int(t)*(60**(2-i))*1000
    elapsed_ms = int(float(elapsed_t[:-1])*1000)
    return (total_end_ms, elapsed_ms)

if __name__ == '__main__':
    inputs = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
    end_elapsed_times = preprocess_input(inputs)
    start_times = list(map(lambda x: x[0]-x[1]+1, end_elapsed_times))
    print(end_elapsed_times, start_times)

    # 각 완료시간마다 1초당 얼마나 많이 처리했는지 찾아냄
    process_nums_per_sec = []
    for i, times in enumerate(end_elapsed_times):
        process_num_in_sec = next((i for i, x in enumerate(start_times) if x >= times[0] + 1000), len(start_times))
        process_nums_per_sec.append(process_num_in_sec)
        start_times = start_times[1:]

    print(process_nums_per_sec)
    print(max(process_nums_per_sec))
