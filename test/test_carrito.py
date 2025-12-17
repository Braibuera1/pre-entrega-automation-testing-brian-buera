import pytest
from conftest import driver 
from pages  import LoginPage, InventoryPage, CartPage

@pytest.mark.carrito
def test_carrito(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo()
    catalogo_page = InventoryPage(login_page.driver)

    catalogo_page.agregar_primer_producto()

    carrito = catalogo_page.ir_al_carrito()

    assert "/cart.html" in carrito.driver.current_url
    print(f"URL Carrito OK ->{carrito.driver.current_url}")

    
