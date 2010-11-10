import unittest
from system import Directory, DirectoryInitializer, File, FileInitializer

class DirectoryTest(unittest.TestCase):
	def test_can_be_initialized(self):
		d = Directory()
		d.initialize('path')
		assert d.path == 'path'

class DirectoryInitializerTest(unittest.TestCase):
	def test_initializes_directory(self):
		d = Directory()
		initializer = DirectoryInitializer()
		initializer.initialize(d)
		assert d.path == 'initialized_path'

class FileTest(unittest.TestCase):
	def test_can_be_initialized(self):
		f = File('parent')
		f.initialize('name', 'extension')
		assert f.name == 'name'
		assert f.extension == 'extension'
		
	def test_contains_parent_directory(self):
		f = File('parent')
		assert f.parent_directory == 'parent'

class FileInitializerTest(unittest.TestCase):
	def test_initializes_file(self):
		f = File('parent')
		initializer = FileInitializer()
		initializer.initialize(f)
		assert f.name == 'initialized_name'
		assert f.extension == 'initialized_extension'
