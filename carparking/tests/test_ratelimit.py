from django.test import TestCase
from carparking.ratelimit import Ratelimit
import time

class RatelimitTestCase(TestCase):
	
	def test_allow(self):
		r=Ratelimit.getInstance()
		allow=r.AllowRequest("ipaddr1")
		self.assertTrue(allow)
		for i in range(9):
			allow=r.AllowRequest("ipaddr1")
			self.assertTrue(allow)
		allow=r.AllowRequest("ipaddr1")
		self.assertFalse(allow)
		now1=time.time()
		time.sleep(3)
		print(int(time.time()-now1))
		allow=r.AllowRequest("ipaddr1")
		self.assertTrue(allow)	