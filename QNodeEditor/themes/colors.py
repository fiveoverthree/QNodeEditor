"""
Base classes for color properties of objects in the scene
"""

from PyQt5.QtGui import QColor


class NodeColor:
    """Saves color attributes for a node"""
    node_color_body: QColor
    """QColor: Color of node body"""
    node_color_header: QColor
    """QColor: Color of node header (behind title)"""
    node_color_outline_default: QColor
    """QColor: Color of node outline in default state"""
    node_color_outline_hovered: QColor
    """QColor: Color of node outline in hovered state"""
    node_color_outline_selected: QColor
    """QColor: Color of node outline in selected state"""
    node_color_shadow: QColor
    """QColor: Color of node shadow"""
    node_color_title: QColor
    """QColor: Color of node title text"""

class SocketColor:
    """Saves color attributes for a socket"""
    socket_color_fill: QColor
    """QColor: Color of socket types"""
    socket_color_outline: QColor
    """QColor: Color of socket outline"""