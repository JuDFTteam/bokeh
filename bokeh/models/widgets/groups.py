#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
'''

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports
from ...core.has_props import abstract
from ...core.properties import Bool, Instance, Int, List, String

from ..callbacks import Callback

from .buttons import ButtonLike
from .widget import Widget

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'AbstractGroup',
    'ButtonGroup',
    'CheckboxButtonGroup',
    'CheckboxGroup',
    'Group',
    'RadioButtonGroup',
    'RadioGroup',
)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

@abstract
class AbstractGroup(Widget):
    ''' Abstract base class for all kinds of groups.

    '''

    labels = List(String, help="""
    List of text labels contained in this group.
    """)

    def on_click(self, handler):
        ''' Set up a handler for button check/radio box clicks including
        the selected indices.

        Args:
            handler (func) : handler function to call when button is clicked.

        Returns:
            None

        '''
        self.on_change('active', lambda attr, old, new: handler(new))

    def js_on_click(self, handler):
        ''' Set up a handler for button check/radio box clicks including the selected indices. '''
        self.js_on_change('active', handler)

    callback = Instance(Callback, help="""
    A callback to run in the browser whenever a button group is manipulated.
    """)

@abstract
class ButtonGroup(AbstractGroup, ButtonLike):
    ''' Abstract base class for groups with items rendered as buttons.

    '''

@abstract
class Group(AbstractGroup):
    ''' Abstract base class for groups with items rendered as check/radio
    boxes.

    '''

    inline = Bool(False, help="""
    Should items be arrange vertically (``False``) or horizontally
    in-line (``True``).
    """)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class CheckboxGroup(Group):
    ''' A group of check boxes.

    '''

    active = List(Int, help="""
    The list of indices of selected check boxes.
    """)

class RadioGroup(Group):
    ''' A group of radio boxes.

    '''

    active = Int(None, help="""
    The index of the selected radio box, or ``None`` if nothing is
    selected.
    """)

class CheckboxButtonGroup(ButtonGroup):
    ''' A group of check boxes rendered as toggle buttons.

    '''

    active = List(Int, help="""
    The list of indices of selected check boxes.
    """)

class RadioButtonGroup(ButtonGroup):
    ''' A group of radio boxes rendered as toggle buttons.

    '''

    active = Int(None, help="""
    The index of the selected radio box, or ``None`` if nothing is
    selected.
    """)

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
