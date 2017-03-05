import unittest
import mock
from access import models


from django.test import TestCase

# Create your tests here.


class DepartmentTests(unittest.TestCase):

    @mock.patch('access.models.DepartmentManager.filter')
    def test_filters_by_name(self, filter_method):
        department = mock.Mock()
        models.Department.objects.get_by_department(department)
        filter_method.assert_called_with(department=department)
