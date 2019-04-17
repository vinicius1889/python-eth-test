from unittest import TestCase

class MiscTestCases(TestCase):

    SLOCKIT="slockit"
    SLOCKIT_HASH="736c6f636b6974"

    def testingHexToString(self):
        name = MiscTestCases.SLOCKIT.encode("utf-8")
        hexa = name.hex()
        self.assertEqual(hexa, MiscTestCases.SLOCKIT_HASH)



    def testingDecode(self):
        name = bytearray.fromhex(MiscTestCases.SLOCKIT_HASH).decode()
        self.assertEqual(name,MiscTestCases.SLOCKIT)


    def testing(self):
        print(hex(1))
        print(int(hex(1), 16))


