Running server - python manage.py runserver


APIS - 
Parking car - localhost:8000/park/<vehicleNum>
	1. Verifies parking slot is available or not
	2. Verifies the car is already parked or not
Unpark      - localhost:8000/unpark/<vehicleNum>
	1. Validates vehicle num
CarInfo     - localhost:8000/info/?VehicleNum=<vehicleNum>
              localhost:8000/info/?slot=<slotno>
     1. Validates vehiclenum
     2. validate sslot no

.env file
PARKING_SLOTS             - Total Number of parking slots
RATELIMIT_WINDOW_INTERVAL - Ratelimit window interval
RATELIMIT_WINDOW_REQUESTS - No:of requests to be ratelimited in the interval





