import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Crack").teaching()
elif 'aarch' in arc:
	__import__("Crack64").teaching()
else:
	exit(f' Unknow device machine {arc}')
