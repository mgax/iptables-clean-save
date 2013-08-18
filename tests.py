from iptables_clean_save import clean


def test_remove_comments():
    rulestext = ("# comment one\n"
                 "   # comment two\n"
                 "some stuff here\n")
    assert clean(rulestext) == "some stuff here\n"


def test_remove_counters():
    rulestext = ":FORWARD ACCEPT [100:200]\n"
    assert clean(rulestext) == ":FORWARD ACCEPT\n"
