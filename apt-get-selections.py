#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# this made for python3
import subprocess as sp
import re

class AptgetSelection:
    """ """
    DEBUG = True

    def __init__(self, dpkg_lFile='../dpkg-l.txt'):
        self.pkgedFile = dpkg_lFile
        self.pkgformat = '\\w,\\d,\.,\-,\:,\+'
        pass

    def do(self):
        now = sp.check_output('dpkg --get-selections', shell=True).decode('ascii', 'ignore')
        _print('Now Installed:')
        installed = now.split('\n')
        willbeSet = None
        with open(self.pkgedFile, 'r') as pkg:
            p = re.compile('^([\\w,\\d,\.,\-,\:,\+]+)\\t+install$')
            raspi_installed = []
            for ii in installed:
                _print(ii)
                m = p.match(ii)
                if m is not None:
                    raspi_installed.append(m.groups()[0])
            p2 = re.compile('^ii\\s{2}([\\w,\\d,\.,\-,\:,\+]+).+$')
            willbe = []
            for p in pkg.readlines():
                m = p2.match(p)
                if m is not None:
                    instPkg = m.groups()[0]
                    if not instPkg in raspi_installed:
                        willbe.append(instPkg)
            willbeSet = frozenset(willbe)
        for w in willbeSet:
            print('-> ' + w)
            sp.call('apt-get -y install %s'%w, shell=True)
        pass

    def finalize(self):
        sp.call('dpkg -l > %s'%self.pkgedFile, shell=True)
        pass

def _print(str, flag=AptgetSelection.DEBUG):
    if flag:
        print(str)
    pass


if __name__ == '__main__':
    ins = AptgetSelection()
    ins.do()
    ins.finalize()
