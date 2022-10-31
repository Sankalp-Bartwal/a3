class Solution:
    def __init__(self):
        pass
    def getMaxPath(self, g: int, location:list[tuple[int]], coins:list[int], numOfChest: int) -> int:
        chest = {}
        for index, loc in enumerate(location):
            chest[loc] = coins[index]
        
        location.sort(key=lambda x : tuple(x), reverse = True)

        max_cache = {location[0]: chest[location[0]]}
        max = chest[location[0]]

        for index, loc in enumerate(location):
            max_route = 0 
            for key in max_cache:
                print(type(key), key)
                if max_route < max_cache[key] and key[1] >= loc[1]:
                    max_route = max_cache[key]
            max_cache[loc] = chest[loc] + max_route
            if max < max_cache[loc]:
                max = max_cache[loc]
        print(location)
        print(max_cache)
        return max
    
if __name__ == "__main__":
    sol = Solution()
    print("solution", sol.getMaxPath(8, [(4,7),(4,1), (5,5), (3,6), (5,3), (8,2), (1,4), (7,7), (4,4)], [3,42,1,1,42,9,9,9,5],9))