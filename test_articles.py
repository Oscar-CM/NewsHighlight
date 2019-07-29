import unittest
from app.models import Articles
# Articles=articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    testcase class
    '''
    def setUp(self):
        '''
        testcase that runs after every test
        '''
        self.new_article= Articles ()
    def test_for_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
if __name__=='__main__':
    unittest.main()