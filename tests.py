from iptables_clean_save import clean


def test_remove_comments():
    rulestext = ("# comment one\n"
                 "   # comment two\n"
                 "some stuff here\n")
    assert clean(rulestext) == "some stuff here\n"
