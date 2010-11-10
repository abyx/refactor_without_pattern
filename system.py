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

class ResourceInitializer(object):
	def __init__(self, file_initializer, directory_initializer):
		self.file_initializer = file_initializer
		self.directory_initializer = directory_initializer

	# This is the interface that I was aiming for: users can supply a generic resource
	# and it will simply be initialized. If it has dependencies, they will be initialized
	# too
	def initialize(self, resource):
		if isinstance(resource, File):
			self.file_initializer.initialize(resource)
			self._initialize_directory(resource.parent_directory)
		else:
			self._initialize_directory(resource)

	def _initialize_directory(self, directory):
		self.directory_initializer.initialize(directory)
