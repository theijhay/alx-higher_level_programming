#!/usr/bin/python3
"""Defines the class Student"""


class Student:
    """Represents class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation in Student instance"""
        return self.__dict__
