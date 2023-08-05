""" State machine for Cimc """

__copyright__ = "# Copyright (c) 2017 by cisco Systems, Inc. All rights reserved."
__author__ = "Dave Wapstra <dwapstra@cisco.com>"


import re

from unicon.plugins.cimc.patterns import CimcPatterns

from unicon.statemachine import State, Path, StateMachine
from unicon.eal.dialogs import Dialog, Statement

from unicon.core.errors import SubCommandFailure, StateMachineError

from .statements import CimcStatements

patterns = CimcPatterns()
statements = CimcStatements()

default_statement_list = [statements.more_prompt_stmt,
                          statements.confirm_prompt_stmt,
                          statements.yes_no_stmt,
                          statements.enter_yes_or_no_stmt]


class CimcStateMachine(StateMachine):

    def __init__(self, hostname=None):
        super().__init__(hostname)

    def create(self):
        shell = State('shell', patterns.prompt)
        self.add_state(shell)
        self.add_default_statements(default_statement_list)
