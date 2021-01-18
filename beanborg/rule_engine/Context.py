#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Context:
    # rule file
    rules: str
    # custom rules folder
    rules_dir: str
    date_fomat: str
    default_expense: str
    date_pos: int
    payee_pos: int
    tx_type_pos: int
    account_pos: int

    account: str
    # decision tables
    payees: ()
    assets: ()
    accounts: ()