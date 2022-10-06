def solution(queryType, query):
    count = 0
    getSum = 0
    hashmap = {}
    while count<= len(queryType)-1:
        # print(count)
        if queryType[count] == "insert":
            print('insert')
            hashmap[query[count][0]] = query[count][1]
            
        elif queryType[count] == "addToKey":
            print('key')
            keys = list(hashmap.keys())
            print(keys)
            print(hashmap)
            for key in keys:
                add = query[count][0] + key
                hashmap[add] = hashmap[key]
                print(hashmap)
                # del hashmap[key]
        elif queryType[count] == "addToValue":
            print('val')
            keys = list(hashmap.keys())
            for key in keys:
                hashmap[key] += query[count][0]
        else:
            print('get')
            keys = list(hashmap.keys())
            for key in keys:
                if hashmap[key] == query[count][0]:
                    getSum += hashmap[key]
        count += 1
        
    
    return getSum

print(solution(queryType = ["insert", "insert", "addToKey", "get"], query = [[1, 2], [2, 3], [1], [3]]))
# print(solution(queryType = ["insert", "insert", "addToValue", "addToKey", "get"], query = [[1, 2], [2, 3], [2], [1], [3]]))

# x = {1:2,3:4}
# print(x.keys())