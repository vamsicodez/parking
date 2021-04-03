from django.conf import settings 

class Parking:
    __instance = None

    @staticmethod 
    def getInstance():
      if Parking.__instance == None:
         Parking()
      return Parking.__instance
   
    def __init__(self):
     
      if Parking.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         slots=getattr(settings, 'PARKING_SLOTS', '5')
         self.totalSlots = int(slots)
         self.carInfo = {}  
         self.parkingInfo= {}
         self.freeSlots = [i for i in range(self.totalSlots)]
         self.busySlots = []
         for i in range(self.totalSlots):
            self.parkingInfo[i] = False
              
         Parking.__instance = self
    
    def park(self, vehicleNum):
        
        if vehicleNum in self.carInfo:
            return "<h2>Vehicle is already parked at "+str(self.carInfo[vehicleNum])+"</h2>"
        if len(self.freeSlots) == 0:
            return "<h2>No parking slots left for vehiclenum "+vehicleNum+"</h2>"
        freeSlot = self.freeSlots.pop(0)    
        self.busySlots.append(freeSlot)
        self.carInfo[vehicleNum] = freeSlot
        self.parkingInfo[freeSlot] = vehicleNum
        return "<h2>Vehicle is parked at slot "+str(self.carInfo[vehicleNum])+"</h2>"
      
    def unpark(self, vehicleNum):
        if vehicleNum not in self.carInfo:
            return "<h2>No vehicle is present with number "+vehicleNum+"</h2>"
        slot = self.carInfo[vehicleNum]  
        del self.carInfo[vehicleNum]
        self.busySlots.remove(slot)
        self.freeSlots.append(slot)
        return "<h2>slot "+str(slot)+" is free"+"</h2>"
        
    def getInfo(self, vehicleNum, slot):
        if vehicleNum!=None:
            if vehicleNum not in self.carInfo:
                return "<h2>No Vehicle is present with this num "+str(vehicleNum)+"</h2>"
            return "<h2>vehicleNum "+str(vehicleNum)+" is parked at slot "+str(self.carInfo[vehicleNum])+"</h2>"
        if slot!=None:
            try:
                slot=int(slot)
            except ValueError:
                return "<h2>Slot Number should be of Integer format</h2>"    
            if slot not in self.parkingInfo:
                return "<h2>Slot number "+str(slot)+" doesn't exist</h2>"
            if slot not in self.busySlots:
                return "<h2>No Vehicle is present at slot "+str(slot)+"</h2>"
                        
            return "<h2>vehicleNum "+self.parkingInfo[slot]+" is parked at slot "+str(slot)+"</h2>"          

        