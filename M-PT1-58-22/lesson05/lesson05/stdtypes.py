from typing import Hashable
import helpers


def differ(orig: set, template: set) -> set:
    return orig.difference(template)


def main():
    # len_atr = len(helpers.ATTRS_NO_TEST)
    # print('HelloWorld')
    # print(len_atr)
    # len_list = differ(set(dir(list)), helpers.ATTRS_NO_TEST)
    # len_dict = differ(set(dir(dict)), helpers.ATTRS_NO_TEST)
    # len_str = differ(set(dir(str)), helpers.ATTRS_NO_TEST)
    # len_set = differ(set(dir(set)), helpers.ATTRS_NO_TEST)
    # len_tuple = differ(set(dir(tuple)), helpers.ATTRS_NO_TEST)
    # print(f"{len(len_tuple)} + {len(len_set)} + {len(len_str)} + {len(len_dict)} + {len(len_list)}")
    # print(f"{set(dir(tuple))}\n{len_tuple}")


    test_list = [4, 2, 3]
    testing_dict = {1:'one', 2:'two'}
    t_set = {1, 2}
    str1 = repr("")
    print(str1)

    #str methods
    assert "pytho".ljust(6, 'n') == "python"
    assert "py it's a good ext".partition("it's") == ('py ', "it's", ' a good ext')
    assert " ".isspace()
    assert "noise" in "white noise"
    assert "langpython".removeprefix("lang") == "python"
    assert "qwqwqw".replace('q', 'k', 2) == "kwkwqw"
    assert "_".join("qwerty") == "q_w_e_r_t_y"
    assert "item"[1] == 't'
    assert "item".index('t') == 1
    assert "PYTHON".lower() == "python"
    assert "PYTHON".isupper()
    assert 'creature,,,'.removesuffix(',,,') == "creature"
    assert "python".islower()
    assert "csharp".translate({99: 110}) == "nsharp"
    assert " python ".strip() == "python"
    assert "error inside".find("inside") == 6
    assert "sssd".isidentifier()
    assert "12".isdigit()
    assert "ErRoR".swapcase() == "eRrOr"
    assert "qwe".center(7) == "  qwe  "
    assert "read only for".rsplit(" ", 1) == ['read only', 'for']
    assert "\u0033".isdecimal()
    assert "2233".isnumeric()
    assert "python".endswith('n')
    assert "ython".rjust(7, 'p') == "ppython"
    assert "pyt{0}on".format('h') == "python"
    assert "text".isprintable()
    assert "title".title() == "Title"
    assert "text".isascii()
    assert "hohohohoho".rfind('h') == 8
    assert "hohohohoho".count('h') == 5
    assert "ErRoR".casefold() == "error"
    assert "NO\tRD".expandtabs(2) == "NO  RD"
    assert "11".zfill(4) == "0011"
    assert "Python".istitle()
    assert len("three") == 5
    assert "district13".isalnum()
    assert "python".maketrans('p', 'c') == {112: 99}
    assert "out to in".rpartition("to") == ('out ', 'to', ' in')
    assert "{x}{y}".format_map({'x': '4', 'y': '5'}) == '45'
    assert "pyt" + "hon" == "python"
    assert "python   ".rstrip() == "python"
    assert "pine#apple".split('#') == ["pine", "apple"]
    assert "Français".encode() == b'Fran\xc3\xa7ais'
    assert "python".startswith('p')
    assert "    python  ".lstrip() == "python  "
    assert isinstance("python", Hashable)
    assert "python".capitalize() == "Python"
    assert "%sgress and %sgress" % ("pro", "re") == "progress and regress"
    assert "notnum".isalpha()
    assert "Three" * 3 == "ThreeThreeThree"
    assert "python".upper() == "PYTHON"
    assert "sci\nand\nfi".splitlines() == ['sci', 'and', 'fi']
    assert "AAA" < "B"

    # list methods
    
    assert len(test_list) == 3
    assert not isinstance(test_list, Hashable)
    assert test_list.copy() == [4, 2, 3]
    test_list[1] = 5
    assert test_list == [4, 5, 3]
    test_list[2] = test_list[2] * 3
    assert test_list == [4, 5, 9]
    assert test_list[0] + 3 == 7
    test_list[0] = test_list[0] + 3
    assert test_list == [7, 5, 9]
    assert test_list[0] * 2 == 14
    test_list.extend([4, 2])
    assert test_list == [7, 5, 9, 4, 2]
    test_list.pop(1)
    assert test_list == [7, 9, 4, 2]
    assert test_list.index(9) == 1
    test_list.reverse()
    assert test_list == [2, 4, 9, 7]
    assert 2 in test_list
    del(test_list[0])
    assert test_list == [4, 9, 7]
    test_list.sort()
    assert test_list == [4, 7, 9]
    assert test_list[1] == 7
    assert test_list.count(4) == 1
    test_list.remove(4)
    assert test_list == [7, 9]
    test_list.append(3)
    assert test_list == [7, 9, 3]
    test_list.insert(1, 8)
    assert test_list == [7, 8, 9, 3]
    test_list.clear()
    assert test_list == []
    assert test_list < [4, 6]

    # Dict methods

    assert testing_dict.items() == {(1, 'one'), (2, 'two')}
    testing_dict.update({3:'three'})
    assert testing_dict == {1:'one', 2:'two', 3:'three'} 
    testing_dict = testing_dict | {3: '3'}
    assert testing_dict == {1:'one', 2:'two', 3:'3'}
    assert str(testing_dict.values()) == "dict_values(['one', 'two', '3'])"
    assert len(testing_dict) == 3
    testing_dict.pop(1)
    assert testing_dict == {2: 'two', 3: '3'}
    testing_dict |= {4: '4'}
    assert testing_dict == {2: 'two', 3: '3', 4: '4'}
    testing_dict.popitem()
    assert testing_dict == {2: 'two', 3: '3'}
    assert 3 in testing_dict
    assert testing_dict.copy() == {2: 'two', 3: '3'}
    assert testing_dict.get(2) == 'two'
    testing_dict.setdefault(4, '4')
    assert testing_dict == {2: 'two', 3: '3', 4: '4'}
    assert dict.fromkeys([1, 2, 3]) == {1: None, 2: None, 3: None}
    assert testing_dict[3] == '3'
    assert not isinstance(testing_dict, Hashable)
    assert str(testing_dict.keys()) == "dict_keys([2, 3, 4])"
    testing_dict[3] = 'tri'
    assert testing_dict == {2: 'two', 3: 'tri', 4: '4'}
    del testing_dict[4]
    testing_dict.clear()
    assert testing_dict == {}

    # Set methods
    
    t_set |= {3}
    assert t_set == {1, 2, 3}
    t_set.remove(1)
    assert t_set == {2, 3}
    temp_set = {3, 8, 4}
    t_set = t_set.symmetric_difference(temp_set)
    assert t_set == {8, 2, 4}
    t_set.difference_update({4, 7})
    assert t_set == {2, 8}
    assert 2 in t_set
    t_set.symmetric_difference_update({5, 4, 2})
    assert t_set == {4, 5, 8}
    assert not isinstance(t_set, Hashable)
    t_set = t_set & {4, 5, 1}
    assert t_set == {4, 5}
    t_set = t_set | {1, 4}
    assert t_set == {1, 4, 5}

    print(repr(t_set))
    

if __name__ == "__main__":
    main()
