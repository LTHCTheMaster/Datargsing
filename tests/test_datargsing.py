from datargsing import datargsing

def test_datargsing():
    jm = datargsing.JSON_Manage()
    assert type(jm.get_from_file('./tests/json/a.json', True)) == dict
    assert type(jm.get_from_file('b.json', True)) == datargsing.datargsing_Error
    assert type(jm.get_from_file('a.lk', True)) == datargsing.datargsing_Error
