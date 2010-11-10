import unittest
from system import Directory, DirectoryInitializer, File, FileInitializer, ResourceInitializer

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

class DummyInitializer(object):
	def initialize(self, resource):
		self.called_with = resource

class ResourceInitializerTest(unittest.TestCase):
	def setUp(self):
		self.file_initializer = DummyInitializer()
		self.directory_initializer = DummyInitializer()
		self.resource_initializer = ResourceInitializer(self.file_initializer, self.directory_initializer)

	def test_initializes_file_using_file_initializer(self):
		f = File('parent')
		self.resource_initializer.initialize(f)
		assert self.file_initializer.called_with == f

	def test_initializes_a_files_directory(self):
		f = File('parent')
		self.resource_initializer.initialize(f)
		assert self.directory_initializer.called_with == 'parent'

	def test_initializes_a_directory_by_itself(self):
		d = Directory()
		self.resource_initializer.initialize(d)
		assert self.directory_initializer.called_with == d
		
