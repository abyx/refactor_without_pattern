import unittest
from system import Directory, DirectoryInitializer, File

class DirectoryTest(unittest.TestCase):
	def test_can_be_initialized(self):
		d = Directory()
		d.initialize('path')
		assert d.path == 'path'

class DirectoryInitializerTest(unittest.TestCase):
	def test_initializes_directory(self):
		d = Directory()
		initializer = DirectoryInitializer()
		initializer.initialize_directory(d)
		assert d.path == 'initialized_path'

class FileTest(unittest.TestCase):
	def test_can_be_initialized(self):
		f = File()
		f.initialize('name', 'extension')
		assert f.name == 'name'
		assert f.extension == 'extension'
		
