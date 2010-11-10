import unittest
from system import Directory

class DirectoryTest(unittest.TestCase):
	def test_can_be_initialized(self):
		d = Directory()
		d.initialize('path')
		assert d.path == 'path'
