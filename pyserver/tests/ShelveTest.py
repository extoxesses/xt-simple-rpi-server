from datetime import datetime
from modules.models.shelve import Shelve
import unittest

class ShelveTest(unittest.TestCase):

  def test_default_constructor(self):
    shelve = Shelve(50)
    self.assertEqual(shelve.cpu_temp, 50)
    self.assertFalse(shelve.is_alert)
    self.assertIsNotNone(shelve.last_update)
    self.assertIsNotNone(shelve.last_status_change)

  def test_positional_constructor(self):
    shelve = self.get_mocked_shelve()
    self.assertEqual(shelve.cpu_temp, 50)
    self.assertTrue(shelve.is_alert)
    self.assertEqual(shelve.last_update.isoformat(), '2020-01-01T00:00:00')
    self.assertEqual(shelve.last_status_change.isoformat(), '2020-01-02T00:00:00')

  def test_str(self):
    shelve = self.get_mocked_shelve()
    self.assertEqual(str(shelve), 'cpu_temp: 50, is_alert: True, last_update: 2020-01-01T00:00:00, last_status_change: 2020-01-02T00:00:00')

  def test_repr(self):
    shelve = self.get_mocked_shelve()
    self.assertEqual(repr(shelve), '{"cpu_temp": 50, "is_alert": true, "last_update": "Wed, 01 Jan 2020 00:00:00 GMT", "last_status_change": "Thu, 02 Jan 2020 00:00:00 GMT"}')

  def test_update_with_alert(self):
    shelve = self.get_mocked_shelve()
    shelve.update(60, True)
    self.assertEqual(shelve.cpu_temp, 60)
    self.assertTrue(shelve.is_alert)
    self.assertNotEqual(shelve.last_update.isoformat(), '2020-01-01T00:00:00')
    self.assertEqual(shelve.last_status_change.isoformat(), '2020-01-02T00:00:00')

  def test_update_without_alert(self):
    shelve = self.get_mocked_shelve()
    shelve.update(60, False)
    self.assertEqual(shelve.cpu_temp, 60)
    self.assertFalse(shelve.is_alert)
    self.assertNotEqual(shelve.last_update.isoformat(), '2020-01-01T00:00:00')
    self.assertNotEqual(shelve.last_status_change.isoformat(), '2020-01-02T00:00:00')

  def get_mocked_shelve(self) -> Shelve:
    last_update = datetime.fromisoformat('2020-01-01T00:00:00')
    last_status_change = datetime.fromisoformat('2020-01-02T00:00:00')
    return Shelve(50, is_alert=True, last_update=last_update, last_status_change=last_status_change)


if __name__ == '__main__':
  unittest.main()