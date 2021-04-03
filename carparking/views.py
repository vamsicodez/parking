from django.http import HttpResponse
from carparking.parking import Parking
from carparking.ratelimit import Ratelimit

def ratelimit(func):
	def inner(*args, **kwargs):
		req=args[0]
		r=Ratelimit.getInstance()
		if len(r.Ratelimit)>10000:
			#To Avoid out of memory Exception Error
			r.clearHistory()
		if r.AllowRequest(req.META.get("REMOTE_ADDR")):
			return func(*args, **kwargs)	
		return HttpResponse("User is ratelimited")	
	return inner	


@ratelimit
def park(request, vehicleNum):
   p = Parking.getInstance()	
   return HttpResponse(p.park(vehicleNum))
@ratelimit
def unpark(request, vehicleNum):
	p = Parking.getInstance()
	return HttpResponse(p.unpark(vehicleNum))

@ratelimit	
def getInfo(request):
	vehicleNum = request.GET.get('vehicleNum')
	slot = request.GET.get('slot')
	p = Parking.getInstance()
	return HttpResponse(p.getInfo(vehicleNum, slot))
