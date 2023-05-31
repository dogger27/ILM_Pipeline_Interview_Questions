"""
Question #4: Implement a simple priority queue.
Assume an incoming stream of dictionaries containing two keys: command to be executed and priority.
Priority is an integer value [0, 10], where work items of the same priority are processed in the order
they are received.


This module provides an abstract base class `AbstractPriorityQueue` for priority queue
implementations, as well as two concrete implementations `PriorityQueue1` and `PriorityQueue2`.

`AbstractPriorityQueue` specifies the interface for a priority queue with `push`, `pop`, and
`is_empty` methods.

`PriorityQueue1` is a basic implementation of a priority queue using a list. The `push` operation
appends an item to the end of the list, and the `pop` operation sorts the list and pops the
highest-priority item. The time complexity is O(n log n) due to the sort operation.

`PriorityQueue2` is a more efficient implementation of a priority queue using a binary heap. The
`push` and `pop` operations maintain the heap property to ensure that the highest-priority item
can always be popped in O(log n) time.

The module also includes a `test_priority_queue` function that tests the functionality of a
priority queue implementation.
"""

from abc import ABC, abstractmethod
from heapq import heappush, heappop


class AbstractPriorityQueue(ABC):
    """Abstract base class for a priority queue."""

    @abstractmethod
    def push(self, item, priority):
        """Push an item onto the queue with a given priority."""
        pass

    @abstractmethod
    def pop(self):
        """Remove and return the lowest priority item. If two items have the same priority,
        return the item that was pushed first."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        pass


class PriorityQueue1(AbstractPriorityQueue):
    """A simple priority queue implementation using a list."""

    def __init__(self):
        self._queue = []
        self._counter = 0  # New variable to track the order items are added

    def push(self, item, priority):
        self._queue.append((priority, self._counter, item))
        self._counter += 1

    def pop(self):
        self._queue.sort(reverse=True)
        return self._queue.pop()[1]

    def is_empty(self):
        return len(self._queue) == 0


class PriorityQueue2(AbstractPriorityQueue):
    """A priority queue implementation using a heap."""

    def __init__(self):
        self._queue = []
        self._counter = 0  # New variable to track the order items are added

    def push(self, item, priority):
        heappush(self._queue, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        return heappop(self._queue)[2]

    def is_empty(self):
        return len(self._queue) == 0


def test_priority_queue(q):
    """Test the priority queue implementation."""
    assert q.is_empty()

    q.push("item1", 2)
    assert not q.is_empty()

    q.push("item2", 1)
    q.push("item3", 3)

    # Push several items with the same priority
    q.push("item4", 2)
    q.push("item5", 2)
    q.push("item6", 2)

    assert q.pop() == "item2"
    assert q.pop() == "item1"

    # These 3 items all have the same priority, so they should be popped in the order they were added
    assert q.pop() == "item4"
    assert q.pop() == "item5"
    assert q.pop() == "item6"

    assert q.pop() == "item3"

    assert q.is_empty()


if __name__ == "__main__":
    test_priority_queue(PriorityQueue1())
    test_priority_queue(PriorityQueue2())
