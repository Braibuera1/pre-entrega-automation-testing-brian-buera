import pytest
from utils import login
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture #driver que sera pasado como parametro
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Se ejecuta al final de cada test


@pytest.mark.login 
def test_login(driver):
    login(driver)
    print(f"Login OK -> {driver.current_url}")
    

@pytest.mark.navegacion
def test_navegacion(driver): 
    login(driver)
    #Verificar titulo de seccion
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo == "Products"
    print(f"Titulo de seccion OK ->{titulo}")
    #Verificar que exista el boton de filtros
    filtro = driver.find_element(By.CLASS_NAME,'product_sort_container')
    assert bool(filtro) == True
    #Verificar que exista el boton de menu
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.text == "Open Menu"
    #Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(productos) >= 1
    print(f"Se encontraron {len(productos)} productos.")
    #Mostrar nombre y precio del primer producto
    nombre = productos[0].find_element(By.CLASS_NAME, 'inventory_item_name').text
    precio = productos[0].find_element(By.CLASS_NAME, 'inventory_item_price').text
    assert nombre == "Sauce Labs Backpack" and precio == "$29.99"
    print(f"Primer producto: {nombre} - Precio: {precio}")


@pytest.mark.comprar
def test_comprar(driver):
    login(driver)
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    #Agregar al carrito el primer producto
    productos[0].find_element(By.TAG_NAME, 'button').click()
    #Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
    assert badge.text == "1"
    print('Carrito OK ->',badge.text)
    #Seleccionar carrito de compras
    badge.click()
    assert "/cart.html" in driver.current_url
    print(f"URL Carrito OK ->{driver.current_url}")
    carrito = driver.find_elements(By.CLASS_NAME, 'cart_item')
    print(f"Se encontraron {len(carrito)} productos en el carrito de compras.")




