from django.http import HttpResponse
from carparking.parking import Parking

def park(request, vehicleNum):
   p = Parking.getInstance()	
   return HttpResponse(p.park(vehicleNum))

def unpark(request, vehicleNum):
	p = Parking.getInstance()
	return HttpResponse(p.unpark(vehicleNum))
def getInfo(request):
	vehicleNum = request.GET.get('vehicleNum')
	slot = request.GET.get('slot')
	p = Parking.getInstance()
	return HttpResponse(p.getInfo(vehicleNum, slot))
