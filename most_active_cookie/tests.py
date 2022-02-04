import unittest

from .most_active_cookie import findCookie, formatDateInput, parseArgs


class ParserTests(unittest.TestCase):

    def test_happy_path(self):
        inputArgs = ['tests_inputs\\test_input_1.csv', '-d', '2018-12-08']
        parsedArgs = parseArgs(inputArgs)
        self.assertEqual(parsedArgs.filePath, inputArgs[0])

    def test_missing_date_flag(self):
        with self.assertRaises(SystemExit):
            inputArgs = ['tests_inputs\\test_input_1.csv', '2018-12-08']
            parseArgs(inputArgs)

    def test_incorrect_date_format(self):
        with self.assertRaises(SystemExit):
            inputArgs = ['tests_inputs\\test_input_1.csv', '-d', '2018-12-0']
            parseArgs(inputArgs)

    def test_incorrect_file_format(self):
        with self.assertRaises(SystemExit):
            inputArgs = ['tests_inputs\\test_input_1', '-d', '2018-12-08']
            parseArgs(inputArgs)

    def test_non_existent_file(self):
        with self.assertRaises(SystemExit):
            inputArgs = ['tests_inputs\\test_input_0.csv', '-d', '2018-12-08']
            parseArgs(inputArgs)


class FindCookieTest(unittest.TestCase):

    def test_findCookie_happy_path(self):
        testFilePath = "tests_inputs/test_input_1.csv"
        testDate = formatDateInput("2018-12-08")
        expected = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        output = findCookie(testFilePath, testDate)
        self.assertEqual(output, expected)

    def test_findCookie_happy_path(self):
        testFilePath = "tests_inputs/test_input_1.csv"
        testDate = formatDateInput("2018-12-15")
        expected = []
        output = findCookie(testFilePath, testDate)
        self.assertEqual(output, expected)

    def test_empty_file(self):
        with self.assertRaises(Exception):
            testFilePath = "tests_inputs/test_input_2.csv"
            testDate = formatDateInput("2018-12-08")
            output = findCookie(testFilePath, testDate)

    def test_no_body(self):
        testFilePath = "tests_inputs/test_input_3.csv"
        testDate = formatDateInput("2018-12-08")
        expected = []
        output = findCookie(testFilePath, testDate)
        self.assertEqual(output, expected)

    def test_no_header(self):
        with self.assertRaises(Exception):
            testFilePath = "tests_inputs/test_input_4.csv"
            testDate = formatDateInput("2018-12-08")
            findCookie(testFilePath, testDate)

    def test_incorrect_timestamp_format(self):
        with self.assertRaises(Exception):
            testFilePath = "tests_inputs/test_input_5.csv"
            testDate = formatDateInput("2018-12-08")
            findCookie(testFilePath, testDate)

    def test_timezone_sensitivity(self):
        testFilePath = "tests_inputs/test_input_6.csv"
        testDate = formatDateInput("2018-12-09")
        expected = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA"]
        output = findCookie(testFilePath, testDate)
        self.assertEqual(output, expected)

    def test_empty_cookie_value(self):
        with self.assertWarns(Warning):
            testFilePath = "tests_inputs/test_input_7.csv"
            testDate = formatDateInput("2018-12-08")
            expected = ["SAZuXPGUrfbcn5UA", "fbcn5UAVanZf6UtG"]
            output = findCookie(testFilePath, testDate)
            self.assertEqual(output, expected)

    def test_empty_timestamp_value(self):
        with self.assertWarns(Warning):
            testFilePath = "tests_inputs/test_input_8.csv"
            testDate = formatDateInput("2018-12-08")
            expected = ["SAZuXPGUrfbcn5UA", "fbcn5UAVanZf6UtG"]
            output = findCookie(testFilePath, testDate)
            self.assertEqual(output, expected)
