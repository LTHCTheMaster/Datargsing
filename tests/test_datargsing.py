from datargsing import datargsing_core

def test_datargsing():
    jm = datargsing_core.JSON_Manage()
    cm = datargsing_core.CSV_Manage()
    cjc = datargsing_core.CSV_JSON_Convert()

    assert type(jm.get_from_file('./tests/json/a.json', True)) == dict
    assert type(jm.get_from_file('b.json', True)) == datargsing_core.datargsing_Error
    assert type(jm.get_from_file('a.lk', True)) == datargsing_core.datargsing_Error
    assert type(jm.set_to_file('./tests/json/b.json', {"a":"u","l":True}, True)) == datargsing_core.datargsing_Complete
    assert type(jm.set_to_file('./tests/json/c.json', {"a":"u","l":True}, True)) == datargsing_core.datargsing_Complete
    assert type(jm.set_to_file('a.lk', {"a":"u","l":True}, True)) == datargsing_core.datargsing_Error
    
    assert type(jm.get_from_file_like_json('./tests/json_like/a.jsonlike', True)) == dict
    assert type(jm.get_from_file_like_json('b.jsonlike', True)) == datargsing_core.datargsing_Error
    assert type(jm.set_to_file_like_json('./tests/json_like/b.jsonlike', {"a":"u","l":True}, True)) == datargsing_core.datargsing_Complete
    assert type(jm.set_to_file_like_json('./tests/json_like/c.jsonlike', {"a":"u","l":True}, True)) == datargsing_core.datargsing_Complete
    
    assert type(cm.get_from_file('./tests/csv/a.csv', ',', True)) == tuple
    assert type(cm.get_from_file('b.csv', ',', True)) == datargsing_core.datargsing_Error
    assert type(cm.get_from_file('a.lk', ',', True)) == datargsing_core.datargsing_Error
    content = cm.get_from_file('./tests/csv/a.csv', ',', True)
    assert type(cm.set_to_file('./tests/csv/b.csv', content, ',', True)) == datargsing_core.datargsing_Complete
    assert type(cm.set_to_file('./tests/csv/c.csv', content, ',', True)) == datargsing_core.datargsing_Complete
    assert type(cm.set_to_file('a.lk', content, ',', True)) == datargsing_core.datargsing_Error

    assert type(cm.get_from_file_like_csv('./tests/csv_like/a.csvlike', ',', True)) == tuple
    assert type(cm.get_from_file_like_csv('b.csvlike', ',', True)) == datargsing_core.datargsing_Error
    content = cm.get_from_file_like_csv('./tests/csv_like/a.csvlike', ',', True)
    assert type(cm.set_to_file_like_csv('./tests/csv_like/b.csvlike', content, ',', True)) == datargsing_core.datargsing_Complete
    assert type(cm.set_to_file_like_csv('./tests/csv_like/c.csvlike', content, ',', True)) == datargsing_core.datargsing_Complete

    assert type(cjc.csv_json_get_set('./tests/csv/a.csv', './tests/json/csv.json', ',', True)) == datargsing_core.datargsing_Complete
    assert type(cjc.csv_json_get_set('./tests/csv/a.csv', './tests/json/csv.jso', ',', True)) == datargsing_core.datargsing_Error
    assert type(cjc.csv_json_get_set('./tests/csv/a.csvv', './tests/json/csv.json', ',', True)) == datargsing_core.datargsing_Error
    assert type(cjc.csv_json_get('./tests/csv/a.csv', ',', True)) == dict
    assert type(cjc.csv_json_get('./tests/csv/a.csvv', ',', True)) == datargsing_core.datargsing_Error

    assert(type(cjc.json_csv_get_set('./tests/json/for_csv.json', './tests/csv/json.csv', ',', True))) == datargsing_core.datargsing_Complete
    assert(type(cjc.json_csv_get_set('./tests/json/for_csv.jso', './tests/csv/json.csv', ',', True))) == datargsing_core.datargsing_Error
    assert(type(cjc.json_csv_get_set('./tests/json/for_csv.json', './tests/csv/json.csvv', ',', True))) == datargsing_core.datargsing_Error
    assert(type(cjc.json_csv_get('./tests/json/for_csv.json', True))) == tuple
    assert(type(cjc.json_csv_get('./tests/json/for_csv.jso', True))) == datargsing_core.datargsing_Error

    assert type(cjc.csv_like_json_get_set('./tests/csv_like/a.csvlike', './tests/json/csv.json', ',', True)) == datargsing_core.datargsing_Complete
    assert type(cjc.csv_like_json_get_set('./tests/csv_like/a.csvv', './tests/json/csv.json', ',', True)) == datargsing_core.datargsing_Error
    assert type(cjc.csv_json_like_get_set('./tests/csv/a.csv', './tests/json_like/csv.jsonlike', ',', True)) == datargsing_core.datargsing_Complete
    assert type(cjc.csv_json_like_get_set('./tests/csv/a.csvv', './tests/json_like/csv.jsonlike', ',', True)) == datargsing_core.datargsing_Error
    assert type(cjc.csv_like_json_like_get_set('./tests/csv_like/a.csvlike', './tests/json_like/csv.jsonlike', ',', True)) == datargsing_core.datargsing_Complete
    assert type(cjc.csv_like_json_like_get_set('./tests/csv_like/a.csvv', './tests/json_like/csv.jsonlike', ',', True)) == datargsing_core.datargsing_Error
    assert type(cjc.csv_like_json_get('./tests/csv_like/a.csvlike', ',', True)) == dict
    assert type(cjc.csv_like_json_get('./tests/csv_like/a.csvv', ',', True)) == datargsing_core.datargsing_Error

    assert(type(cjc.json_like_csv_get_set('./tests/json_like/for_csv.jsonlike', './tests/csv/json.csv', ',', True))) == datargsing_core.datargsing_Complete
    assert(type(cjc.json_like_csv_get_set('./tests/json_like/for_csv.jso', './tests/csv/json.csv', ',', True))) == datargsing_core.datargsing_Error
    assert(type(cjc.json_csv_like_get_set('./tests/json/for_csv.json', './tests/csv_like/json.csvlike', ',', True))) == datargsing_core.datargsing_Complete
    assert(type(cjc.json_csv_like_get_set('./tests/json/for_csv.jso', './tests/csv_like/json.csvlike', ',', True))) == datargsing_core.datargsing_Error
    assert(type(cjc.json_like_csv_like_get_set('./tests/json_like/for_csv.jsonlike', './tests/csv_like/json.csvlike', ',', True))) == datargsing_core.datargsing_Complete
    assert(type(cjc.json_like_csv_like_get_set('./tests/json_like/for_csv.jso', './tests/csv_like/json.csvlike', ',', True))) == datargsing_core.datargsing_Error
    assert(type(cjc.json_like_csv_get('./tests/json_like/for_csv.jsonlike', True))) == tuple
    assert(type(cjc.json_like_csv_get('./tests/json_like/for_csv.jso', True))) == datargsing_core.datargsing_Error
