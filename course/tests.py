from django.test import TestCase
from django.test import Client

# Create your tests here.
class ResponseTestCourse(TestCase):

    def setUp(self):
        print("Set uo [ Response Test ] : course")
        self.client = Client()

    def test_course(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course")
        response = self.client.get('/course')
        self.assertEqual(response.status_code, 404)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_course1(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/1")
        response = self.client.get("/course/1")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course2(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/2")
        response = self.client.get("/course/2")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course3(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/3")
        response = self.client.get("/course/3")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course4(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/4")
        response = self.client.get("/course/4")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course5(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/5")
        response = self.client.get("/course/5")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course6(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/6")
        response = self.client.get("/course/6")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course7(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/7")
        response = self.client.get("/course/7")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course8(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/8")
        response = self.client.get("/course/8")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course9(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/9")
        response = self.client.get("/course/9")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course10(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/10")
        response = self.client.get("/course/10")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course11(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/11")
        response = self.client.get("/course/11")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course12(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/12")
        response = self.client.get("/course/12")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course13(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/13")
        response = self.client.get("/course/13")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course14(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/14")
        response = self.client.get("/course/14")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course15(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/15")
        response = self.client.get("/course/15")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course16(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/16")
        response = self.client.get("/course/16")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course17(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/17")
        response = self.client.get("/course/17")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course18(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/18")
        response = self.client.get("/course/18")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course19(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/19")
        response = self.client.get("/course/19")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course20(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/20")
        response = self.client.get("/course/20")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course21(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/21")
        response = self.client.get("/course/21")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course22(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/22")
        response = self.client.get("/course/22")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course23(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/23")
        response = self.client.get("/course/23")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course24(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/24")
        response = self.client.get("/course/24")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course25(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/25")
        response = self.client.get("/course/25")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course26(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/26")
        response = self.client.get("/course/26")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course27(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/27")
        response = self.client.get("/course/27")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course28(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/28")
        response = self.client.get("/course/28")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course29(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/29")
        response = self.client.get("/course/29")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course30(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/30")
        response = self.client.get("/course/30")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course31(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/31")
        response = self.client.get("/course/31")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course32(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/32")
        response = self.client.get("/course/32")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course33(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/33")
        response = self.client.get("/course/33")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course34(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/34")
        response = self.client.get("/course/34")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course35(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/35")
        response = self.client.get("/course/35")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course36(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/36")
        response = self.client.get("/course/36")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course37(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/37")
        response = self.client.get("/course/37")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course38(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/38")
        response = self.client.get("/course/38")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course39(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/39")
        response = self.client.get("/course/39")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course40(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/40")
        response = self.client.get("/course/40")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course41(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/41")
        response = self.client.get("/course/41")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course42(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/42")
        response = self.client.get("/course/42")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course43(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/43")
        response = self.client.get("/course/43")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course44(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/44")
        response = self.client.get("/course/44")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course45(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/45")
        response = self.client.get("/course/45")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course46(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/46")
        response = self.client.get("/course/46")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course47(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/47")
        response = self.client.get("/course/47")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course48(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/48")
        response = self.client.get("/course/48")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course49(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/49")
        response = self.client.get("/course/49")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course50(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/50")
        response = self.client.get("/course/50")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course51(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/51")
        response = self.client.get("/course/51")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course52(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/52")
        response = self.client.get("/course/52")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course53(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/53")
        response = self.client.get("/course/53")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course54(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/54")
        response = self.client.get("/course/54")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course55(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/55")
        response = self.client.get("/course/55")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course56(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/56")
        response = self.client.get("/course/56")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course57(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/57")
        response = self.client.get("/course/57")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course58(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/58")
        response = self.client.get("/course/58")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course59(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/59")
        response = self.client.get("/course/59")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course60(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/60")
        response = self.client.get("/course/60")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course61(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/61")
        response = self.client.get("/course/61")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course62(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/62")
        response = self.client.get("/course/62")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course63(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/63")
        response = self.client.get("/course/63")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course64(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/64")
        response = self.client.get("/course/64")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course65(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/65")
        response = self.client.get("/course/65")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course66(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/66")
        response = self.client.get("/course/66")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course67(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/67")
        response = self.client.get("/course/67")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course68(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/68")
        response = self.client.get("/course/68")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course69(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/69")
        response = self.client.get("/course/69")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course70(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/70")
        response = self.client.get("/course/70")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course71(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/71")
        response = self.client.get("/course/71")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course72(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/72")
        response = self.client.get("/course/72")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course73(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/73")
        response = self.client.get("/course/73")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course74(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/74")
        response = self.client.get("/course/74")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course75(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/75")
        response = self.client.get("/course/75")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course76(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/76")
        response = self.client.get("/course/76")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course77(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/77")
        response = self.client.get("/course/77")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course78(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/78")
        response = self.client.get("/course/78")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course79(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/79")
        response = self.client.get("/course/79")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course80(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/80")
        response = self.client.get("/course/80")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course81(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/81")
        response = self.client.get("/course/81")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course82(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/82")
        response = self.client.get("/course/82")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course83(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/83")
        response = self.client.get("/course/83")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course84(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/84")
        response = self.client.get("/course/84")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course85(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/85")
        response = self.client.get("/course/85")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course86(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/86")
        response = self.client.get("/course/86")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course87(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/87")
        response = self.client.get("/course/87")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course88(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/88")
        response = self.client.get("/course/88")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course89(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/89")
        response = self.client.get("/course/89")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course90(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/90")
        response = self.client.get("/course/90")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course91(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/91")
        response = self.client.get("/course/91")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course92(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/92")
        response = self.client.get("/course/92")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course93(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/93")
        response = self.client.get("/course/93")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course94(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/94")
        response = self.client.get("/course/94")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course95(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/95")
        response = self.client.get("/course/95")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course96(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/96")
        response = self.client.get("/course/96")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course97(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/97")
        response = self.client.get("/course/97")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course98(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/98")
        response = self.client.get("/course/98")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course99(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/99")
        response = self.client.get("/course/99")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_course100(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/course/100")
        response = self.client.get("/course/100")
        self.assertEqual(response.status_code, 301)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
