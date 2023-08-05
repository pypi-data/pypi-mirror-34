import unittest
import yaml
import binascii
from recordskeeper_python_lib3 import permissions
from recordskeeper_python_lib3.permissions import Permissions

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

class PermissionsTest(unittest.TestCase):


    def test_grantpermissions(self):
        
        txid = Permissions.grantPermission(self, net['permissionaddress'], "create, connect")
        self.assertEqual(txid, 'Invalid permission')

    def test_revokepermissions(self):

        txid = Permissions.revokePermission(self, net['permissionaddress'], "send, admin")
        self.assertEqual(txid, 'Invalid permission')


    def test_failgrantpermissions(self):

    	txid = Permissions.grantPermission(self, net['permissionaddress'], "create, connect")
    	self.assertEqual(txid, 'e3bba87d1f0a980b65f12388d31c734ea38b08d11d00aaab1004e470ca419556')


    def test_failrevokepermissions(self):

    	txid = Permissions.revokePermission(self, net['permissionaddress'], "create, connect")
    	self.assertEqual(txid, 'e3bba87d1f0a980b65f12388d31c734ea38b08d11d00aaab1004e470ca419556')
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PermissionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)