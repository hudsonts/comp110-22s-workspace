"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union


__author__ = "730509671"


class Simpy:
    """A utility class that simplifies the process of working with sequences of numerical data in the form of float values."""
    values: list[float]

    def __init__(self, floats: list[float]):
        """Initializes the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = floats

    def __str__(self) -> str: 
        """Converts the original list into a list of strings."""
        return f"Simpy({self.values})"
    
    def fill(self, v: float, n: int) -> None:
        """Generates a Simpy list of a defined number a defined number of times."""
        self.values: list[float] = []
        i: int = 0
        while i < n:
            self.values.append(v)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values in terms of floats."""
        assert step != 0
        self.values: list[float] = []
        self.values.append(start)
        if start > stop:
            while start > stop - step:
                start += step
                self.values.append(start)
        if start < stop:
            while start < stop - step:
                start += step
                self.values.append(start)

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        i: float = 0
        total: float = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object that is the result of two lists values or a list of values and a float added together."""
        if isinstance(rhs, float):
            result: list[float] = []
            for value in self.values:
                result.append(value + rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            i: float = 0
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object that is the result of the values of one list to the power of the values of the other list or a defined float value."""
        if isinstance(rhs, float):
            result: list[float] = []
            for value in self.values:
                result.append(value ** rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            i: float = 0
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Generates and returns a mask that is a list of boolean values telling whether values are equivalent across lists."""
        if isinstance(rhs, float):
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result
        else:
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result 

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Adds subscription notation to call certain indexes of values from functions and a mask."""
        if isinstance(rhs, float):
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result
        else:
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result          

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Identifies the value at a defined index in self."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)