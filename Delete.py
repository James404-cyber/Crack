import os, sys
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			print(" [?] How to use : ")
			exit(" [!] Usages : python run.py remove")
	try:
		__import__("delete").menu()
	except Exception as e:
		exit(str(e))
