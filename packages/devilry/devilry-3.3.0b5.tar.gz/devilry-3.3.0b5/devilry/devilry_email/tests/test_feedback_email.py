import htmls
from django import test
from django.core import mail
from django.utils import timezone
from django.template import defaultfilters

from datetime import datetime
from model_mommy import mommy

from devilry.devilry_dbcache.customsql import AssignmentGroupDbCacheCustomSql
from devilry.devilry_group import devilry_group_mommy_factories as group_mommy
from devilry.devilry_email.feedback_email import feedback_email
from devilry.apps.core.models import Assignment


class TestFeedbackEmail(test.TestCase):
    def setUp(self):
        AssignmentGroupDbCacheCustomSql().initialize()

    def __setup_feedback_set(self, deadline_datetime=None, grading_published_datetime=None):
        """
        Simple setup used for testing mail content.
        """
        if not deadline_datetime:
            deadline_datetime = timezone.now()
        if not grading_published_datetime:
            grading_published_datetime = timezone.now()
        testassignment = mommy.make_recipe('devilry.apps.core.assignment_activeperiod_start',
                                           points_to_grade_mapper=Assignment.POINTS_TO_GRADE_MAPPER_RAW_POINTS,
                                           long_name='Assignment 1', parentnode__parentnode__long_name='Subject 1')
        testgroup = mommy.make('core.AssignmentGroup', parentnode=testassignment)
        test_feedbackset = group_mommy.feedbackset_first_attempt_published(
            group=testgroup, deadline_datetime=deadline_datetime,
            grading_published_datetime=grading_published_datetime, grading_points=1)
        student = mommy.make('core.Candidate', assignment_group=testgroup)
        mommy.make('devilry_account.UserEmail', user=student.relatedstudent.user, email='student@example.com')
        return test_feedbackset

    def test_send_feedback_email_subject(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            mail.outbox[0].subject,
            '[Devilry] Feedback for {}'.format(test_feedbackset.group.parentnode.long_name))

    def test_send_feedback_email_recipients(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            mail.outbox[0].recipients(),
            ['student@example.com'])

    def test_send_feedback_email_body_result(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_result').alltext_normalized,
            'Result: 1/1 ( passed )')

    def test_send_feedback_email_body_corrected_datetime(self):
        test_feedbackset = self.__setup_feedback_set(grading_published_datetime=datetime.utcnow())
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_corrected_datetime').alltext_normalized,
            'Corrected datetime: {}'.format(
                defaultfilters.date(test_feedbackset.grading_published_datetime, 'DATETIME_FORMAT')))

    def test_send_feedback_email_body_deadline_datetime(self):
        test_feedbackset = self.__setup_feedback_set(deadline_datetime=datetime.utcnow())
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_deadline_datetime').alltext_normalized,
            'Deadline datetime: {}'.format(
                defaultfilters.date(test_feedbackset.deadline_datetime, 'DATETIME_FORMAT')))

    def test_send_feedback_email_body_assignment(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_assignment').alltext_normalized,
            'Assignment: {}'.format(test_feedbackset.group.parentnode.long_name))

    def test_send_feedback_email_body_subject(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_subject').alltext_normalized,
            'Subject: {}'.format(test_feedbackset.group.parentnode.parentnode.parentnode.long_name))

    def test_send_feedback_email_body_link(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_email(feedback_set=test_feedbackset,
                                           points=test_feedbackset.grading_points,
                                           domain_url_start='http://www.example.com/',
                                           feedback_type='feedback_created')
        feedback_link = 'http://www.example.com/devilry_group/student/{}/feedbackfeed/'.format(
            test_feedbackset.group.id)
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one('.devilry_email_feedback_detail_text').alltext_normalized,
            'See the delivery feed for more details:')
        self.assertEqual(
            htmls.S(mail.outbox[0].message().as_string()).one(
                '.devilry_email_feedback_detail_url').alltext_normalized,
            feedback_link)

    def test_send_feedback_edited_email_subject(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_edited_email(feedback_set=test_feedbackset,
                                                  points=test_feedbackset.grading_points,
                                                  domain_url_start='http://www.example.com/')
        self.assertEqual(
            mail.outbox[0].subject,
            '[Devilry] Feedback updated for {}'.format(test_feedbackset.group.parentnode.long_name))

    def test_send_feedback_created_email_subject(self):
        test_feedbackset = self.__setup_feedback_set()
        feedback_email.send_feedback_created_email(feedback_set=test_feedbackset,
                                                   points=test_feedbackset.grading_points,
                                                   domain_url_start='http://www.example.com/')
        self.assertEqual(
            mail.outbox[0].subject,
            '[Devilry] Feedback for {}'.format(test_feedbackset.group.parentnode.long_name))
