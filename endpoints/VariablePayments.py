#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class VariablePayments(BaseEndpoint):
    pass

    def list(self, employee_id):
        """
        List employee's variable payments
        Returns a list of variable payments for a given employee.

        Args:
            employee_id (str): employee id
        """
        return self.client.get(
            'people/{employee_id}/variable'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            amount_value,
            amount_currency,
            pay_type,
            payment_period
    ):
        """
        Creates a new variable payment for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            amount_value (float):
            amount_currency (str): 3 letter currency code
            pay_type (str): The type of the variable pay
            payment_period (str): represents the period for this variable entry.
                One of: Annual, Half-Yearly, Quarterly, Monthly
        """
        return self.client.post(
            'people/{employee_id}/variable'.format(
                employee_id=employee_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'amount': {
                    'value': amount_value,
                    'currency': amount_currency,
                },
                'type': pay_type,
                'paymentPeriod': payment_period
            }
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes a variable payment for an employee

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete
        """
        return self.client.delete(
            'people/{employee_id}/variable/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            )
        )
