#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""
An implementation of a Hash using mod.
Please implement the requiered methods.
"""

from HashScheme import HashScheme
import hashlib

class ModHash(HashScheme):

    def __init__(self):
        """
        You have to decide what members to add to the class
        """
        self.__scheme_name = 'Modular_Hash'
        self.nodes = {}
        pass

    def get_name(self):
        return self.__scheme_name


    def dump(self):
        """
        Auxiliary method to print out information about the hash
        """
        for k in self.nodes.keys():
            print ("Node: {0} hash: {1}".format(self.nodes[k], k))

    def add_node(self, new_node):
        """
        Possibly just increment a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        #Funcion para agregar un nodo. Se revisa si ya existe esa llave o no
        hash_value = self.hash(new_node)
        if hash_value not in self.nodes.keys():
            self.nodes[hash_value] = new_node
            return 0
        return 1
        pass

    def remove_node(self, node):
        """
        Possibly just decrement a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        pass

    def hash(self, value):
        """
        Convert value to a number representation and then obtain mod(number_of_nodes)
        """
        if len(self.nodes) == 0:
            return None   
        return int(hashlib.md5(value.encode()).hexdigest(),16) % len(self.nodes)
        pass
