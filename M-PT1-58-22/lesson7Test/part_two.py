def append(arg: list = []) -> list:
    name = arg
    name.append("+")
    return name

test_list = ["test"]
alice = append(test_list)
id_alice = id(alice)

bob = append(test_list)
id_bob = id(bob)

charlie = append(test_list)
id_charlie = id(charlie)

dan = append(test_list)
id_dan = id(dan)

assert not alice == []
assert alice == bob
assert bob is charlie
assert charlie is dan
assert len(dan) == 4

