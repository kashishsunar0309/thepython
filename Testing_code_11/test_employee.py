'''from employee import Employee
import pytest
#Version 1: Without fixture
def test_give_default_raise():
    emp = Employee('John','Doe',50000)
    emp.give_raise()
    assert emp.annual_salary == 55000
def test_give_custom_raise():
    emp = Employee('John','Doe',50000)
    emp.give_raise(10000)
    assert emp.annual_salary == 60000
'''
#With fixture
"""
from employee import Employee
import pytest
@pytest.fixture
def employee():
    return Employee('John','Doe',50000)
def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000
def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
"""