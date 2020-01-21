import os, shutil
from multiprocessing import Queue
import json


class Directory():
	def __init__(self, queue):
		self.start_prefs = {}
		self.end_prefs = {}
		self.file_prefs = {}

		self.list_files = []
		self.work_files = {}
		
		self.work_path = os.getcwd()
		self.file_path = os.getcwd()

		# Give progress status
		self.queue = queue
		self.status = 0

		os.chdir(self.work_path)
		try:
			self.load_state()
		except: pass

	def make_directory(self, path):
		try:
			os.makedirs(path)
			print("Directory ", path, "created ")
		except FileExistsError:
			print("Directory ", path, "already exists")

	def create_start_pref(self, dir_name, name, start_prefix):
		if name:
			folder_name = name
		else:
			folder_name = start_prefix
		path = os.path.join(self.work_path, dir_name, folder_name)
		self.make_directory(path)
		self.start_prefs[start_prefix] = folder_name

	def create_end_pref(self, dir_name, name, end_prefix):
		if name:
			folder_name = name
		else:
			folder_name = end_prefix
		path = os.path.join(self.work_path, dir_name, folder_name)
		self.make_directory(path)
		self.end_prefs[end_prefix] = folder_name

	def create_file_pref(self, dir_name, name, file_prefix):
		if name:
			folder_name = name
		else:
			folder_name = file_prefix
		path = os.path.join(self.work_path, dir_name, folder_name)
		self.make_directory(path)
		self.file_prefs[file_prefix] = folder_name

	def delete_start_pref(self, name, start_prefix):
		try:
			iters = float(100/len(self.work_files.keys()))
		except: return
		if name:
			folder_name = name
		else:
			try:
				folder_name = self.start_prefs[start_prefix]
			except: return

		for dirs in self.work_files.keys():
			self.Progress(iters)
			if name:
				try:
					dir_name = os.path.join(self.work_path, dirs, folder_name)
					shutil.rmtree(dir_name)
					del self.start_prefs[start_prefix]
					break
				except: pass
			else:
				if dirs.startswith(folder_name):
					try:
						dir_name = os.path.join(self.work_path, dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.start_prefs[start_prefix]
						break
					except: pass

			for inner_dirs in self.work_files[dirs]:
				if name:
					try:
						dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.start_prefs[start_prefix]
						break
					except: pass
				else:
					if inner_dirs.startswith(folder_name):
						try:
							dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
							shutil.rmtree(dir_name)
							del self.start_prefs[start_prefix]
							break
						except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def delete_end_pref(self, name, end_prefix):
		self.scan_work_path()
		try:
			iters = float(100/len(self.work_files.keys()))
		except: return
		if name:
			folder_name = name
		else:
			try:
				folder_name = self.end_prefs[end_prefix]
			except: return

		for dirs in self.work_files.keys():
			self.Progress(iters)
			if name:
				try:
					dir_name = os.path.join(self.work_path, dirs, folder_name)
					shutil.rmtree(dir_name)
					del self.end_prefs[end_prefix]
					break
				except: pass
			else:
				if dirs.ednswith(folder_name):
					try:
						dir_name = os.path.join(self.work_path, dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.end_prefs[end_prefix]
						break
					except: pass

			for inner_dirs in self.work_files[dirs]:
				if name:
					try:
						dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.end_prefs[end_prefix]
						break
					except: pass
				else:
					if inner_dirs.endswith(folder_name):
						try:
							dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
							shutil.rmtree(dir_name)
							del self.end_prefs[end_prefix]
							break
						except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def delete_file_pref(self, name, file_prefix):
		try:
			iters = float(100/len(self.work_files.keys()))
		except: return
		if name:
			folder_name = name
		else:
			try:
				folder_name = self.file_prefs[file_prefix]
			except: return
		for dirs in self.work_files.keys():
			self.Progress(iters)
			if name:
				try:
					dir_name = os.path.join(self.work_path, dirs, folder_name)
					shutil.rmtree(dir_name)
					del self.file_prefs[file_prefix]
					break
				except: pass
			else:
				if dirs.endswith(folder_name):
					try:
						dir_name = os.path.join(self.work_path, dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.file_prefs[file_prefix]
						break
					except: pass
			
			for inner_dirs in self.work_files[dirs]:
				if name:
					try:
						dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
						shutil.rmtree(dir_name)
						del self.file_prefs[file_prefix]
						break
					except: pass
				else:
					if inner_dirs.endswith(folder_name):
						try:
							dir_name = os.path.join(self.work_path, dirs, inner_dirs, folder_name)
							shutil.rmtree(dir_name)
							del self.file_prefs[file_prefix]
							break
						except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def work_new_path(self, path):
		if os.path.exists(path):
			self.work_path = path
			os.chdir(self.work_path)
		else: print("Directory doesn't exist")

	def file_new_path(self, path):
		if os.path.exists(path):
			self.file_path = path
		else: print("Directory doesn't exist")

	def move_file(self, file, prefix):
		"""Move files inwards"""
		dir_old = os.path.join(str(self.file_path), str(file))
		dir_new = os.path.join(str(self.work_path), str(prefix), str(file))
		try:
			shutil.move(dir_old, dir_new)
		except: pass

	def move_deep_file(self, file, pref, inner_pref):
		"""Move files inwards"""
		dir_old = os.path.join(self.file_path, file)
		dir_new = os.path.join(self.work_path, pref, inner_pref, file)
		try:
			shutil.move(dir_old, dir_new)
		except: pass

	def move_inner_files(self, prefix, pref_type):
		"""Move files outwards"""
		try:
			if pref_type == "Start Prefix":
				work_dir = self.start_prefs[prefix]
			elif pref_type == "End Prefix":
				work_dir = self.end_prefs[prefix]
			else: work_dir = self.file_prefs[prefix]
		except KeyError:
			return print("Prefix in prefix type doesn't exist")
		path = os.path.join(self.work_path, work_dir)

		with os.scandir(path) as it:
			iters = float(100/len(os.listdir(path)))
			for entry in it:
				self.Progress(iters)
				file = str(entry.name)
				dir_old = os.path.join(self.work_path, work_dir, file)
				dir_new = os.path.join(self.file_path, file)
				try:
					shutil.move(dir_old, dir_new)
				except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def move_deep_files(self, work_dir, inner_dir):
		"""Move files outwards"""
		path = os.path.join(self.work_path, work_dir, inner_dir)
		try:
			with os.scandir(path) as it:
				iters = float(100/len(os.listdir(path)))
				for entry in it:
					self.Progress(iters)
					file = str(entry.name)
					dir_old = os.path.join(self.work_path, work_dir, inner_dir, file)
					dir_new = os.path.join(self.file_path, file)
					try:
						shutil.move(dir_old, dir_new)
					except: pass
		except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def scan_work_path(self):
		try:
			with os.scandir(self.work_path) as it:
				iters = float(100/len(os.listdir(self.work_path)))
				for entry in it:
					self.Progress(iters)
					if entry.is_dir():
						self.work_files[entry.name] = []
		except: pass

		self.Progress(100, False)
		self.Progress(0, False)
		return self.work_files

	def scan_inner_work_path(self):
		try:
			iters = float(100/len(os.listdir(self.work_path)))
		except:
			self.Progress(100, False)
			self.Progress(0, False)
			return
		for directory in self.work_files.keys():
			self.Progress(iters)
			path = os.path.join(self.work_path, directory)
			with os.scandir(path) as it:
				for entry in it:
					if entry.is_dir():
						self.work_files[directory].append(entry.name)

		self.Progress(100, False)
		self.Progress(0, False)
		return self.work_files

	def scan_file_path(self):
		try:
			with os.scandir(self.file_path) as it:
				iters = float(100/len(os.listdir(self.file_path)))
				for entry in it:
					self.Progress(iters)
					if entry.is_file():
						name = str(entry.name)
						self.list_files.append(name)
		except:
			self.Progress(100, False)
			self.Progress(0, False)
			return
		
		self.Progress(100, False)
		self.Progress(0, False)
		return self.list_files

	def scan_inner_file_path(self):
		for directory in self.work_files.keys():
			path = os.path.join(self.work_path, directory)
			with os.scandir(path) as it:
				for entry in it:
					if entry.is_file():
						pass

	def scan_deep_file_path(self):
		for dirs in self.work_files.keys():
			for inner_dir in self.work_files[dirs].keys():
				path = os.path.join(self.work_path, dirs, inner_dir)
				with os.scandir(path) as it:
					for entry in it:
						if entry.is_file():
							pass
							# Deep files
		self.Progress(100, False)
		self.Progress(0, False)
		return self.work_files

	def organize_file(self, file_name):
		self.scan_file_path()
		try:
			iters = float(100/(len(self.end_prefs.keys())
				+ len(self.start_prefs.keys())
				+ len(self.file_prefs.keys())))
		except: return

		file_string = file.split(".")
		for prefix, name in self.end_prefs.items():
			self.Progress(iters)
			if file[0].endswith(prefix):
				dir_name = name
				flag = False
				break

		if flag == False:
			for prefix, name in self.start_prefs.items():
				self.Progress(iters)
				if file[0].startswith(prefix):
					dir_name = name
					flag = False
					break

		if flag == False:
			for prefix, name in self.file_prefs.items():
				self.Progress(iters)
				if file[1].startswith(prefix):
					dir_name = name
					break

		self.Progress(100, False)
		self.Progress(0, False)
		self.move_file(str(file_name), dir_name)

	def organize_files(self):
		self.scan_file_path()

		try:
			start_iter = float(100/(len(self.list_files) + len(self.start_prefs)))
		except: pass
		try:
			end_iter = float(100/(len(self.list_files) + len(self.end_prefs)))
		except: pass
		try:
			file_iter = float(100/(len(self.list_files) + len(self.file_prefs)))
		except: pass

		for file in self.list_files:
			file_string = file.split(".")

			for start_pref, dir_name in self.start_prefs.items():
				self.Progress(start_iter)
				if file_string[0].startswith(start_pref):
					self.move_file(str(file), dir_name)
					continue

			for end_pref, dir_name in self.end_prefs.items():
				self.Progress(end_iter)
				if file_string[0].endswith(end_pref):
					self.move_file(str(file), dir_name)
					continue
			
			for file_pref, dir_name in self.file_prefs.items():
				self.Progress(file_iter)
				if file_string[1].startswith(file_pref):
					self.move_file(str(file), dir_name)
					continue

		self.Progress(100, False)
		self.Progress(0, False)

	def organize_prefix(self, prefix):
		self.scan_file_path()
		try:
			iters = float(100/len(self.list_files))
		except: return
		try:
			dir_name_file = self.file_prefs[prefix]
			for file in self.list_files:
				self.Progress(iters)
				file_string = file.split(".")
				if file_string[1].startswith(prefix):
					self.move_file(str(file), dir_name_file)

			self.Progress(100, False)
			self.Progress(0, False)
			return True
		except: pass
		try:
			dir_name_end = self.end_prefs[prefix]
			for file in self.list_files:
				self.Progress(iters)
				file_string = file.split(".")
				if file_string[0].endswith(prefix):
					self.move_file(str(file), dir_name_end)

			self.Progress(100, False)
			self.Progress(0, False)
			return True
		except: pass
		try:
			dir_name_start = self.start_prefs[prefix]
			for file in self.list_files:
				self.Progress(iters)
				file_string = file.split(".")
				if file_string[0].startswith(prefix):
					self.move_file(str(file), dir_name_start)

			self.Progress(100, False)
			self.Progress(0, False)
			return True
		except: return False

	def organize_type(self, kind):
		self.scan_file_path()
		if kind == "End Prefix":
			try:
				iters = float(100/(len(self.list_files) + len(self.end_prefs.items())))
			except: return
			for file in self.list_files:
				file_string = file.split(".")
				for end_pref, dir_name in self.end_prefs.items():
					self.Progress(iters)
					if file_string[0].endswith(end_pref):
						dir_name = self.end_prefs[end_pref]
						self.move_file(str(file), dir_name)

		elif kind == "Start Prefix":
			try:
				iters = float(100/(len(self.list_files) + len(self.start_prefs.items())))
			except: return
			for file in self.list_files:
				file_string = file.split(".")
				for start_pref, dir_name in self.start_prefs.items():
					self.Progress(iters)
					if file_string[0].startswith(start_pref):
						dir_name = self.start_prefs[start_pref]
						self.move_file(str(file), dir_name)

		elif kind == "File Prefix":
			try:
				iters = float(100/(len(self.list_files) + len(self.file_prefs.items())))
			except: return
			for file in self.list_files:
				file_string = file.split(".")
				for file_pref, dir_name in self.file_prefs.items():
					self.Progress(iters)
					if file_string[1].startswith(file_pref):
						dir_name = self.file_prefs[file_pref]
						self.move_file(str(file), dir_name)

		self.Progress(100, False)
		self.Progress(0, False)

	def organize_prefix_type(self, prefix, kind):
		self.scan_file_path()
		if kind == "End Prefix":
			dir_name_end = self.end_prefs[prefix]
			for file in self.list_files:
				self.Progress(len(self.list_files))
				file_string = file.split(".")
				if file_string[0].endswith(prefix):
					self.move_file(str(file_string[0]), dir_name_end)

		elif kind == "Start Prefix":
			dir_name_start = self.start_prefs[prefix]
			for file in self.list_files:
				self.Progress(len(self.list_files))
				file_string = file.split(".")
				if file_string[0].startswith(prefix):
					self.move_file(str(file), str(dir_name_start))

		elif kind == "File Prefix":
			dir_name_file = str(self.file_prefs[prefix])
			for file in self.list_files:
				self.Progress(len(self.list_files))
				if file == "another_gui.py" \
					or file == "directory_class.py" \
					or file == "end_prefxies.json" \
					or file == "start_prefixes.json" \
					or file == "file_prefixes.json":
					continue
				file_string = file.split(".")
				if file_string[1].startswith(prefix):
					self.move_file(str(file), dir_name_file)

		self.Progress(100, False)
		self.Progress(0, False)

	def organize_file_prefix(self, file_name, prefix):
		self.scan_file_path()
		try:
			dir_name_file = self.file_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)
			return True
		except: pass
		try:
			dir_name_end = self.end_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)
			return True
		except: pass
		try:
			dir_name_start = self.start_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)
			return True
		except: return False

	def organize_file_type(self, file_name, prefix_type):
		self.scan_file_path()
		file_string = file_name.split(".")

		if kind == "End Prefix":
			try:
				iters = float(100/len(self.end_prefs.items()))
				for prefix, name in self.end_prefs.items():
					if file_string[0].endswith(prefix):
						self.move_file(str(file_name), name)
			except: pass

		elif kind == "Start Prefix":
			try:
				iters = float(100/len(self.start_prefs.items()))
				for prefix, name in self.start_prefs.items():
					if file_string[0].startswith(prefix):
						self.move_file(str(file_name), name)
			except: pass

		elif kind == "File Prefix":
			try:
				iters = float(100/len(self.file_prefs.items()))
				for prefix, name in self.file_prefs.items():
					if file_string[1].endswith(prefix):
						self.move_file(str(file_name), name)
			except: pass

		self.Progress(100, False)
		self.Progress(0, False)

	def organize_file_prefix_type(self, file_name, pref, pref_type):
		if kind == "End Prefix":
			dir_name_file = self.file_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)

		elif kind == "Start Prefix":
			dir_name_end = self.end_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)

		elif kind == "File Prefix":
			dir_name_start = self.start_prefs[prefix]
			self.move_file(str(file_name), dir_name_file)

	def search_file(self, search):
		try:
			iters = float(100/len(self.work_files.keys()))
		except: return

		for directory in self.work_files.keys():
			self.Progress(iters)
			path = os.path.join(self.work_path, directory)
			with os.scandir(path) as it:
				for entry in it:
					if entry.name.split(".")[0] == search and entry.is_file():
						self.Progress(100, False)
						self.queue.put(os.path.join(path, entry.name))
						return True

			for inner_dir in self.work_files[directory]:
				path = os.path.join(self.work_path, directory, inner_dir)
				with os.scandir(path) as it:
					for entry in it:
						if entry.name.split(".")[0] == search and entry.is_file():
							self.Progress(100, False)
							self.queue.put(os.path.join(path, entry.name))
							return True

		self.Progress(100, False)
		self.Progress(0, False)
		return False

	def search_files(self, prefix):
		try:
			iters = float(100/len(self.work_files.keys()))
		except: return

		for directory in self.work_files.keys():
			self.Progress(iters)
			path = os.path.join(self.work_path, directory)
			if directory.startswith(prefix) or directory.endswith(prefix):
				self.Progress(100, False)
				return self.queue.put(path)
			for inner_dir in self.work_files[directory]:
				path = os.path.join(self.work_path, directory, inner_dir)
				if inner_dir.startswith(prefix) or inner_dir.endswith(prefix):
					self.Progress(100, False)
					return self.queue.put(path)

		self.Progress(100, False)
		self.Progress(0, False)
		return False

	def Progress(self, add=0, state=True):
		if state == True:
			self.status += add
			self.queue.put(self.status)
		elif state == False:
			self.status = add
			self.queue.put(self.status)

	def save_state(self):
		with open("prefixes.json", "w") as f_obj:
			json_data = {}
			json_data["start_prefixes"] = self.start_prefs
			json_data["end_prefixes"] = self.end_prefs
			json_data["file_prefixes"] = self.file_prefs
			json.dump(json_data, f_obj, indent=4)

	def load_state(self):
		with open("start_prefixes.json", "r") as f_obj:
			json_data = json.load(f_obj)
			self.start_prefs = json_data["start_prefixes"]
			self.end_prefs = json_data["end_prefixes"]
			self.file_prefs = json_data["file_prefixes"]

	def get_work_usage(self):
		return shutil.disk_usage(self.work_path)

#if __name__ == "__main__":
#	Directory(Queue())