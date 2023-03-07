import time

from lithops import FunctionExecutor


def sample_method(data):
    data
    return time.process_time()


def hello(name):
    return 'Hello {}!'.format(name)


with FunctionExecutor() as fexec:
    # fut = fexec.call_async(hello, 'World')
    # print(fut.result())
    fut2 = fexec.call_async(sample_method,'DATA')
    print(fut2.result())
