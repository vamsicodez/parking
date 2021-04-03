from django.conf import settings 

import time
class Ratelimit:
    
    __instance = None

    @staticmethod 
    def getInstance():
      print("Static method of ratelimit")  
      if Ratelimit.__instance == None:
         Ratelimit()
        
      return Ratelimit.__instance

    def __init__(self):
        if Ratelimit.__instance != None:
            raise Exception("This class is a singleton!")
        self.Ratelimit = {}
        self.reqLen = int(getattr(settings, 'RATELIMIT_WINDOW_REQUESTS', '10'))
        self.windowInterval = int(getattr(settings, 'RATELIMIT_WINDOW_INTERVAL', '2'))
        Ratelimit.__instance = self
    
    def AllowRequest(self,ipaddr):
        #Each i
        now = time.time()    
        if ipaddr not in self.Ratelimit:
            self.Ratelimit[ipaddr] = [now]
            return True
        if len(self.Ratelimit[ipaddr])<self.reqLen:
            self.Ratelimit[ipaddr].append(now)
            return True
        oldReqArrival = self.Ratelimit[ipaddr][0]
        now=time.time()
        if int(now-oldReqArrival)>=self.windowInterval:
            self.Ratelimit[ipaddr].pop(0)
            self.Ratelimit[ipaddr].append(now)
            return True
        return False

    def clearHistory(self):
        #To avoid out of memory exception
        for key in self.Ratelimit:
            val=self.Ratelimit[key][-1]
            now=time.time()
            if int(now-val)>10:
                del self.Ratelimit[key]
        if len(self.Ratelimit)>10000:
            #Clear ratelimit entire history
            self.Ratelimit = {}            









         
               