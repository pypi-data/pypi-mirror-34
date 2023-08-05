# -*- coding: utf-8 -*-

import wx
import DynaUI as UI


# ======================================================= Harbor =======================================================
class Harbor(UI.Scrolled):
    def __init__(self, parent, size):
        super().__init__(parent, size=size, edge="H")
        self.AddScrollBar((0, 12))
        self.Outer = wx.Panel(self)
        self.Inner = wx.Panel(self.Outer, pos=(0, 0))
        self.Inner.R = self.R
        self.Inner.S = self.S
        self.Inner.L = self.L
        self.Inner.SetSizer(wx.BoxSizer(wx.VERTICAL))
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        MainSizer.Add(self.Outer, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 2)
        Sizer = wx.BoxSizer(wx.HORIZONTAL)
        Sizer.Add(MainSizer, 1, wx.EXPAND | wx.ALL, 4)
        Sizer.Add(UI.SETTINGS["SCROLL_DIAMETER"], 4)
        self.SetSizer(Sizer)

    # --------------------------------------
    def SetActualSize(self):
        super().SetActualSize()
        self.Inner.SetSize(self.ASize)

    def SetOffset(self, *args):
        super().SetOffset(*args)
        self.Inner.SetPosition((0, -self.GetViewPoint()[1]))

    def CalculateActualSize(self):
        return self.Outer.GetSize()[0], self.Inner.GetEffectiveMinSize()[1] + 36

    def OnSize(self):
        self.Inner.SetSize(wx.Size(self.Outer.GetSize()[0], self.Inner.GetEffectiveMinSize()[1] + 36))
        self.SetActualSize()

    # --------------------------------------
    def OnChild(self, child):
        show = not child.IsShown()
        child.Show(show)
        child.Sash.Show(show)
        child.Head.SetPic(self.R["AP_ABORT" if show else "AP_MINI"][0])
        self.SetActualSize()
        self.ReDraw()
