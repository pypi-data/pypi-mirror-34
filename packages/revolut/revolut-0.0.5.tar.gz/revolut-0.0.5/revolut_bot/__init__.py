# -*- coding: utf-8 -*-
"""
This package allows you to control the Revolut bot
"""

import csv
from revolut import Amount, Transaction
from datetime import datetime
import io

_CSV_COLUMNS = ["date", "hour", "from_amount", "from_currency",
                "to_amount", "to_currency"]


def csv_to_dict(csv_str, separator=","):
    """ From a csv string, returns a list of dictionnaries
>>> csv_to_dict("a,b,c\\n1,2,3")
[{'a': '1', 'b': '2', 'c': '3'}]
>>> csv_to_dict("a,b,c\\n1,2,3\\n4,5,6")
[{'a': '1', 'b': '2', 'c': '3'}, {'a': '4', 'b': '5', 'c': '6'}]
>>> csv_to_dict("a;b;c\\n1;2;3", separator=";")
[{'a': '1', 'b': '2', 'c': '3'}]"""
    dict_list = []
    reader = csv.DictReader(io.StringIO(csv_str), delimiter=separator)
    for line in reader:
        dict_list.append(dict(line))
        # By default, DictReader returns OrderedDict => convert to dict
    return dict_list


def append_dict_to_csv(filename, dict_obj, separator=",",
                       col_names=_CSV_COLUMNS):
    """ Append a dict object, to a csv file """
    with open(filename, 'a', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile,
                                delimiter=separator,
                                fieldnames=col_names,
                                lineterminator='\n')  # To avoid '^M'
        writer.writerow(dict_obj)
    return


def convert_Transaction_to_dict(transaction_obj):
    tr_dict = {}
    tr_dict["date"] = transaction_obj.date.strftime("%d/%m/%Y")
    tr_dict["hour"] = transaction_obj.date.strftime("%H:%M:%S")
    tr_dict["from_amount"] = transaction_obj.from_amount.real_amount
    tr_dict["from_currency"] = transaction_obj.from_amount.currency
    tr_dict["to_amount"] = transaction_obj.to_amount.real_amount
    tr_dict["to_currency"] = transaction_obj.to_amount.currency
    return tr_dict


def update_historyfile(filename, exchange_transaction):
    """ Update the history file with an exchange transaction """
    tr_dict = convert_Transaction_to_dict(transaction_obj=exchange_transaction)
    append_dict_to_csv(filename=filename, dict_obj=tr_dict)
    return


def read_file_to_str(filename):
    with open(filename, 'r') as f:
        ret_str = f.read()
    return ret_str


def get_last_transactions_from_csv(filename="exchange_history.csv",
                                   separator=","):
    csv_str = read_file_to_str(filename=filename)
    last_transactions = csv_to_dict(csv_str=csv_str, separator=separator)

    tr_list = []
    for tr in last_transactions:
        tr_obj = dict_transaction_to_Transaction(tr)
        tr_list.append(tr_obj)

    return tr_list


def dict_transaction_to_Transaction(tr_dict):
    """ Converts a transaction dictionnary to a Transaction object """
    if list(tr_dict.keys()) != _CSV_COLUMNS:
        raise TypeError("Columns expected : {}\n{} received".format(
                _CSV_COLUMNS, list(tr_dict.keys())))
    str_date = "{} {}".format(tr_dict["date"],
                              tr_dict["hour"])
    tr = Transaction(from_amount=Amount(
                    real_amount=float(tr_dict["from_amount"]),
                    currency=tr_dict["from_currency"]),
                to_amount=Amount(
                    real_amount=float(tr_dict["to_amount"]),
                    currency=tr_dict["to_currency"]),
                date=datetime.strptime(str_date, "%d/%m/%Y %H:%M:%S"))
    return tr


def get_amount_with_margin(amount, percent_margin):
    """ Returns the amount with a margin
>>> print(get_amount_with_margin(amount=Amount(real_amount=100,\
currency="EUR"), percent_margin=1))
101.00 EUR
"""
    if type(amount) != Amount:
        raise TypeError
    if type(percent_margin) not in [float, int]:
        raise TypeError
    margin = percent_margin/100

    amount_with_margin = amount.real_amount * (1 + margin)

    return Amount(real_amount=amount_with_margin, currency=amount.currency)
