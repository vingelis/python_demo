import argparse


def dest_():
    # Most ArgumentParser actions add some value as an attribute of the object returned by parse_args().
    # The name of this attribute is determined by the dest keyword argument of add_argument().
    # For positional argument actions, dest is normally supplied as the first argument to add_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('bar')
    args = parser.parse_args(['XXX'])
    print(args)

    # For optional argument actions, the value of dest is normally inferred from the option strings.
    # ArgumentParser generates the value of dest by taking the first long option string and stripping away the initial -- string.
    # If no long option strings were supplied, dest will be derived from the first short option string by stripping the initial - character.
    # Any internal - characters will be converted to _ characters to make sure the string is a valid attribute name.
    # The examples below illustrate this behavior:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo-bar', '--foo')
    parser.add_argument('-x', '-y')
    args = parser.parse_args('-f 1 -x 2'.split())
    print(args)
    args = parser.parse_args('--foo 1 -y 2'.split())
    print(args)

    # dest allows a custom attribute name to be provided:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', dest='bar')
    args = parser.parse_args('--foo XXX'.split())
    print(args)


if __name__ == '__main__':
    dest_()
