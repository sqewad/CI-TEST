import unittest
from datetime import *
from Guests import *
schedule = [
                {
                    "end_time": "05/06/2017 20:00",
                    "service": "massage_shiatsu",
                    "start_time": "05/06/2017 19:00",
                    "time_of_reserving": "04/26/2017 13:27"
                },
                {
                    "end_time": "05/06/2017 17:00",
                    "service": "massage_shiatsu",
                    "start_time": "05/06/2017 16:00",
                    "time_of_reserving": "04/26/2017 13:28"
                }
            ]

guest = Guests('a','0','0',schedule)
class TestGuestsMethods(unittest.TestCase):

    def test_check_schecule(self):
        self.assertEqual(guest.check_guest_schedule(datetime(2017,5,6,17),datetime(2017,5,6,18), True))
        self.assertEqual(guest.check_guest_schedule(datetime(2017,5,6,16,30),datetime(2017,5,6,17,30), False))
        self.assertEqual(guest.check_guest_schedule(datetime(2017,5,6,18),datetime(2017,5,6,19), True))

if __name__ == '__main__':
    unittest.main()
