#!/usr/bin/env python3
# -*- coding: utf8 -*-
from client import Client


class BaseEndpoint:
    """
    Base class for all endpoints
    """

    def __init__(self, client: Client):
        self.client = client
