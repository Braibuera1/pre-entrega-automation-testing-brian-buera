import pytest
from pages import LoginPage
from conftest import driver





@pytest.mark.login 
def test_login(driver):
    login = LoginPage(driver)
    login.abrir()
    assert login.driver.current_url == "https://www.saucedemo.com/"
    login.login_completo()
    assert 'inventory.html' in login.driver.current_url 
    print(f"Login OK -> {driver.current_url}")





    