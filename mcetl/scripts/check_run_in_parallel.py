import logging
import time
from multiprocessing import Process
from ..utils.LoggingHelper import LoggingHelper


def run_in_parallel(fn_list, arg_list):
    proc = []
    for i in range(0, len(fn_list)):
        p = Process(target=fn_list[i], args=arg_list[i])
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


def try_it(n):
    print(n, 's')
    for i in range(0, 2*n):
        print(n, i)
        time.sleep(1)
    print(n, 'e')


if __name__ == "__main__":
    LoggingHelper().set_root()
    startup_log = logging.getLogger("main-setup")

    target_list = []
    target_arg_list = []

    for count in range(0, 10):
        target_list.append(try_it)
        target_arg_list.append((count,))

    run_in_parallel(target_list, target_arg_list)

    print("Done")
