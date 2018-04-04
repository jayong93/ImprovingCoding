import functools


def insert_to_cache(cache, city, cache_size):
    if cache_size > 0:
        if len(cache) >= cache_size:
            cache.pop()
        cache.insert(0, city)


def reorder_cache(cache, city):
    idx = cache.index(city)
    cache[1:idx+1] = cache[:idx]
    cache[0] = city
    return idx


def update_check_cache(cache, city, cache_size):
    city = str(city).upper()
    if city in cache:
        reorder_cache(cache, city)
        return True
    else:
        insert_to_cache(cache, city, cache_size)
        return False


def get_processing_time(is_cache_hit):
    return 1 if is_cache_hit else 5


def main(cache_size, cities):
    cache = []
    hit_list = map(lambda x: update_check_cache(cache, x, cache_size), cities)
    total_time = functools.reduce(
        lambda result, x: result + get_processing_time(x), hit_list, 0)
    return total_time


if __name__ == "__main__":
    print(main(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
                   "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(main(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
                   "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(main(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(main(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(main(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(main(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
