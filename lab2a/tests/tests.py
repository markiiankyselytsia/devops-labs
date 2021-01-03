import unittest
from unittest import mock
from datetime import datetime
from app import main, my_good_fun, home_work


class TestClass(unittest.TestCase):
    am_expected_outp = 'Доброго дня'
    pm_expected_outp = 'Доброї ночі'

    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    @mock.patch('app.datetime')
    def test_home_work(self, dt_mock):
        # now
        # 2021.10.10 10:10:10
        dt_mock.now.return_value = datetime(2021, 10, 10, 10, 10, 10)
        res = home_work()
        # self.assertEqual(dt_mock.now.call_count, 1)
        self.assertEqual(res, self.am_expected_outp)

        # 2021.10.10 17:10:10
        dt_mock.now.return_value = datetime(2021, 10, 10, 17, 10, 10)
        res = home_work()
        self.assertEqual(dt_mock.now.call_count, 2)
        self.assertEqual(res, self.pm_expected_outp)

    def test_my_fun(self):
        self.assertEqual(my_good_fun(), "success")
