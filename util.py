import sys


def get_list_from_file(filename):
    items = []
    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                continue
            items.append(line.rstrip('\n'))

    return items


def check_option():
    argvs = sys.argv[1:]
    options = ['db', 'syslog', 'mail']

    real_options = []

    for argv in argvs:
        if argv not in options:
            print("unkown option: %s" % argv)
        else:
            real_options.append(argv)

    return real_options
