'''Tkinter widgets nodes'''

from tkinter import Tk, Widget
from pyviews.core.ioc import inject
from pyviews.core.xml import XmlNode
from pyviews.core.node import Node, RenderArgs
from tkviews.geometry import Geometry

class TkRenderArgs(RenderArgs):
    '''RenderArgs for WidgetNode'''
    def __init__(self, xml_node, parent_node=None, widget_master=None):
        super().__init__(xml_node, parent_node)
        self['master'] = widget_master

    def get_args(self, inst_type=None):
        if issubclass(inst_type, Widget):
            return RenderArgs.Result([self['master']], {})
        return super().get_args(inst_type)

class WidgetNode(Node):
    '''Wrapper under tkinter widget'''
    def __init__(self, widget, xml_node: XmlNode, parent_context=None):
        super().__init__(xml_node, parent_context)
        self.widget = widget
        self._geometry = None
        self._style = ''

    @property
    def geometry(self) -> Geometry:
        '''Geometry'''
        return self._geometry

    @geometry.setter
    def geometry(self, value: Geometry):
        if self._geometry:
            self._geometry.forget()
        self._geometry = value
        if value is not None:
            value.apply(self.widget)

    @property
    def style(self):
        '''Widget style'''
        return self._style

    @style.setter
    @inject('apply_styles')
    def style(self, value, apply_styles=None):
        self._style = value
        apply_styles(self, value)

    def get_render_args(self, xml_node: XmlNode):
        return TkRenderArgs(xml_node, self, self.widget)

    def destroy(self):
        super().destroy()
        self.widget.destroy()

    def bind(self, event, command):
        '''Calls widget's bind'''
        self.widget.bind('<'+event+'>', command)

    def bind_all(self, event, command):
        '''Calls widget's bind_all'''
        self.widget.bind_all('<'+event+'>', command, '+')

    def set_attr(self, key, value):
        '''Applies passed attribute'''
        if hasattr(self, key):
            setattr(self, key, value)
        elif hasattr(self.widget, key):
            setattr(self.widget, key, value)
        else:
            self.widget.configure(**{key:value})

    def call(self, key, args):
        '''Calls method by key'''
        if hasattr(self, key):
            getattr(self, key)(*args)
        elif hasattr(self.widget, key):
            getattr(self.widget, key)(*args)

class Root(WidgetNode):
    '''Wrapper under tkinter Root'''
    def __init__(self, xml_node: XmlNode):
        super().__init__(Tk(), xml_node)
        self._icon = None

    @property
    def state(self):
        '''Widget state'''
        return self.widget.state()

    @state.setter
    def state(self, state):
        self.widget.state(state)

    @property
    def icon(self):
        '''Icon path'''
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.widget.iconbitmap(default=value)
