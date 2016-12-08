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
        
    def test_browse101(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/101")
        response = self.client.get("/browse/101")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse102(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/102")
        response = self.client.get("/browse/102")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse103(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/103")
        response = self.client.get("/browse/103")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse104(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/104")
        response = self.client.get("/browse/104")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse105(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/105")
        response = self.client.get("/browse/105")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse106(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/106")
        response = self.client.get("/browse/106")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse107(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/107")
        response = self.client.get("/browse/107")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse108(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/108")
        response = self.client.get("/browse/108")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse109(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/109")
        response = self.client.get("/browse/109")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse110(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/110")
        response = self.client.get("/browse/110")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse111(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/111")
        response = self.client.get("/browse/111")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse112(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/112")
        response = self.client.get("/browse/112")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse113(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/113")
        response = self.client.get("/browse/113")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse114(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/114")
        response = self.client.get("/browse/114")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse115(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/115")
        response = self.client.get("/browse/115")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse116(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/116")
        response = self.client.get("/browse/116")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse117(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/117")
        response = self.client.get("/browse/117")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse118(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/118")
        response = self.client.get("/browse/118")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse119(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/119")
        response = self.client.get("/browse/119")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse120(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/120")
        response = self.client.get("/browse/120")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse121(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/121")
        response = self.client.get("/browse/121")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse122(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/122")
        response = self.client.get("/browse/122")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse123(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/123")
        response = self.client.get("/browse/123")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse124(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/124")
        response = self.client.get("/browse/124")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse125(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/125")
        response = self.client.get("/browse/125")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse126(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/126")
        response = self.client.get("/browse/126")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse127(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/127")
        response = self.client.get("/browse/127")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse128(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/128")
        response = self.client.get("/browse/128")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse129(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/129")
        response = self.client.get("/browse/129")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse130(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/130")
        response = self.client.get("/browse/130")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse131(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/131")
        response = self.client.get("/browse/131")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse132(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/132")
        response = self.client.get("/browse/132")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse133(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/133")
        response = self.client.get("/browse/133")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse134(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/134")
        response = self.client.get("/browse/134")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse135(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/135")
        response = self.client.get("/browse/135")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse136(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/136")
        response = self.client.get("/browse/136")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse137(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/137")
        response = self.client.get("/browse/137")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse138(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/138")
        response = self.client.get("/browse/138")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse139(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/139")
        response = self.client.get("/browse/139")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse140(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/140")
        response = self.client.get("/browse/140")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse141(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/141")
        response = self.client.get("/browse/141")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse142(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/142")
        response = self.client.get("/browse/142")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse143(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/143")
        response = self.client.get("/browse/143")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse144(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/144")
        response = self.client.get("/browse/144")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse145(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/145")
        response = self.client.get("/browse/145")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse146(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/146")
        response = self.client.get("/browse/146")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse147(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/147")
        response = self.client.get("/browse/147")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse148(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/148")
        response = self.client.get("/browse/148")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse149(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/149")
        response = self.client.get("/browse/149")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse150(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/150")
        response = self.client.get("/browse/150")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse151(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/151")
        response = self.client.get("/browse/151")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse152(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/152")
        response = self.client.get("/browse/152")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse153(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/153")
        response = self.client.get("/browse/153")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse154(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/154")
        response = self.client.get("/browse/154")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse155(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/155")
        response = self.client.get("/browse/155")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse156(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/156")
        response = self.client.get("/browse/156")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse157(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/157")
        response = self.client.get("/browse/157")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse158(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/158")
        response = self.client.get("/browse/158")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse159(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/159")
        response = self.client.get("/browse/159")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse160(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/160")
        response = self.client.get("/browse/160")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse161(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/161")
        response = self.client.get("/browse/161")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse162(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/162")
        response = self.client.get("/browse/162")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse163(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/163")
        response = self.client.get("/browse/163")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse164(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/164")
        response = self.client.get("/browse/164")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse165(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/165")
        response = self.client.get("/browse/165")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse166(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/166")
        response = self.client.get("/browse/166")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse167(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/167")
        response = self.client.get("/browse/167")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse168(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/168")
        response = self.client.get("/browse/168")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse169(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/169")
        response = self.client.get("/browse/169")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse170(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/170")
        response = self.client.get("/browse/170")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse171(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/171")
        response = self.client.get("/browse/171")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse172(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/172")
        response = self.client.get("/browse/172")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse173(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/173")
        response = self.client.get("/browse/173")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse174(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/174")
        response = self.client.get("/browse/174")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse175(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/175")
        response = self.client.get("/browse/175")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse176(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/176")
        response = self.client.get("/browse/176")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse177(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/177")
        response = self.client.get("/browse/177")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse178(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/178")
        response = self.client.get("/browse/178")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse179(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/179")
        response = self.client.get("/browse/179")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse180(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/180")
        response = self.client.get("/browse/180")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse181(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/181")
        response = self.client.get("/browse/181")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse182(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/182")
        response = self.client.get("/browse/182")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse183(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/183")
        response = self.client.get("/browse/183")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse184(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/184")
        response = self.client.get("/browse/184")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse185(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/185")
        response = self.client.get("/browse/185")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse186(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/186")
        response = self.client.get("/browse/186")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse187(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/187")
        response = self.client.get("/browse/187")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse188(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/188")
        response = self.client.get("/browse/188")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse189(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/189")
        response = self.client.get("/browse/189")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse190(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/190")
        response = self.client.get("/browse/190")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse191(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/191")
        response = self.client.get("/browse/191")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse192(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/192")
        response = self.client.get("/browse/192")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse193(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/193")
        response = self.client.get("/browse/193")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse194(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/194")
        response = self.client.get("/browse/194")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse195(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/195")
        response = self.client.get("/browse/195")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse196(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/196")
        response = self.client.get("/browse/196")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse197(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/197")
        response = self.client.get("/browse/197")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse198(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/198")
        response = self.client.get("/browse/198")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse199(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/199")
        response = self.client.get("/browse/199")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse200(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/200")
        response = self.client.get("/browse/200")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse201(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/201")
        response = self.client.get("/browse/201")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse202(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/202")
        response = self.client.get("/browse/202")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse203(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/203")
        response = self.client.get("/browse/203")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse204(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/204")
        response = self.client.get("/browse/204")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse205(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/205")
        response = self.client.get("/browse/205")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse206(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/206")
        response = self.client.get("/browse/206")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse207(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/207")
        response = self.client.get("/browse/207")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse208(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/208")
        response = self.client.get("/browse/208")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse209(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/209")
        response = self.client.get("/browse/209")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse210(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/210")
        response = self.client.get("/browse/210")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse211(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/211")
        response = self.client.get("/browse/211")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse212(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/212")
        response = self.client.get("/browse/212")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse213(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/213")
        response = self.client.get("/browse/213")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse214(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/214")
        response = self.client.get("/browse/214")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse215(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/215")
        response = self.client.get("/browse/215")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse216(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/216")
        response = self.client.get("/browse/216")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse217(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/217")
        response = self.client.get("/browse/217")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse218(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/218")
        response = self.client.get("/browse/218")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse219(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/219")
        response = self.client.get("/browse/219")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse220(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/220")
        response = self.client.get("/browse/220")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse221(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/221")
        response = self.client.get("/browse/221")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse222(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/222")
        response = self.client.get("/browse/222")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse223(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/223")
        response = self.client.get("/browse/223")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse224(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/224")
        response = self.client.get("/browse/224")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse225(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/225")
        response = self.client.get("/browse/225")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse226(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/226")
        response = self.client.get("/browse/226")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse227(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/227")
        response = self.client.get("/browse/227")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse228(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/228")
        response = self.client.get("/browse/228")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse229(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/229")
        response = self.client.get("/browse/229")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse230(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/230")
        response = self.client.get("/browse/230")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse231(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/231")
        response = self.client.get("/browse/231")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse232(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/232")
        response = self.client.get("/browse/232")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse233(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/233")
        response = self.client.get("/browse/233")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse234(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/234")
        response = self.client.get("/browse/234")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse235(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/235")
        response = self.client.get("/browse/235")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse236(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/236")
        response = self.client.get("/browse/236")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse237(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/237")
        response = self.client.get("/browse/237")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse238(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/238")
        response = self.client.get("/browse/238")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse239(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/239")
        response = self.client.get("/browse/239")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse240(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/240")
        response = self.client.get("/browse/240")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse241(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/241")
        response = self.client.get("/browse/241")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse242(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/242")
        response = self.client.get("/browse/242")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse243(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/243")
        response = self.client.get("/browse/243")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse244(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/244")
        response = self.client.get("/browse/244")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse245(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/245")
        response = self.client.get("/browse/245")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse246(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/246")
        response = self.client.get("/browse/246")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse247(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/247")
        response = self.client.get("/browse/247")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse248(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/248")
        response = self.client.get("/browse/248")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse249(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/249")
        response = self.client.get("/browse/249")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse250(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/250")
        response = self.client.get("/browse/250")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse251(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/251")
        response = self.client.get("/browse/251")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse252(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/252")
        response = self.client.get("/browse/252")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse253(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/253")
        response = self.client.get("/browse/253")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse254(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/254")
        response = self.client.get("/browse/254")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse255(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/255")
        response = self.client.get("/browse/255")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse256(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/256")
        response = self.client.get("/browse/256")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse257(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/257")
        response = self.client.get("/browse/257")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse258(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/258")
        response = self.client.get("/browse/258")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse259(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/259")
        response = self.client.get("/browse/259")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse260(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/260")
        response = self.client.get("/browse/260")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse261(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/261")
        response = self.client.get("/browse/261")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse262(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/262")
        response = self.client.get("/browse/262")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse263(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/263")
        response = self.client.get("/browse/263")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse264(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/264")
        response = self.client.get("/browse/264")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse265(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/265")
        response = self.client.get("/browse/265")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse266(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/266")
        response = self.client.get("/browse/266")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse267(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/267")
        response = self.client.get("/browse/267")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse268(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/268")
        response = self.client.get("/browse/268")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse269(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/269")
        response = self.client.get("/browse/269")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse270(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/270")
        response = self.client.get("/browse/270")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse271(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/271")
        response = self.client.get("/browse/271")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse272(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/272")
        response = self.client.get("/browse/272")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse273(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/273")
        response = self.client.get("/browse/273")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse274(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/274")
        response = self.client.get("/browse/274")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse275(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/275")
        response = self.client.get("/browse/275")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse276(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/276")
        response = self.client.get("/browse/276")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse277(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/277")
        response = self.client.get("/browse/277")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse278(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/278")
        response = self.client.get("/browse/278")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse279(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/279")
        response = self.client.get("/browse/279")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse280(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/280")
        response = self.client.get("/browse/280")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse281(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/281")
        response = self.client.get("/browse/281")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse282(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/282")
        response = self.client.get("/browse/282")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse283(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/283")
        response = self.client.get("/browse/283")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse284(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/284")
        response = self.client.get("/browse/284")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse285(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/285")
        response = self.client.get("/browse/285")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse286(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/286")
        response = self.client.get("/browse/286")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse287(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/287")
        response = self.client.get("/browse/287")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse288(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/288")
        response = self.client.get("/browse/288")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse289(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/289")
        response = self.client.get("/browse/289")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse290(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/290")
        response = self.client.get("/browse/290")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse291(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/291")
        response = self.client.get("/browse/291")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse292(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/292")
        response = self.client.get("/browse/292")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse293(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/293")
        response = self.client.get("/browse/293")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse294(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/294")
        response = self.client.get("/browse/294")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse295(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/295")
        response = self.client.get("/browse/295")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse296(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/296")
        response = self.client.get("/browse/296")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse297(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/297")
        response = self.client.get("/browse/297")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse298(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/298")
        response = self.client.get("/browse/298")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse299(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/299")
        response = self.client.get("/browse/299")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_browse300(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/browse/300")
        response = self.client.get("/browse/300")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
