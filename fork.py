import sys, time, os

def f():
    pid = os.fork()
    if pid == 0:
        os.execv(
            "/usr/bin/env",
            ["", "python", "-c",
             "import sys, time; print time.ctime(time.time()); time.sleep(5)"])


if __name__ == '__main__':
    for i in range(long(sys.argv[1])): f()
    time.sleep(10)
