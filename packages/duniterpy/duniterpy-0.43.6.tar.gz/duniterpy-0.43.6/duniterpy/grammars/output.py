from ..documents.constants import pubkey_regex
from ..documents.constants import hash_regex
from pypeg2 import *


class Pubkey(str):
    regex = re.compile(pubkey_regex)


class Hash(str):
    regex = re.compile(hash_regex)


class Int(str):
    regex = re.compile(r"[0-9]+")


class SIG(str):
    grammar = "SIG(", attr('pubkey', Pubkey), ")"

    @classmethod
    def token(cls, pubkey):
        sig = cls()
        sig.pubkey = pubkey
        return sig

    def compose(self, parser, grammar=None, attr_of=None):
        return "SIG({0})".format(self.pubkey)


class CSV(str):
    grammar = "CSV(", attr('time', Int), ")"

    @classmethod
    def token(cls, time):
        csv = cls()
        csv.time = str(time)
        return csv

    def compose(self, parser, grammar=None, attr_of=None):
        return "CSV({0})".format(self.time)


class CLTV(str):
    grammar = "CLTV(", attr('timestamp', Int), ")"

    @classmethod
    def token(cls, timestamp):
        cltv = cls()
        cltv.timestamp = str(timestamp)
        return cltv

    def compose(self, parser, grammar=None, attr_of=None):
        return "CLTV({0})".format(self.timestamp)


class XHX(str):
    grammar = "XHX(", attr('sha_hash', Hash), ")"

    @classmethod
    def token(cls, sha_hash):
        xhx = cls()
        xhx.sha_hash = sha_hash
        return xhx

    def compose(self, parser, grammar=None, attr_of=None):
        return "XHX({0})".format(self.sha_hash)


class Operator(Keyword):
    grammar = Enum(K("&&"), K("||"), K("AND"), K("OR"))
    regex = re.compile(r"[&&|\|\||\w]+")

    @classmethod
    def token(cls, keyword):
        op = cls(keyword)
        return op

    def compose(self, parser, grammar=None, attr_of=None):
        return "{0}".format(self.name)


class Condition(str):
    @classmethod
    def token(cls, left, op=None, right=None):
        condition = cls()
        condition.left = left
        if op:
            condition.op = op
        if right:
            condition.right = right
        return condition

    def compose(self, parser, grammar=None, attr_of=None):
        if type(self.left) is Condition:
            left = "({0})".format(parser.compose(self.left, grammar=grammar, attr_of=attr_of))
        else:
            left = parser.compose(self.left, grammar=grammar, attr_of=attr_of)

        if getattr(self, 'op', None):

            if type(self.right) is Condition:
                right = "({0})".format(parser.compose(self.right, grammar=grammar, attr_of=attr_of))
            else:
                right = parser.compose(self.right, grammar=grammar, attr_of=attr_of)
            op = parser.compose(self.op, grammar=grammar, attr_of=attr_of)
            result = "{0} {1} {2}".format(left, op, right)
        else:
            result = left
        return result

Condition.grammar = contiguous(attr('left', [SIG, XHX, CSV, CLTV, ('(', Condition, ')')]),
                     maybe_some(whitespace, attr('op', Operator), whitespace,
                               attr('right', [SIG, XHX, CSV, CLTV, ('(', Condition, ')')])))
