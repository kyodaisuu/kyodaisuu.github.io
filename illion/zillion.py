#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# zillion.py - show name of N'th zillion number
#
# Published at https://kyodaisuu.github.io/illion/
# For detailed explanation, see this site.
#
# Author: Fish https://googology.wikia.org/wiki/User:Kyodaisuu
# MIT license

DESCRIPTION = "show name of N'th zillion number"
ISOLATE = ['', 'mi', 'bi', 'tri', 'quadri',
           'quinti', 'sexti', 'septi', 'octi', 'noni']
CW_UNI = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'se',
          'septe', 'octo', 'nove']  # quinqua is changed to quin
TEN = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta',
       'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti',
       'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']
SIMP_UNI = ['', 'un', 'duo', 'tre', 'quattuor',
            'quin', 'sex', 'septen', 'octo', 'novem']
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']


def main():
    import argparse
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('N', type=int, nargs='*',
                        help='N values. If 2 values are given, all values between them.')
    parser.add_argument('-m', '--modified',
                        action='store_true', help='use modified system')
    parser.add_argument('-t', '--table', action='store_true',
                        help='show html table')
    parser.add_argument('-d', '--definition',
                        action='store_true', help='show definition table')
    args = parser.parse_args()
    n = args.N
    if len(n) == 2:
        n = list(range(n[0], n[1]+1))
    if args.table:
        show_html(n)
        return
    if args.definition:
        show_definition(args.modified)
    for i in n:
        print('N={0} 10^{1} (10^{2} in long scale) {3}'.format(
            i, 3*i+3, 6*i, llion(i, args.modified)))


def show_html(n):
    print('<table>\n<tr><th>N <th>short scale <th>long scale <th>Conway-Wechsler system <th>Modified system')
    for i in n:
        c = llion(i, False)
        m = llion(i, True)
        if c == m:
            print(
                '<tr><td>{0} <td>10<sup>{1}</sup> <td>10<sup>{2}</sup> <td colspan="2" align="center">{3}</tr>'.format(i, 3*i+3, 6*i, c))
        else:
            print(
                '<tr><td>{0} <td>10<sup>{1}</sup> <td>10<sup>{2}</sup> <td align="center">{3} <td align="center">{4}</tr>'.format(i, 3*i+3, 6*i, c, m))
    print('</table>')


def show_definition(modified):
    print('<table>\n<tr><th>N <th>units <th>tens <th>hundreds')
    for i in range(1, 10):
        if modified:
            unit = SIMP_UNI[i]
        else:
            unit = CW_UNI[i]
            if i == 5:
                unit = unit + ' (**)'
            if i in [3, 6, 7, 9]:
                unit = unit + ' (*)'
        ten = TEN[i]
        hun = HUN[i]
        if not modified:
            if len(PREC_TEN[i]) > 0:
                ten = '<sup>' + PREC_TEN[i] + '</sup> ' + ten
            if len(PREC_HUN[i]) > 0:
                hun = '<sup>' + PREC_HUN[i] + '</sup> ' + hun
        print(
            '<tr><td>{0} <td>{1} <td>{2} <td>{3}</tr>'.format(i, unit, ten, hun))
    print('</table>')
    if not modified:
        print('<p><sup>*</sup>Note: when it is immediately before a component marked with <sup>S</sup> or <sup>N</sup>, "tre" increases to "tres" and "se" to "ses" or "sex" as appropriate. Similarly "septe" and "nove" increase to "septem" and "novem" or "septen" and "noven" immediately before components marked with <sup>M</sup> or <sup>N</sup>.</p>')
        print('<p><sup>**</sup>quin is changed from original quinqua.</p>')


def llion(n, modified):
    if n < 1:
        return 'N<1 is not defined'
    if n < 10:
        return ISOLATE[n] + 'llion'
    name = 'llion'
    while n > 999:
        if n % 1000 == 0:
            if name == 'llion':
                name = 'nillion'
            else:
                name = 'nilli' + name
        else:
            if n % 1000 < 10:
                name = ISOLATE[n % 1000] + name
            else:
                name = base(n % 1000, modified) + name
        n = n // 1000
    if n < 10:
        name = ISOLATE[n] + 'lli' + name
    else:
        name = base(n, modified) + name
    return name


def base(n, modified):
    unit = n % 10
    ten = (n//10) % 10
    hun = n//100
    if ten == 0:
        prec = PREC_TEN[hun]
    else:
        prec = PREC_HUN[ten]
    if modified:
        name = SIMP_UNI[unit]
    else:
        name = CW_UNI[unit]
        if unit == 3 or unit == 6:
            if 'S' in prec:
                name += 's'
            if 'X' in prec:
                if unit == 3:
                    name = 'tres'
                else:
                    name = 'sex'
        if unit == 7 or unit == 9:
            if 'M' in prec:
                name += 'm'
            if 'N' in prec:
                name += 'n'
    name += TEN[ten]
    name += HUN[hun]
    return name


if __name__ == "__main__":
    main()
