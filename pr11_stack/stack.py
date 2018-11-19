"""Stack.py."""

from typing import Any

"""First exception for stack overflow."""


class StackOverflowException(Exception):
    """StackOverflowException."""
    pass


"""First exception for stack underflow."""


class StackUnderflowException(Exception):
    """StackUnderflowException."""
    pass


"""Stack."""


class Stack:
    """Simple stack implementation."""

    def __init__(self, capacity: int) -> None:
        """
        Initialise the stack.

        :param capacity: the maximum number of objects that stack can hold.
        """
        self.capacity = capacity
        self.elements = []

    def push(self, item: Any) -> None:
        """
        Add the element to the collection.

        If stack has no more room, raises StackOverflowException.
        """
        if len(self.elements) >= self.capacity:
            raise StackOverflowException
        else:
            self.elements.insert(0, item)

    def pop(self) -> Any:
        """
        Remove and return the most recently added element that was not yet removed.

        If stack is empty, raises StackUnderflowException.
        """
        if len(self.elements) <= 0:
            raise StackUnderflowException
        else:
            recent_el = self.elements[0]
            self.elements.pop(0)
        return recent_el

    def peek(self) -> Any:
        """
        Show the most recently added element without removing it from the stack.

        If stack is empty returns None.
        """
        if len(self.elements) == 0:
            return None
        else:
            print(self.elements[0])

    def is_empty(self) -> bool:
        """
        Is the list empty?

        :return:
        """
        pass

    def is_full(self) -> bool:
        """
        Is the list full?

        :return:
        """
        pass

    def __str__(self) -> str:
        """
        Get string representation of stack.

        If top element is present should return:
            "Stack(capacity={capacity}, top_element={top_element})"
        Else
            "Stack(capacity={capacity})"
        """
        pass
