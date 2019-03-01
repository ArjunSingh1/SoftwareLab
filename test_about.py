import unittest
from HttpHandler import get_issues_statistics, get_contributors_statistics

class MyTestCase(unittest.TestCase):
    def test_issues(self):
        table = get_issues_statistics()
        expectedtotal = table['total']
        total = table['rabia'] + table['wenran'] + table['blake'] + table['yinghong'] + table['arjun']
        self.assertEqual(expectedtotal,total,"Should be the same")
        self.assertEqual(0,table['rabia'])
        self.assertEqual(0, table['yinghong'])
        self.assertEqual(0, table['blake'])
        self.assertEqual(0, table['arjun'])
        self.assertEqual(2, table['wenran'])

    def test_contributors(self):
        table = get_contributors_statistics()
        expectedtotal = table['total']
        total = table['rabia'] + table['wenran'] + table['blake'] + table['yinghong'] + table['arjun']
        self.assertEqual(expectedtotal, total, "Should be the same")
        self.assertEqual(0, table['rabia'])
        self.assertEqual(1, table['yinghong'])
        self.assertEqual(4, table['blake'])
        self.assertEqual(0, table['arjun'])
        self.assertEqual(3, table['wenran'])

if __name__ == '__main__':
    unittest.main()
