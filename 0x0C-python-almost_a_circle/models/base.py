#!/usr/bin/python3
"""Define a Base class "BAse" """
import json


class Base:
    """Definition of a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): tracks the instances of the class. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            JSON: json representation of disctionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON representation of list_objs to a file

        Args:
            list_objs (object): list of objects inheriting from base
        """
        if list_objs is None:
            json.loads(cls.json, "[]")
        else:
            with open(cls.__name__ + ".json", "w") as file:
                json_data = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(json_data))
