import pytest

from components.interfacesBasePage import POCInterface


@pytest.mark.poc_test
class TestWPPages:
    def test_poc(self):
        self.poc_interfaces = POCInterface
        self.poc_interfaces.test_analisis2()
