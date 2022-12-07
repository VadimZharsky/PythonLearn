# import helpers


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

    strexp = "qwerty"
    str1 = repr("Français".encode())
    print(str1)

    assert "pytho".ljust(6, 'n') == "python"
    assert "py it's a good ext".partition("it's") == ('py ', "it's", ' a good ext')
    assert " ".isspace()
    assert "noise" in "white noise"
    assert "langpython".removeprefix("lang") == "python"
    assert "qwqwqw".replace('q', 'k', 2) == "kwkwqw"
    assert "_".join(strexp) == "q_w_e_r_t_y"
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


if __name__ == "__main__":
    main()
