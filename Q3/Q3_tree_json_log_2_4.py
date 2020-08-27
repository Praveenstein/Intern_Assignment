# -*- coding: utf-8 -*-
""" Implementing a tree and storing it's information in a class

This script requires that `Json` be installed within the Python
environment you are running this script in.

This file contains the following class:

    * TreeNode - This class represent a single node of a tree
    * Tree - This class represents the tree

"""

import json
import logging
from os import path
import logging.config


class TreeNode:
    """It represents the whole tree
     It has the following methods
            *get_level(): Used to get level of the current node in the whole hierarchy of tree
            *print_tree(): Used to print the current node and it's children in preorder traversal "Root->Left->Right"
            *add_child(): Used to add child to the current node
    """

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_depth(self):
        """
        :return int depth: Returns the depth of the given node( number of ancestors)
        """
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent

        return depth

    def print_tree(self):
        """
        This methods travels through the tree in pre-order traversal to print all it's elements
        """
        spaces = ' ' * self.get_depth() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        """
        This methods is used to add a child to the given node
        :param TreeNode child: New instance of TreeNode
        """
        child.parent = self
        self.children.append(child)


class Tree:
    """It represents the whole tree
     It has the following methods
            *_adding_child(): Based on the data in the given json file, it will add children from the root node
            *show_data(): It prints the whole tree
    """

    def __init__(self, data):
        self.data = data
        self.root = TreeNode(self.data['data'])
        self.found = False

    def adding_child(self, p, data):
        """
        given a json file with tree data, this method is used to populate the tree
        :param TreeNode p: The parent node
        :param dic data: The corresponding data, such us it's value, list of children
        """
        try:
            for values in data['children']:
                _child = TreeNode(values['data'])
                p.add_child(_child)
                if values['children']:
                    self.adding_child(_child, values)
        except Exception:
            logger.error("Error Occurred", exc_info=True)

    def show_data(self):
        """
        Prints the whole tree
        """
        self.root.print_tree()

    def post_order(self):
        """
        Traverses through the elements of the tree in post order and prints them
        """
        Tree._post_order(self.root)
        print(self.root.data)

    @staticmethod
    def _post_order(node):
        """
        Used by the post_order method to traverse from the root node
        It prints the all the child nodes from left to right and then prints the root node
        :param node: The node from which the traversal has to be done
        """

        for child in node.children:
            if child.children:
                Tree._post_order(child)
            print(child.data + "->", end='')

    def get_level(self, element):
        """
        Given an element in the tree it will find the level of it
        :param element: The element for which the level needs to be found
        :return int : returns the level or none if the elements doesn't exist
        """

        self.found = False

        def find(p, element_):
            if p.data == element_:
                self.found = True
                return p.get_depth() + 1
            if p.children:
                for child in p.children:
                    if self.found:
                        break
                    z = find(child, element_)
                    if not z:
                        continue
                    return z

        level = find(self.root, element)
        return level


def log():
    """
    Creates a custom logger from the configuration dictionary
    """
    with open('log_tree.json', 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    global logger
    logger = logging.getLogger(__name__)


def main():
    """
    Main function to instantiate a tree class
    """
    log()
    file = 'TreeJson_4.json'
    if not path.exists(file):
        logger.error("The given file does not exist")
        raise Exception("The file does not exist")
    with open(file) as f:
        data = json.load(f)
    tree = Tree(data)
    tree.adding_child(tree.root, tree.data)
    level = tree.get_level("25")
    if not level:
        logger.info("The given element does not exist")
    else:
        print(level)


if __name__ == '__main__':
    main()
