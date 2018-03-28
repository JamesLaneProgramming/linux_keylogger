import unittest
from linux_key_logger import event_log as el

class testEventLogMethods(unittest.TestCase):
    def setUp(self):
        self.linux_keylogger = el('a', repress_messages = True)
    def test_str_method(self):
        self.assertEqual(self.linux_keylogger.__str__(), 'a')
    def test_is_repeat_method(self):
        self.assertTrue(self.linux_keylogger.is_repeat())
    def test_is_mistake_method(self):
        self.assertFalse(self.linux_keylogger.is_mistake())

if __name__ == '__main__':
    unittest.main()
