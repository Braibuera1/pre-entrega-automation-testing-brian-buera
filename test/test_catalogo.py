import pytest
from pages import InventoryPage, LoginPage
from conftest import driver






@pytest.mark.catalogo
def test_catalogo (driver):
    index = LoginPage(driver)
    index.abrir()
    index.login_completo()
    catalogo_page = InventoryPage(index.driver)
    title = catalogo_page.obtener_titulo()
    assert title == "Products"
    print(f"Titulo de seccion OK ->{title}")

    #Verificar que existan los elementos
    assert catalogo_page.verificar_elemento(catalogo_page._FILTER_BUTTON) == True
    assert catalogo_page.verificar_elemento(catalogo_page._MENU_BUTTON) == True
    assert catalogo_page.verificar_elemento(catalogo_page._ADD_BUTTONS) == True

    #Contar productos visibles
    productos = catalogo_page.obtener_productos()
    assert len(productos) >= 1
    print(f"Se encontraron {len(productos)} productos.")

    #Mostrar nombre y precio del primer producto
    nombre,precio = catalogo_page.get_nombre_precio(0)
    assert nombre == "Sauce Labs Backpack" and precio == "$29.99"
    print(f"Primer producto: {nombre} - Precio: {precio}")

    catalogo_page.agregar_primer_producto()
    #Obtener numero de contador del carrito
    contador_carrito= catalogo_page.obtener_contador_carrito()
    assert contador_carrito == 1
    print("Cantidad en el carrito: ", contador_carrito)




