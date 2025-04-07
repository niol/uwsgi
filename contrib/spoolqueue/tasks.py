from tasksconsumer import queueconsumer
from __future__ import print_function


@queueconsumer('fast', 4)
def fast_queue(arguments):
    print("fast", arguments)


@queueconsumer('slow')
def slow_queue(arguments):
    print("foobar", arguments)
