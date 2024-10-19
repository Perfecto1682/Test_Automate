from StringUtils import StringUtils

string_utils = StringUtils()


def capitilize(self, string):
    assert string_utils.capitilize('skypro') == 'Skypro'  # noqa:  E501
    assert string_utils.capitilize('') == ''  # noqa:  E501
    assert string_utils.capitilize(' ') == ' '  # noqa:  E501
    assert string_utils.capitilize('  skypro') == 'Skypro'  # noqa:  E501
    assert string_utils.capitilize('skypro  '.strip()) == 'Skypro'  # noqa:  E501


def test_trim():
    assert string_utils.trim('   skypro') == 'skypro'  # noqa:  E501
    assert string_utils.trim('skypro') == 'skypro'  # noqa:  E501
    assert string_utils.trim('') == ''  # noqa:  E501
    assert string_utils.trim('  ') == ''  # noqa:  E501


def test_to_list():
    assert string_utils.to_list('a,b,c') == ['a', 'b', 'c']  # noqa:  E501
    assert string_utils.to_list('a,,b,c') == ['a', '', 'b', 'c']  # noqa:  E501
    assert string_utils.to_list('') == []  # noqa:  E501
    assert string_utils.to_list('a,b,c,') == ['a', 'b', 'c', '']  # noqa:  E501
    assert string_utils.to_list('1:2:3', ':') == ['1', '2', '3']  # noqa:  E501


def test_contains():
    assert string_utils.contains('SkyPro', 'S') is True  # noqa:  E501
    assert string_utils.contains('SkyPro', 'U') is False  # noqa:  E501
    assert string_utils.contains('', 'a') == False  # noqa:  E501
    assert string_utils.contains('abc', '') == True  # noqa:  E501
    assert string_utils.contains('abc', 'abc') == True  # noqa:  E501


def test_delete_symbol():
    assert string_utils.delete_symbol('SkyPro', 'k') == 'SyPro'  # noqa:  E501
    assert string_utils.delete_symbol('SkyPro', 'Pro') == 'Sky'  # noqa:  E501
    assert string_utils.delete_symbol('', 'a') == ''  # noqa:  E501
    assert string_utils.delete_symbol('SkyPro', 'X') == 'SkyPro'  # noqa:  E501
    assert string_utils.delete_symbol('abc123', '123') == 'abc'  # noqa:  E501


def test_starts_with():
    assert string_utils.starts_with('SkyPro', 'S') is True  # noqa:  E501
    assert string_utils.starts_with('SkyPro', 'U') is False  # noqa:  E501
    assert string_utils.starts_with('', 'a') == False  # noqa:  E501
    assert string_utils.starts_with('abc', 'a') == True  # noqa:  E501
    assert string_utils.starts_with('abc', 'X') == False  # noqa:  E501


def test_end_with():
    assert string_utils.end_with('SkyPro', 'o') is True  # noqa:  E501
    assert string_utils.end_with('SkyPro', 'U') is False  # noqa:  E501
    assert string_utils.end_with('', 'a') == False  # noqa:  E501
    assert string_utils.end_with('abc', 'c') == True  # noqa:  E501
    assert string_utils.end_with('abc', 'X') == False  # noqa:  E501


def test_list_to_string():
    assert string_utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'  # noqa:  E501
    assert string_utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'  # noqa:  E501
    assert string_utils.list_to_string([]) == ''  # noqa:  E501
    assert string_utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'  # noqa:  E501
    assert string_utils.list_to_string(['a', 'b', 'c'], '') == 'abc'  # noqa:  E501
