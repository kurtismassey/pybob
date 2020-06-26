#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Payroll(BaseEndpoint):

    def history(self, department='', show_inactive=False):
        """
        Read payroll history

        Args:
            department (string): filter payroll for specific department
            show_inactive (bool): Show also inactive employees

        # TODO: response schema
        """
        return self.client.get(
            "people",
            query={
                'department': department,
                'showInactive': show_inactive
            }
        )
