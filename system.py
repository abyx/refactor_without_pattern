class Directory(object):
	def initialize(self, path):
		self.path = path

class DirectoryInitializer(object):
	def initialize_directory(self, directory):
		# Here some system logic happens to get a valid path
		directory.initialize('initialized_path')
