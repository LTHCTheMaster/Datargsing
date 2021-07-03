from datargsing import datargsing

def test_datargsing():
    jm = datargsing.JSON_Manage()
    cm = datargsing.CSV_Manage()
    cjc = datargsing.CSV_JSON_Convert()

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
    
    assert type(cm.get_from_file('./tests/csv/a.csv', ',', True)) == tuple
    assert type(cm.get_from_file('b.csv', ',', True)) == datargsing.datargsing_Error
    assert type(cm.get_from_file('a.lk', ',', True)) == datargsing.datargsing_Error
    content = cm.get_from_file('./tests/csv/a.csv', ',', True)
    assert type(cm.set_to_file('./tests/csv/b.csv', content, ',', True)) == datargsing.datargsing_Complete
    assert type(cm.set_to_file('./tests/csv/c.csv', content, ',', True)) == datargsing.datargsing_Complete
    assert type(cm.set_to_file('a.lk', content, ',', True)) == datargsing.datargsing_Error

    assert type(cm.get_from_file_like_csv('./tests/csv_like/a.csvlike', ',', True)) == tuple
    assert type(cm.get_from_file_like_csv('b.csvlike', ',', True)) == datargsing.datargsing_Error
    content = cm.get_from_file_like_csv('./tests/csv_like/a.csvlike', ',', True)
    assert type(cm.set_to_file_like_csv('./tests/csv_like/b.csvlike', content, ',', True)) == datargsing.datargsing_Complete
    assert type(cm.set_to_file_like_csv('./tests/csv_like/c.csvlike', content, ',', True)) == datargsing.datargsing_Complete

    assert type(cjc.csv_json('./tests/csv/a.csv', './tests/json/csv.json', ',', True)) == datargsing.datargsing_Complete
    assert type(cjc.csv_json('./tests/csv/a.csv', './tests/json/csv.jso', ',', True)) == datargsing.datargsing_Error
    assert type(cjc.csv_json('./tests/csv/a.csvv', './tests/json/csv.json', ',', True)) == datargsing.datargsing_Error
