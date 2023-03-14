import time
from lithops import ServerlessExecutor

from lithops.multiprocessing import Pool


# setup_lithops_logger(logging.CRITICAL)


def sample_method(data):
    time_elapsed = time.localtime()
    return time_elapsed


def execute_sample_method_remotely():
    fexec = ServerlessExecutor()
    fut = fexec.call_async(sample_method, 'DATA')
    print('Waiting for the result...')
    result = fut.result()
    print('Result: ', result)

def hello(input):
    return 'Hello,{}!'.format(input)
def square(x):
    return x * x


def divide(x, y):
    return x / y


def sleep_seconds(s):
    time.sleep(s)

execute_sample_method_remotely()

if __name__ == '__main__':

  with Pool() as pool:
      # Synchronously execute function remotely
      res = pool.apply(hello,('World',))
      print(res) #print "Hello World"