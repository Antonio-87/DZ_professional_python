import pytest
from accounting_main import get_doc_owner_name, get_all_doc_owners_names
from accounting_main import get_doc_shelf, add_new_doc, delete_doc

fixtures_p = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов')
]

fixtures_ap = [
    {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}
]

fixtures_s = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('10006', '2')
]

fixtures_a =  [('50008', 'insurance', 'Аркадий Мамонтов', '3','3')]


class TestSomething:
    def setup(self):
        print("method setup")


    def teardown(self):
        print("method teardown")

    @pytest.mark.parametrize("number, result", fixtures_p)
    def test_get_doc_owner_name(self, number, result):
        assert get_doc_owner_name(number) == result


    @pytest.mark.parametrize("result", fixtures_ap)
    def test_get_all_doc_owners_names(self, result):
        assert get_all_doc_owners_names() == result


    @pytest.mark.parametrize("number, result", fixtures_s)
    def test_get_doc_shelf(self, number, result):
        assert get_doc_shelf(number) == result
        assert get_doc_shelf(number) != 3

    @pytest.mark.parametrize("number, type, name, shelf, result", fixtures_a)
    def test_add_new_doc(self, number, type, name, shelf, result):
        assert add_new_doc(number, type, name, shelf) == result


    def test_delete_doc(self):
        assert delete_doc('50008') != '50008'


if __name__ == '__main__':
    pytest.main()