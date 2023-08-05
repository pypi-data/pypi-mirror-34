# -*- coding: utf-8 -*-

__all__ = [
    "LegitLink",
    "ANCHOR_REGULAR",
    "ANCHOR_SPECIAL",
    "ANCHOR_ALL",
    "ANCHOR_NONE"
]


# =============================================== AnchorType & LegitLink ===============================================
class ANCHOR_REGULAR(object):
    pass


class ANCHOR_SPECIAL(object):
    pass


class ANCHOR_ALL(ANCHOR_SPECIAL):
    pass


class ANCHOR_NONE(ANCHOR_SPECIAL):
    pass


class _LegitLink(object):
    _SharedState = {}

    def __init__(self):
        self.__dict__ = self._SharedState
        self.links = {}

    def __call__(self, a1, a2):  # TODO deal with subclass
        if issubclass(a1.aType, ANCHOR_SPECIAL) and issubclass(a2.aType, ANCHOR_SPECIAL):
            return False
        if a1.GetType() == ANCHOR_NONE or a2.GetType() == ANCHOR_NONE:
            return False
        if a1.GetType() == ANCHOR_ALL or a2.GetType() == ANCHOR_ALL:
            return a1.send != a2.send
        if a1.recv and a2.send:
            return a1.GetType() in self.links.get(a2.GetType(), {})
        if a1.send and a2.recv:
            return a2.GetType() in self.links.get(a1.GetType(), {})
        return False

    def Add(self, source, target, reverse=False, onTransferForward=None, onTransferReverse=None):
        if source is target:
            reverse = False
        if source not in self.links:
            self.links[source] = {}
        if target not in self.links[source]:
            self.links[source][target] = onTransferForward
        else:
            raise Exception
        if reverse:
            self.Add(target, source, False, onTransferReverse)

    def Del(self, source, target, reverse=False):
        if source is target:
            reverse = False
        if target in self.links[source]:
            del self.links[source][target]
        if not self.links[source]:
            del self.links[source]
        if reverse:
            self.Del(target, source, False)

    def Transfer(self, source, target):
        return self.links.get(source, {}).get(target, None)


LegitLink = _LegitLink()


# ======================================================== Link ========================================================
class Link(object):
    __slots__ = ["source", "target", "pen"]
    __TYPE__ = "LINK"

    def __init__(self, source, target, pen):
        self.source = source
        self.target = target
        self.pen = pen

    def Disconnect(self):
        self.source.RemoveTarget(self.target)

    def GetXY(self):
        x1, y1 = self.source.x + 3, self.source.y + 3
        x2, y2 = self.target.x + 3, self.target.y + 3
        c = (x1 + x2) / 2
        c1 = max(c, x1 + 32)
        c2 = min(c, x2 - 32)
        return x1, y1, x2, y2, c1, c2

    def GetName(self):
        return "[%s].[%s] --> [%s].[%s]" % (self.source.Widget.NAME, self.source.name, self.target.Widget.NAME, self.target.name)
