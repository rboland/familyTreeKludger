class TestClass:
    """
    Tests for ftk.py
    """

    testString = "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|" \
            + "1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"



    def test_happyPath(self):
        """Assert that the first node exists"""
        from ftk import FamilyTreeKludger as ftk
        tree = ftk(self.testString)
        familyTree = tree.familyTree
        assert familyTree['id'] == "0"


    def test_grandpaHasTwoKids(self):
        """Assert that Grandpa does have two kids"""
        from ftk import FamilyTreeKludger as ftk
        tree = ftk(self.testString)
        familyTree = tree.familyTree
        assert len(familyTree['children']) == 2

    def test_parentsAndChildren(self):
        """Assert that all nodes are in their correct places"""
        from ftk import FamilyTreeKludger as ftk
        tree = ftk(self.testString)
        familyTree = tree.familyTree
        grandpa = ftk.findNode(tree, 0, familyTree)
        son = ftk.findNode(tree, 1, familyTree)
        assert son in grandpa['children']
        daughter = ftk.findNode(tree, 2, familyTree)
        assert daughter in grandpa['children']
        grandkid3 = ftk.findNode(tree, 3, familyTree)
        assert grandkid3 in son['children']
        grandkid4 = ftk.findNode(tree, 4, familyTree)
        assert grandkid4 in son['children']
        grandkid5 = ftk.findNode(tree, 5, familyTree)
        assert grandkid5 in daughter['children']
        greatgrandkid = ftk.findNode(tree, 6, familyTree)
        assert greatgrandkid in grandkid5['children']

    def test_json(self):
        """Assert that the json output is valid json"""
        from ftk import FamilyTreeKludger as ftk
        import json
        tree = ftk(self.testString)
        j = tree.printJson(indent=None)
        jsn = json.loads(j)
        assert jsn['name'] == "grandpa"
