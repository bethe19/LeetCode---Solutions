class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_h = {}
        self.cuisines_h = {}
        self.ratings_h = {}

        for f,c,r in zip(foods,cuisines,ratings):
            self.foods_h[f] = c
            self.ratings_h[f] = r
            if c not in self.cuisines_h:
                self.cuisines_h[c] = []
            heapq.heappush(self.cuisines_h[c], (-r,f))
    def changeRating(self, food: str, newRating: int) -> None:
        c = self.foods_h[food]
        self.ratings_h[food] = newRating 
        heapq.heappush(self.cuisines_h[c], (-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        newHeap = self.cuisines_h[cuisine]
        while newHeap:
            rating, food = newHeap[0]
            if -rating == self.ratings_h[food]:
                return food
            heapq.heappop(newHeap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)