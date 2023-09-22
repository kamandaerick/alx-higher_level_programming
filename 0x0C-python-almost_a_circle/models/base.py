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
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_data = cls.to_json_string(dict_list)

        with open(cls.__name__ + ".json", "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Return list of json strng representation of json_string

        Args:
            json_string (str): list of disctionaries

        Returns:
            list: list of json strings
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            return None
        new_obj.update(**dictionary)
        return new_obj
