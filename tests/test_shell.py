# core modules
import unittest

# internal modules
from mpu.shell import Codes


class ShellTest(unittest.TestCase):

    def test_codes(self):
        print(Codes.BOLD + Codes.GREEN + 'WORKS!' + Codes.RESET_ALL)