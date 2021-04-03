from django.test import TestCase
from carparking.parking import Parking

class ParkingTestCase(TestCase):

	def test_init(self):
		p=Parking.getInstance()
		self.assertEqual(p.totalSlots, 5)
		self.assertEqual(len(p.carInfo), 0)
		self.assertEqual(len(p.parkingInfo), 5)
		self.assertEqual(len(p.freeSlots), 5)
		self.assertEqual(len(p.busySlots), 0)

	def test_park_unpark_info(self):
		p=Parking.getInstance()
		resp=p.park("1001")
		self.assertEqual("<h2>Vehicle is parked at slot 0</h2>", resp)
		self.assertEqual(1, len(p.busySlots))
		self.assertEqual(4, len(p.freeSlots))
		self.assertEqual("1001", p.parkingInfo[0])
		self.assertEqual(0, p.carInfo["1001"])

		resp=p.park("1002")
		self.assertEqual("<h2>Vehicle is parked at slot 1</h2>", resp)
		self.assertEqual(2, len(p.busySlots))
		self.assertEqual(3, len(p.freeSlots))
		self.assertEqual("1002", p.parkingInfo[1])
		self.assertEqual(1, p.carInfo["1002"])
		resp=p.park("1003")
		resp=p.park("1004")
		resp=p.park("1004")
		self.assertEqual("<h2>Vehicle is already parked at 3</h2>", resp)
		resp=p.park("1005")
		

		self.assertEqual(5, len(p.busySlots))
		self.assertEqual(0, len(p.freeSlots))

		#After full parking
		resp=p.park("1006")
		self.assertEqual("<h2>No parking slots left for vehiclenum 1006</h2>", resp)
		self.assertFalse("1006" in p.carInfo)

		#UnPark a car
		resp=p.unpark("1003")
		self.assertEqual(2, p.freeSlots[0])
		resp=p.unpark("1004")
		self.assertEqual(3, p.freeSlots[1])
		resp=p.unpark("0000")
		self.assertEqual("<h2>No vehicle is present with number 0000</h2>", resp)

		#Parking after freeing slots
		resp=p.park("1006")
		self.assertEqual("<h2>Vehicle is parked at slot 2</h2>", resp)

		resp = p.getInfo(vehicleNum="1001",slot=None)
		self.assertEqual("<h2>vehicleNum 1001 is parked at slot 0</h2>", resp)
		resp=p.getInfo(vehicleNum=None, slot=0)
		self.assertEqual("<h2>vehicleNum 1001 is parked at slot 0</h2>", resp)

		resp=p.getInfo(vehicleNum="0000", slot=None)
		self.assertEqual("<h2>No Vehicle is present with this num 0000</h2>", resp)
















