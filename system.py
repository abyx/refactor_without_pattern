class Directory(object):
	def initialize(self, path):
		self.path = path

class DirectoryInitializer(object):
	def initialize(self, directory):
		# Here some system logic happens to get a valid path
		directory.initialize('initialized_path')

class File(object):
	def __init__(self, parent_directory):
		self.parent_directory = parent_directory

	def initialize(self, name, extension):
		self.name = name
		self.extension = extension

class FileInitializer(object):
	def initialize(self, file):
		# Here some system logic happens to get valid file names & exts.
		file.initialize('initialized_name', 'initialized_extension')
