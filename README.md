# PYtunl

## *NOTE:* PYtunl is not longer maintained. The Go version of this program can be used instead: https://github.com/cghdev/gotunl-vpn
PYtunl is a command line client for Pritunl written in Python.

At the moment is only supported in MacOS.

Usage:

```
usage: vpn.py [-h] [-l] [-c <profile>] [-d <profile>] [-o <format>]

Pritunl command line client.

optional arguments:
  -h, --help                            show this help message and exit
  -l, --list                            List connections.
  -c <profile>, --connect <profile>     Connects to <profile>.
  -d <profile>, --disconnect <profile>  Disconnects <profile> or "all".
  -o <format>, --output <format>        Selects output format for listing
                                        connections (json, table). Default
                                        "table".
```

Examples:
```
$ ./vpn.py -l
+------+------------------------+--------------+
|   ID | Name                   | Status       |
|------+------------------------+--------------|
|    1 | US VPN                 | Disconnected |
|    2 | UK VPN                 | Disconnected |
|    3 | Netherlands VPN        | Disconnected |
|    4 | Hong Kong VPN          | Disconnected |
|    5 | Test VPN               | Disconnected |
+------+------------------------+--------------+
$ ./vpn.py -c 3
$ ./vpn.py --connect "Test VPN"
Enter the username: user1
Enter the password:
$ ./vpn.py --list
+------+------------------------+--------------+
|   ID | Name                   | Status       |
|------+------------------------+--------------|
|    1 | US VPN                 | Disconnected |
|    2 | UK VPN                 | Disconnected |
|    3 | Netherlands VPN        | Connected    |
|    4 | Hong Kong VPN          | Disconnected |
|    5 | Test VPN               | Connected    |
+------+------------------------+--------------+
$ ./vpn.py -d all
```

