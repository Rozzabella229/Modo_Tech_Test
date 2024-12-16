import pytest
from ASKBOSCO_Class import Client

def test_client_initialization():
    client = Client(client_code="test_client", display_name="Test Client")
    assert client.client_code == "test_client"
    assert client.display_name == "Test Client"
    assert client.is_active
    assert client.settings == {}

def test_client_invalid_code():
    with pytest.raises(ValueError):
        Client(client_code="123_invalid", display_name="Invalid Client")

def test_client_pause_and_enable():
    client = Client(client_code="test_client", display_name="Test Client")
    client.pause()
    assert not client.is_active
    client.enable()
    assert client.is_active

def test_client_partner_agency_assignment():
    client = Client(client_code="test_client", display_name="Test Client")
    client.assign_partner_agency("Agency A")
    assert client.partner_agency == "Agency A"

def test_client_set_business_type():
    client = Client(client_code="test_client", display_name="Test Client")
    client.set_business_type("ecommerce")
    assert client.business_type == "ecommerce"

    with pytest.raises(ValueError):
        client.set_business_type("invalid_type")
