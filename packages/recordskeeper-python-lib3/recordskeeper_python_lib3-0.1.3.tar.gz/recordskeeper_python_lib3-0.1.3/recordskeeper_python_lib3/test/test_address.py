import unittest
import yaml
import binascii
from recordskeeper_python_lib3 import address
from recordskeeper_python_lib3.address import Address


import sys

import os.path
if (os.path.exists("config.yaml")):
   with open("config.yaml", 'r') as ymlfile:
      cfg = yaml.load(ymlfile)
      
      network = cfg['network']

      url = network['url']
      user = network['rkuser']
      password = network['passwd']
      chain = network['chain']
      net = address.network
else:
   
   url = os.environ['url']
   user = os.environ['rkuser']
   password = os.environ['passwd']
   chain = os.environ['chain']
   net = os.environ 


class AddressTest(unittest.TestCase):

    def test_getaddress(self):
        
        address = Address.getAddress()
        address_size = sys.getsizeof(address)
        self.assertEqual(address_size, 83)

    def test_checkifvalid(self):

        checkaddress = Address.checkifValid(self, net['validaddress'])
        self.assertEqual(checkaddress, 'Address is valid')

    def test_failcheckifvalid(self):

        wrongaddress = Address.checkifValid(self, net['invalidaddress'])
        self.assertEqual(wrongaddress, 'Address is valid')

    def test_checkifmineallowed(self):

        checkaddress = Address.checkifMineAllowed(self, net['miningaddress'])
        self.assertEqual(checkaddress, 'Address has mining permission')

    def test_failcheckifmineallowed(self):

        wrongaddress = Address.checkifMineAllowed(self, net['nonminingaddress'])
        self.assertEqual(wrongaddress, 'Address has mining permission')

    def test_checkbalance(self):

        balance = Address.checkBalance(self, net['nonminingaddress'])
        self.assertEqual(balance, 5)

    def test_getmultisigwalletaddress(self):

        address = Address.getMultisigWalletAddress(self, 2, "miygjUPKZNV94t9f8FqNvNG9YjCkp5qqBZ, mwDbTVQcATL263JwpoE8AHCMGM5hE1kd7m, mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9")
        self.assertEqual(address, net['multisigaddress'])

    def test_getmultisigaddress(self):

        address = Address.getMultisigAddress(self, 2,  "miygjUPKZNV94t9f8FqNvNG9YjCkp5qqBZ, mwDbTVQcATL263JwpoE8AHCMGM5hE1kd7m, mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9" )
        self.assertEqual(address, net['multisigaddress'])

    def test_importaddress(self):

        address = Address.importAddress(self, net['miningaddress'])
        self.assertEqual(address, "Address successfully imported")

    def test_wrongimportaddress(self):

        address = Address.importAddress(self, net['wrongimportaddress'])
        self.assertEqual(address, "Invalid Rk address or script")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)