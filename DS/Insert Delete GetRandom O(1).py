# class RandomizedSet:
#     def __init__(self):
#         self.Set = []

#     def insert(self, val: int) -> bool:
#         if val in self.Set:
#             return False
#         self.Set.append(val)
#         return True

#     def remove(self, val: int) -> bool:
#         if val in self.Set:
#             self.Set.remove(val)
#             return True
#         return False
        

#     def getRandom(self) -> int:
#         return choice(self.Set)


class RandomizedSet:

    def __init__(self):
        self.randset = {}
        self.temp = []

    def insert(self, val: int) -> bool:
        if val not in self.randset:
            self.randset[val] = len(self.temp)
            self.temp.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randset:
            last_element = self.temp[-1]
            last_index = self.randset[last_element]
            current_index = self.randset[val]
            self.temp[current_index], self.temp[last_index] = self.temp[last_index], self.temp[current_index]
            self.randset[last_element] = current_index
            del self.randset[val]
            self.temp.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.temp)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
    
    
    
    