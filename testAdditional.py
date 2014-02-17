import unittest
import os
import testLib


class TestUserFunct(testLib.RestTestCase):
    """
    Unittests for the Users model class (a sample, incomplete)
    """
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
        
    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)

    def testAdd2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'password'} )
        self.assertResponse(respData, count=1)
        self.assertResponse(respData2, count=1)

    def testEmptyName(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME, count=None)

    def testDuplicate(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData2 = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )

        self.assertResponse(respData, count=1)
        self.assertResponse(respData2, errCode = testLib.RestTestCase.ERR_USER_EXISTS, count=None)

    def firstLogin(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count=1)
        respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count=2)

    def verifyUser(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count=1)
        respData2 = self.makeRequest("/users/login", method="POST", data = { 'user' : 'userWrong', 'password' : 'password'} )
        self.assertResponse(respData2, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS, count = None)

    def verifyPassword(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count=1)
        respData2 = self.makeRequest("users/login", method="POST", data = { 'user' : 'user1', 'password' : 'wrongthing'} )




