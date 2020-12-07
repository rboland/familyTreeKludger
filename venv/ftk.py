#!/bin/python3
"""
The given string has pipe delimited nodes that represent family members in a family tree. Each node is a CSV with the values being "parent_id, node_id, node_name". Write a method that takes an input string and return a single result that represents the data as a hierarchy (root, children, siblings, etc).
Sample input: "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
• Solve it in any language that you prefer
• Display the hierarchical result any way you prefer (as long as the parent/child connections are clear)
"""
import json
import sys

class FamilyTreeKludger:
    _familyList = None
    familyTree = None

    def __init__(self, inputStr ):
        self._familyList = []
        for j in inputStr.split("|"):
            self._familyList.append(j.split(","))

        # Find the root node.  We will presume that the root node has "null"
        # in the first field.
        for person in self._familyList:
            if person[0] == "null":
                self.familyTree = {}
                self.familyTree['id'] = person[1]
                self.familyTree['name'] = person[2]
                self.familyTree['children'] = []
                self._familyList.remove(person)
                break

        self.findDescendants(self.familyTree)

    def findDescendants(self, node):
        '''
        Recursively find descendants of a person in the _familyList.
        Finds children, and then calls itself on each child.
        Each pass removes "that" generation from the _familyList, so
        that it doesn't waste cpu cycles processing people repeatedly.
        :param node: A dict describing a person, starting with the patriarch
            in the root node.
        '''
        for person in self._familyList:
            pass
            if person[0] == node['id']:
                temp = {}
                temp['id'] = person[1]
                temp['name'] = person[2]
                temp['children'] = []
                node['children'].append(temp)
                
        # Remove everyone from "this" generation from the list.
        self._familyList = [
            person for person in self._familyList if person[0] != node['id']]
        
        for person in node['children']:
            self.findDescendants(person)

    def printJson(self, indent=4):
        """
        Returns a JSON-Formatted string, containing the familyTree object.
        For "human" readability, suggest using the default indent level of 4.
        For a single-line string, used indent = None.
        :param indent:
        :return: String
        """
        return json.dumps(self.familyTree, indent = indent)

            
    def printTree(self, node, depth):
        """
        Does an pre-order transversal of a Family Tree, printing out the
        name, indented by the depth.  This is the "quick and dirty" way
        of printing out a tree!
        :param node: Initially the root node, but called recursively.
        :param depth: Initially zero, increments with each call.
        """
        print("{}{}".format("\t" * depth, node['name']))
        for child in node['children']:
            self.printTree(child, depth + 1)

    def findNode(self, id, node):
        """
        Find a node in the familyTree by the ID.  The tree is not set up as a
        search tree, so the execution time will be on the order of O(n), since
        it will simply search until it finds the requested node.  Hopefully,
        it will be useful for testing.
        :param id: Can be either an integer or an integer string.
        :param node: Initially, the root node, but called recursively.
        :return: Python dict, containing the requested node (but also
        all of that node's descendants (if any), in the "children" field.
        """



if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg =  "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|"
        arg += "1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"

    tree = FamilyTreeKludger(arg)
    tree.printTree(tree.familyTree, 0)
