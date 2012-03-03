# make tests

import os
import unittest

import pydog

test_path = 'tmp'


class PydocTest(unittest.TestCase):
    def setUp(self):
        self.test_ofile_name = os.path.join(test_path, 'ofile.txt')
        if not os.path.exists(test_path):
            os.makedirs(test_path)

    def tearDown(self):
        if os.path.exists(self.test_ofile_name):
            os.remove(self.test_ofile_name)
        if os.path.exists(test_path):
            os.removedirs(test_path)

    def test_open_create_file(self):
        pydog.main('text', self.test_ofile_name)
        self.assertTrue(os.path.isfile(os.path.join(test_path, 'ofile.txt')))


if __name__ == '__main__':
    unittest.main()
