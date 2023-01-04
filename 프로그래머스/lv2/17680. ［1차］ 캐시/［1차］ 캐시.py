def solution(cacheSize, cities):
    # LRU 
    # if call existing element, place that item to the top
    answer = 0
    
    # defualt case
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    for city in cities:
        city = city.lower()
        cache_hit = False
        if city in cache:
            # city 가 cache 안에 있을때
            cache_hit = True
            
            # 기존의 ctiy 를 지우고 cache 대가리에 city 넣기
            cache.remove(city)
            cache.insert(0, city)    
            
        else:
            # city 가 cache 안에 없을때
            if len(cache) == cacheSize:
                cache.pop()    
            cache.insert(0, city)
    
        if cache_hit:
            answer += 1
        else:
            answer += 5
        # print(answer)
    
    return answer