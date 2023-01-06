from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_exists_add_to_cart_button(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(buttons) == 1, 'На странице должна быть одна кнопка "Добавить в корзину"'
