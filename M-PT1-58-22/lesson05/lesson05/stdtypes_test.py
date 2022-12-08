from typing import Hashable


def test_str() -> None:
    assert "pytho".ljust(6, "n") == "python"
    assert "plugnplay".partition("n") == ("plug", "n", "play")
    assert " ".isspace()
    assert "noise" in "white noise"
    assert "langpython".removeprefix("lang") == "python"
    assert "qwqwqw".replace("q", "k", 2) == "kwkwqw"
    assert "_".join("qwerty") == "q_w_e_r_t_y"
    assert "item"[1] == "t"
    assert "item".index("t") == 1
    assert "PYTHON".lower() == "python"
    assert "PYTHON".isupper()
    assert "creature,,,".removesuffix(",,,") == "creature"
    assert "python".islower()
    assert "csharp".translate({99: 110}) == "nsharp"
    assert " python ".strip() == "python"
    assert "error inside".find("inside") == 6
    assert "sssd".isidentifier()
    assert "12".isdigit()
    assert "ErRoR".swapcase() == "eRrOr"
    assert "qwe".center(7) == "  qwe  "
    assert "read only for".rsplit(" ", 1) == ["read only", "for"]
    assert "\u0033".isdecimal()
    assert "2233".isnumeric()
    assert "python".endswith("n")
    assert "ython".rjust(7, "p") == "ppython"
    assert "pyt{0}on".format("h") == "python"
    assert "text".isprintable()
    assert "title".title() == "Title"
    assert "text".isascii()
    assert "hohohohoho".rfind("h") == 8
    assert "hohohohoho".count("h") == 5
    assert "ErRoR".casefold() == "error"
    assert "NO\tRD".expandtabs(2) == "NO  RD"
    assert "11".zfill(4) == "0011"
    assert "Python".istitle()
    assert len("three") == 5
    assert "district13".isalnum()
    assert "python".maketrans("p", "c") == {112: 99}
    assert "out to in".rpartition("to") == ("out ", "to", " in")
    assert "{x}{y}".format_map({"x": "4", "y": "5"}) == "45"
    assert "pyt" + "hon" == "python"
    assert "python   ".rstrip() == "python"
    assert "pine#apple".split("#") == ["pine", "apple"]  # noqa: SIM905
    assert "Français".encode() == b"Fran\xc3\xa7ais"
    assert "python".startswith("p")
    assert "    python  ".lstrip() == "python  "
    assert isinstance("python", Hashable)
    assert "python".capitalize() == "Python"
    assert "%sq%s" % ("s", "l") == "sql"  # noqa: S001,MOD001
    assert "notnum".isalpha()
    assert "Three" * 3 == "ThreeThreeThree"
    assert "python".upper() == "PYTHON"
    assert "sci\nand\nfi".splitlines() == ["sci", "and", "fi"]
    assert "AAA" < "B"


def test_list() -> None:
    testing_list = [4, 2, 3]
    assert len(testing_list) == 3
    assert not isinstance(testing_list, Hashable)
    assert testing_list.copy() == [4, 2, 3]
    testing_list[1] = 5
    assert testing_list == [4, 5, 3]
    testing_list[2] = testing_list[2] * 3
    assert testing_list == [4, 5, 9]
    assert testing_list[0] + 3 == 7
    testing_list[0] = testing_list[0] + 3
    assert testing_list == [7, 5, 9]
    assert testing_list[0] * 2 == 14
    testing_list.extend([4, 2])
    assert testing_list == [7, 5, 9, 4, 2]
    testing_list.pop(1)
    assert testing_list == [7, 9, 4, 2]
    assert testing_list.index(9) == 1
    testing_list.reverse()
    assert testing_list == [2, 4, 9, 7]
    assert 2 in testing_list
    del testing_list[0]
    assert testing_list == [4, 9, 7]
    testing_list.sort()
    assert testing_list == [4, 7, 9]
    assert testing_list[1] == 7
    assert testing_list.count(4) == 1
    testing_list.remove(4)
    assert testing_list == [7, 9]
    testing_list.append(3)
    assert testing_list == [7, 9, 3]
    testing_list.insert(1, 8)
    assert testing_list == [7, 8, 9, 3]
    testing_list.clear()
    assert testing_list == []
    assert testing_list < [4, 6]
