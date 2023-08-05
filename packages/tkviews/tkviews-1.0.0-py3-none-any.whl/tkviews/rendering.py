'''Customizing of tk parsing'''

from tkinter import Checkbutton, Radiobutton, Entry
from tkinter.ttk import Widget as TtkWidget
from pyviews.core.xml import XmlAttr
from pyviews.core.node import RenderArgs
from pyviews.rendering.core import create_inst, render_step, apply_attribute
from tkviews.node import WidgetNode
from tkviews.widgets import CheckbuttonNode, RadiobuttonNode, EntryNode
from tkviews.ttk import TtkWidgetNode

def convert_to_node(inst, args: RenderArgs):
    '''Wraps instance with WidgetNode'''
    args['widget'] = inst
    node_class = WidgetNode
    if isinstance(inst, Entry):
        node_class = EntryNode
    if isinstance(inst, Checkbutton):
        node_class = CheckbuttonNode
    if isinstance(inst, Radiobutton):
        node_class = RadiobuttonNode
    if isinstance(inst, TtkWidget):
        node_class = TtkWidgetNode
    return create_inst(node_class, args)

@render_step('xml_node')
def apply_text(node: WidgetNode, xml_node=None):
    '''Applies xml node content to WidgetNode'''
    if xml_node.text is None or not xml_node.text.strip():
        return
    text_attr = XmlAttr('text', xml_node.text)
    apply_attribute(node, text_attr)
