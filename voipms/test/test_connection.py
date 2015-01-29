import unittest

import voipms.connection

class TestConnection(unittest.TestCase):
	def test_connect(self):
		conn = voipms.connection.Connection("user","password")

if __name__ == '__main__':
	unittest.main()
