#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Tasks(BaseEndpoint):

    def list(self):
        """
        Read all open tasks

        # TODO: response schema
        """
        return self.client.get('tasks')

    def my_tasks(self):
        """
        Read tasks of the logged-in user

        # TODO: response schema
        """
        return self.client.get('my/tasks')
