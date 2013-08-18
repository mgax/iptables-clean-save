from iptables_clean_save import clean


def test_remove_comments():
    rulestext = ("# comment one\n"
                 "   # comment two\n"
                 "some stuff here\n")
    assert clean(rulestext) == "some stuff here\n"


def test_remove_counters():
    rulestext = ":FORWARD ACCEPT [100:200]\n"
    assert clean(rulestext) == ":FORWARD ACCEPT\n"


def test_remove_automatic_modules():
    rulestext = (
        '-A INPUT -p icmp -m icmp --icmp-type 8 '
                '-m comment --comment "foo" -j ACCEPT\n'
        '-A INPUT -p udp -m udp --dport 10604 '
                '-m comment --comment "bar" -j ACCEPT\n'
        '-A INPUT -p tcp -m tcp --dport 28410 '
                '-m comment --comment "baz" -j ACCEPT\n')
    expected_output = (
        '-A INPUT -p icmp --icmp-type 8 -m comment --comment "foo" -j ACCEPT\n'
        '-A INPUT -p udp --dport 10604 -m comment --comment "bar" -j ACCEPT\n'
        '-A INPUT -p tcp --dport 28410 -m comment --comment "baz" -j ACCEPT\n')
    assert clean(rulestext) == expected_output


def test_insert_blank_line_between_tables():
    rulestext = ('*nat\n'
                 '-A PREROUTING blah blah\n'
                 '*filter\n'
                 '-A INPUT blah blah\n')
    expected_output = ('*nat\n'
                       '-A PREROUTING blah blah\n'
                       '\n'
                       '*filter\n'
                       '-A INPUT blah blah\n')
    assert clean(rulestext) == expected_output
