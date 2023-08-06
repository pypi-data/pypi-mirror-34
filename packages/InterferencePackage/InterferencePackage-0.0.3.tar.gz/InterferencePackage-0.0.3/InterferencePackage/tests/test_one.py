from unittest import TestCase
import InterferencePackage.InterferencePackage as IP

class TestOne(TestCase):
	def testIsString(self):
		s = IP.InterferencePackage()
		self.assertIsNotNone(s)
