from datargsing import datargsing

def test_datargsing():
    jm = datargsing.JSON_Manage()
    assert type(jm.get_from_file('./tests/json/a.json', True)) == dict
    assert type(jm.get_from_file('b.json', True)) == datargsing.datargsing_Error
    assert type(jm.get_from_file('a.lk', True)) == datargsing.datargsing_Error
    assert type(jm.set_to_file('./tests/json/b.json', {"a":"u","l":True}, True)) == datargsing.datargsing_Complete
    assert type(jm.set_to_file('./tests/json/c.json', {"a":"u","l":True}, True)) == datargsing.datargsing_Complete
    assert type(jm.set_to_file('a.lk', {"a":"u","l":True}, True)) == datargsing.datargsing_Error
    assert type(jm.get_from_file_like_json('./tests/json_like/a.jsonlike', True)) == dict
    assert type(jm.get_from_file_like_json('b.jsonlike', True)) == datargsing.datargsing_Error
    assert type(jm.set_to_file_like_json('./tests/json_like/b.jsonlike', {"a":"u","l":True}, True)) == datargsing.datargsing_Complete
    assert type(jm.set_to_file_like_json('./tests/json_like/c.jsonlike', {"a":"u","l":True}, True)) == datargsing.datargsing_Complete
