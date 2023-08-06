#!/usr/bin/env python3
import sys
import re
import argparse

def get_parameters():
    parser = argparse.ArgumentParser(description='to extract specific lines from the subject file which maps the query ids.   written by Guanliang MENG')

    parser.add_argument('-q', dest='query_ids', metavar='<str>', nargs="+",
        required=False, help='query list')

    parser.add_argument('-f', dest='fh_query', metavar='<query file>',
        required=False, type=argparse.FileType('r'), help='query list file')

    parser.add_argument('-s', dest='fh_subject', metavar='<subject file>', 
        default=sys.stdin, type=argparse.FileType('r'), nargs='?', 
        help='subject file [stdin]')

    parser.add_argument('-s1', dest='q_sep', metavar='<pattern>',
        required=False, default="\s+", 
        help='query file sep_pattern [%(default)s]')

    parser.add_argument('-s2', dest='s_sep', metavar='<pattern>',
        required=False, default="\s+", 
        help='subject file sep_pattern [%(default)s]')

    parser.add_argument('-d1', dest='query_field', metavar='<int>',
        nargs='?', type=int, default=0,
        help='which field in the query_file is to used? [%(default)s]')

    parser.add_argument('-d2', dest='subject_field', metavar='<int>',
        nargs='?', type=int, default=0,
        help='which field in the subject_file is to used? [%(default)s]')

    parser.add_argument('-o', dest='fhout', metavar='<outfile>', nargs='?', 
        default=sys.stdout, type=argparse.FileType('w'), 
        help="outfile [stdout]")

    parser.add_argument('-v', dest='invert', action='store_true',
        default=False, help="invert the output [%(default)s]")

    parser.add_argument('-V', dest='verbose', action='store_true',
        default=False, help='verbose output')

    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    if not args.fh_query and not args.query_ids:
        sys.exit('you must set -q or -f option!\n')

    if args.fh_query and args.query_ids:
        sys.exit('you can not set -q and -f options at the same time!\n')

    return args


def get_query(fh_query=None, field=0, sep_pattern="\s+", verbose=False):
    queries = {}
    for i in fh_query:
        i = i.strip()
        if not i:
            continue
        line = re.split(sep_pattern, i)
        try:
            queryid = line[field]
        except:
            print('cannot split this line:\n', line, file=sys.stderr)
            continue
        queries[queryid] = 1

    if verbose:
        print('there are {0} query ids'.format(len(queries)), file=sys.stderr)

    return queries


def get_lines(fh_subject=None, queries=None, field=0, sep_pattern="\s+", fhout=None, invert=False, verbose=False):
    count = 0
    for i in fh_subject:
        i = i.strip()
        if not i:
            continue
        line = re.split(sep_pattern, i)
        try:
            queryid = line[field]
        except:
            continue

        if not invert and queryid in queries:
            print(i, file=fhout)
            queries[queryid] = 0
            count += 1
        if invert and queryid not in queries:
            print(i, file=fhout)
            queries[queryid] = 0
            count += 1

    if verbose:
        print('found {0} records in subject file'.format(count), 
            file=sys.stderr)

        query_not_found = list(filter(lambda x:queries[x], queries.keys()))
        if len(query_not_found) > 0:
            print('\nthe following {0} query_ids not found in the subject_file:'.format(len(query_not_found)), file=sys.stderr)
            for queryid in query_not_found:
                print(queryid, file=sys.stderr)


def main():
    args = get_parameters()

    if args.fh_query:
        queries = get_query(fh_query=args.fh_query, field=args.query_field, 
            sep_pattern=args.q_sep, verbose=args.verbose)
    else:
        queries = {}
        for queryid in args.query_ids:
            queries[queryid] = 1

    get_lines(fh_subject=args.fh_subject, queries=queries, 
        field=args.subject_field, sep_pattern=args.s_sep, 
        fhout=args.fhout, invert=args.invert, verbose=args.verbose)


if __name__ == '__main__':
    main()






