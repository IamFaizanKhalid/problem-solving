class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.distances = defaultdict(lambda: defaultdict(tuple))
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t1 = self.checkins[id]
        del self.checkins[id]
        t -= t1

        total,count=0,0
        data = self.distances[startStation][stationName]
        if data:
            total,count = data
        self.distances[startStation][stationName] = (total+t, count+1)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count = self.distances[startStation][endStation]
        return round(total/count, 5)


        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
