from functools import reduce

def time_to_tuple(t):
    return tuple(map(lambda x: int(x), str(t).split(":")))


def tuple_to_time(t):
    return "%02d:%02d" % (t[0], t[1])


def add_time(t, du):
    nt = t[1]+du
    if nt >= 60:
        return (t[0]+(nt//60), nt % 60)
    elif nt < 0:
        return (t[0]+(nt//60), 60+nt)
    return (t[0], nt)


def get_bus_time_list(n, t):
    return [add_time((9, 0), t*i) for i in range(n)]


def filter_n(func, count, iterable):
    return (item for i, item in enumerate(iterable) if func(item) and i<count)


def get_passenger_list_on_bus(bus_time_list, m, crew_list):
    for bt in bus_time_list[:-1]:
        filtered = list(filter_n(lambda x: x <= bt, m, crew_list))
        crew_list = crew_list[len(filtered):]
    return list(filter(lambda x: x <= bus_time_list[-1], crew_list))


def main(params):
    n = params['n']
    t = params['t']
    m = params['m']
    crew_list = params['time_table']
    crew_list = sorted(list(map(time_to_tuple, crew_list)))
    bus_time_list = get_bus_time_list(n, t)
    pass_list = get_passenger_list_on_bus(bus_time_list, m, crew_list)
    if len(pass_list) < m:
        return tuple_to_time(bus_time_list[-1])
    else:
        return tuple_to_time(add_time(pass_list[-1], -1))


if __name__ == "__main__":
    n = [1, 2, 2, 1, 1, 10]
    t = [1, 10, 1, 1, 1, 60]
    m = [5, 2, 2, 5, 1, 45]
    time_table = [["08:00", "08:01", "08:02", "08:03"], ["09:10", "09:09", "08:00"], ["09:00", "09:00", "09:00", "09:00"], ["00:01", "00:01", "00:01", "00:01", "00:01"], [
        "23:59"], ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]

    for n, t, m, tt in zip(n, t, m, time_table):
        print(main({'n': n, 't': t, 'm': m, "time_table": tt}))
