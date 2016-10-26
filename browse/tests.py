from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class BrowseViewTests(TestCase):
    def test_index_view_with_no_courses(self):
        '''
            If no courses exist, an appropriate message should be displayed.
        '''
        response = self.client.get(reverse('browse:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No available course.')
        self.assertQuerysetEqual(response.context['courses'], [])

    # def test_index_view_with_future_question_and_past_question(self):
    #     """
    #     Even if both past and future questions exist, only past questions
    #     should be displayed.
    #     """
    #     create_question(question_text="Past question.", days=-30)
    #     create_question(question_text="Future question.", days=30)
    #     response = self.client.get(reverse('browse:index'))
    #     self.assertQuerysetEqual(
    #         response.context['courses'],
    #         ['<Course: Course object>']
    #     )
