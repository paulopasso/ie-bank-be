from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'France')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_edit_account():
    """
    GIVEN an Account model
    WHEN the account's fields are updated
    THEN check that the fields are updated correctly
    """
    account = Account('John Doe', '€', 'France')

    account.name = 'Jane Doe'
    account.country = 'Germany'

    assert account.name == 'Jane Doe'
    assert account.country == 'Germany'
