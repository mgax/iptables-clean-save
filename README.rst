iptables-clean-save
===================
Script that invokes ``iptables-save``, cleans up its output, and writes
it to ``stdout``. Install like this::

    curl https://raw.github.com/mgax/iptables-clean-save/master/iptables_clean_save.py > /usr/local/bin/iptables-clean-save
    chmod +x /usr/local/bin/iptables-clean-save
