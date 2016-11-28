from django.test import TestCase
from django.test import Client
from django.urls import reverse
# Create your tests here.

class ResponseTestBrowse(TestCase):

    def setUp(self):
        print("Set uo [ Response Test ] : browse")
        self.client = Client()

    def test_browse(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/browse")
         response = self.client.get('/browse')
         self.assertEqual(response.status_code, 301)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_browseAll(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/browse/all")
         response = self.client.get('/browse/all')
         self.assertEqual(response.status_code, 301)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_browse1(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/1")
        response = self.client.get("/browse/1")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse2(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/2")
        response = self.client.get("/browse/2")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse3(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/3")
        response = self.client.get("/browse/3")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse4(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/4")
        response = self.client.get("/browse/4")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse5(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/5")
        response = self.client.get("/browse/5")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse6(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/6")
        response = self.client.get("/browse/6")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse7(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/7")
        response = self.client.get("/browse/7")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse8(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/8")
        response = self.client.get("/browse/8")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse9(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/9")
        response = self.client.get("/browse/9")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse10(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/10")
        response = self.client.get("/browse/10")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse11(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/11")
        response = self.client.get("/browse/11")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse12(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/12")
        response = self.client.get("/browse/12")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse13(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/13")
        response = self.client.get("/browse/13")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse14(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/14")
        response = self.client.get("/browse/14")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse15(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/15")
        response = self.client.get("/browse/15")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse16(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/16")
        response = self.client.get("/browse/16")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse17(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/17")
        response = self.client.get("/browse/17")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse18(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/18")
        response = self.client.get("/browse/18")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse19(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/19")
        response = self.client.get("/browse/19")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse20(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/20")
        response = self.client.get("/browse/20")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse21(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/21")
        response = self.client.get("/browse/21")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse22(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/22")
        response = self.client.get("/browse/22")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse23(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/23")
        response = self.client.get("/browse/23")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse24(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/24")
        response = self.client.get("/browse/24")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse25(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/25")
        response = self.client.get("/browse/25")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse26(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/26")
        response = self.client.get("/browse/26")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse27(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/27")
        response = self.client.get("/browse/27")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse28(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/28")
        response = self.client.get("/browse/28")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse29(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/29")
        response = self.client.get("/browse/29")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse30(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/30")
        response = self.client.get("/browse/30")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse31(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/31")
        response = self.client.get("/browse/31")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse32(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/32")
        response = self.client.get("/browse/32")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse33(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/33")
        response = self.client.get("/browse/33")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse34(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/34")
        response = self.client.get("/browse/34")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse35(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/35")
        response = self.client.get("/browse/35")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse36(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/36")
        response = self.client.get("/browse/36")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse37(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/37")
        response = self.client.get("/browse/37")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse38(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/38")
        response = self.client.get("/browse/38")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse39(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/39")
        response = self.client.get("/browse/39")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse40(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/40")
        response = self.client.get("/browse/40")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse41(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/41")
        response = self.client.get("/browse/41")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse42(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/42")
        response = self.client.get("/browse/42")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse43(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/43")
        response = self.client.get("/browse/43")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse44(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/44")
        response = self.client.get("/browse/44")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse45(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/45")
        response = self.client.get("/browse/45")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse46(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/46")
        response = self.client.get("/browse/46")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse47(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/47")
        response = self.client.get("/browse/47")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse48(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/48")
        response = self.client.get("/browse/48")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse49(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/49")
        response = self.client.get("/browse/49")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse50(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/50")
        response = self.client.get("/browse/50")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse51(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/51")
        response = self.client.get("/browse/51")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse52(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/52")
        response = self.client.get("/browse/52")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse53(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/53")
        response = self.client.get("/browse/53")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse54(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/54")
        response = self.client.get("/browse/54")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse55(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/55")
        response = self.client.get("/browse/55")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse56(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/56")
        response = self.client.get("/browse/56")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse57(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/57")
        response = self.client.get("/browse/57")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse58(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/58")
        response = self.client.get("/browse/58")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse59(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/59")
        response = self.client.get("/browse/59")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse60(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/60")
        response = self.client.get("/browse/60")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse61(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/61")
        response = self.client.get("/browse/61")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse62(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/62")
        response = self.client.get("/browse/62")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse63(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/63")
        response = self.client.get("/browse/63")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse64(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/64")
        response = self.client.get("/browse/64")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse65(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/65")
        response = self.client.get("/browse/65")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse66(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/66")
        response = self.client.get("/browse/66")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse67(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/67")
        response = self.client.get("/browse/67")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse68(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/68")
        response = self.client.get("/browse/68")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse69(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/69")
        response = self.client.get("/browse/69")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse70(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/70")
        response = self.client.get("/browse/70")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse71(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/71")
        response = self.client.get("/browse/71")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse72(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/72")
        response = self.client.get("/browse/72")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse73(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/73")
        response = self.client.get("/browse/73")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse74(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/74")
        response = self.client.get("/browse/74")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse75(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/75")
        response = self.client.get("/browse/75")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse76(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/76")
        response = self.client.get("/browse/76")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse77(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/77")
        response = self.client.get("/browse/77")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse78(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/78")
        response = self.client.get("/browse/78")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse79(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/79")
        response = self.client.get("/browse/79")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse80(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/80")
        response = self.client.get("/browse/80")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse81(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/81")
        response = self.client.get("/browse/81")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse82(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/82")
        response = self.client.get("/browse/82")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse83(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/83")
        response = self.client.get("/browse/83")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse84(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/84")
        response = self.client.get("/browse/84")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse85(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/85")
        response = self.client.get("/browse/85")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse86(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/86")
        response = self.client.get("/browse/86")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse87(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/87")
        response = self.client.get("/browse/87")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse88(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/88")
        response = self.client.get("/browse/88")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse89(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/89")
        response = self.client.get("/browse/89")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse90(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/90")
        response = self.client.get("/browse/90")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse91(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/91")
        response = self.client.get("/browse/91")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse92(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/92")
        response = self.client.get("/browse/92")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse93(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/93")
        response = self.client.get("/browse/93")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse94(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/94")
        response = self.client.get("/browse/94")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse95(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/95")
        response = self.client.get("/browse/95")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse96(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/96")
        response = self.client.get("/browse/96")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse97(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/97")
        response = self.client.get("/browse/97")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse98(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/98")
        response = self.client.get("/browse/98")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse99(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/99")
        response = self.client.get("/browse/99")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse100(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/100")
        response = self.client.get("/browse/100")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
