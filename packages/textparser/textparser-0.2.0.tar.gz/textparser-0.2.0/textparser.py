# A text parser.

from collections import namedtuple


__author__ = 'Erik Moqvist'
__version__ = '0.2.0'


Token = namedtuple('Token', ['kind', 'value', 'line', 'column'])


class Error(Exception):
    pass


def markup_line(string, offset):
    begin = string.rfind('\n', 0, offset)
    begin += 1

    end = string.find('\n', offset)

    if end == -1:
        end = len(string)

    return string[begin:offset] + '>>!<<' + string[offset:end]


class TokenizerError(Error):

    def __init__(self, line, column, offset, string):
        message = 'Invalid syntax at line {}, column {}: "{}"'.format(
            line,
            column,
            markup_line(string, offset))
        super(TokenizerError, self).__init__(message)


def create_token_re(spec):
    return '|'.join([
        '(?P<{}>{})'.format(name, regex) for name, regex in spec
    ])


class _Tokens(object):

    def __init__(self, tokens):
        self._tokens = tokens
        self._pos = 0
        self._stack = []

    def get(self):
        pos = self._pos
        self._pos += 1

        return self._tokens[pos]

    def peek(self):
        return self._tokens[self._pos]

    def save(self):
        self._stack.append(self._pos)

    def restore(self):
        self._pos = self._stack.pop()

    def drop(self):
        self._stack.pop()

    def __repr__(self):
        return str(self._tokens[self._pos:self._pos + 2])


def _match_item(item, tokens):
    if isinstance(item, str):
        if item != tokens.peek().kind:
            return None
        else:
            return tokens.get().value
    else:
        return item.match(tokens)


class Sequence(object):
    """Matches a sequence of patterns.

    """

    def __init__(self, *members):
        self.members = members

    def match(self, tokens):
        matched = []

        for member in self.members:
            mo = _match_item(member, tokens)

            if mo is None:
                return None

            if isinstance(member, Inline) and isinstance(mo, list):
                matched.extend(mo)
            else:
                matched.append(mo)

        return matched


class Choice(object):
    """Matches any of given patterns.

    """

    def __init__(self, *members):
        self._members = members

    def match(self, tokens):
        for member in self._members:
            tokens.save()
            mo = _match_item(member, tokens)

            if mo is not None:
                tokens.drop()

                return mo

            tokens.restore()

        return None


class ChoiceDict(object):
    """Matches any of given patterns.

    """

    def __init__(self, *members):
        self._members_map = {}

        for member in members:
            if not isinstance(member, Sequence):
                raise RuntimeError()

            if not isinstance(member.members[0], str):
                raise RuntimeError()

            if member.members[0] in self._members_map:
                raise RuntimeError()

            self._members_map[member.members[0]] = member

    def match(self, tokens):
        return _match_item(self._members_map[tokens.peek().kind], tokens)


class ZeroOrMore(object):
    """Matches a pattern zero or more times.

    """

    def __init__(self, element, end=None):
        self._element = element
        self._end = end

    def match(self, tokens):
        matched = []

        try:
            while True:
                if self._end is not None:
                    tokens.save()
                    mo = _match_item(self._end, tokens)
                    tokens.restore()

                    if mo is not None:
                        break

                mo = _match_item(self._element, tokens)

                if mo is None:
                    break

                matched.append(mo)
        except KeyError:
            pass

        return matched


class OneOrMore(object):
    """Matches a pattern one or more times.

    """

    def __init__(self, element, end=None):
        self._element = element
        self._end = end

    def match(self, tokens):
        matched = []

        try:
            while True:
                if self._end is not None:
                    tokens.save()
                    mo = _match_item(self._end, tokens)
                    tokens.restore()

                    if mo is not None:
                        break

                mo = _match_item(self._element, tokens)

                if mo is None:
                    break

                matched.append(mo)
        except KeyError:
            pass

        if len(matched) > 0:
            return matched
        else:
            return None


class Any(object):
    """Matches any token.

    """

    def match(self, tokens):
        return tokens.get().value


class DelimitedList(object):
    """Matches a delimented list of given pattern.

    """

    def __init__(self, element, delim=','):
        self._element = element
        self._delim = delim

    def match(self, tokens):
        matched = []

        while True:
            # Element.
            mo = _match_item(self._element, tokens)

            if mo is None:
                if len(matched) == 0:
                    return []
                else:
                    return None

            matched.append(mo)

            # Delimiter.
            mo = _match_item(self._delim, tokens)

            if mo is None:
                return matched


class Inline(object):

    def __init__(self, element):
        self._element = element

    def match(self, tokens):
        return self._element.match(tokens)


class Forward(object):

    def __init__(self):
        self._inner = None

    def __ilshift__(self, other):
        self._inner = other

        return self

    def match(self, tokens):
        return self._inner.match(tokens)


class Grammar(object):
    """Creates a tree of given tokens.

    """

    def __init__(self, grammar):
        self._root = grammar

    def parse(self, tokens):
        tokens = _Tokens(tokens)

        try:
            parsed = self._root.match(tokens)
        except KeyError:
            parsed = None

        if parsed is not None and tokens.get().kind == '__EOF__':
            return parsed
        else:
            raise Error()


def choice(*members):
    try:
        return ChoiceDict(*members)
    except RuntimeError:
        return Choice(*members)
