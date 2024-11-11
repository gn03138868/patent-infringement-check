import unittest
from infringe_check import check_infringement

class TestInfringeCheck(unittest.TestCase):

    def test_valid_infringement(self):
        result = check_infringement("US-RE49889-E1", "Walmart Inc.")
        self.assertEqual(result["analysis_id"], "1")
        self.assertGreater(len(result["top_infringing_products"]), 0)

    def test_invalid_patent_id(self):
        with self.assertRaises(ValueError):
            check_infringement("INVALID-ID", "Walmart Inc.")
        
    def test_invalid_company(self):
        with self.assertRaises(ValueError):
            check_infringement("US-RE49889-E1", "Nonexistent Company")

if __name__ == '__main__':
    unittest.main()
