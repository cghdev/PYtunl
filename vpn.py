#!/usr/bin/env python

from pytunl import PYtunl
from docopt import docopt
import argparse
from tabulate import tabulate
import json
import sys


def listConnections(pt, out='table'):
    profs = []
    cons = pt.getConnections()
    for p in pt.profiles:
        status = 'Disconnected'
        if p in cons:
            status = cons[p]['status'].capitalize()
        profs.append([pt.profiles[p]['id'], pt.profiles[p]['name'], status])
    if out == 'table':
        print(tabulate(sorted(profs), headers=['ID', 'Name','Status'], tablefmt='psql'))
    elif out == 'json':
        j = {}
        for p in sorted(profs):
            j[str(p[0])] = {'name': p[1], 'status': p[2]}
        print json.dumps(j)

def disconnect(pt, id):
    if id == 'all':
        pt.stopConnections()
    else:
        for p in pt.profiles:
            if id == pt.profiles[p]['name'] or id == str(pt.profiles[p]['id']):
                pt.disconnectProfile(p)

def connect(pt, id):
    for p in pt.profiles:
        if id == pt.profiles[p]['name'] or id == str(pt.profiles[p]['id']):
            pt.connectProfile(p)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pritunl command line client.', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40))
    parser.add_argument('-l', '--list', action='store_true', help='List connections.')
    parser.add_argument('-c', '--connect', metavar='<profile>', help='Connects to <profile>.')
    parser.add_argument('-d', '--disconnect', metavar='<profile>', help='Disconnects <profile> or "all".')
    parser.add_argument('-o', '--output', metavar='<format>', help='Selects output format for listing connections (json, table). Default "table".')
    args = parser.parse_args()
    if not args.list and not args.connect and not args.disconnect:
        parser.print_help()
        exit(1)

    pt = PYtunl()
    if not pt.ping():
        print("[!] Error. Verify pritunl service is running and listening in port 9770.")
        exit(1)

    if args.list:
        out = 'table' if not args.output else args.output
        listConnections(pt, out)
    elif args.connect:
        connect(pt, args.connect)
    elif args.disconnect:
        disconnect(pt, args.disconnect)