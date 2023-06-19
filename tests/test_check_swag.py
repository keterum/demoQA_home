from pages.swag_labs import SwagLabs

def test_icon(browser):
    sw_page = SwagLabs(browser)
    sw_page.visit()
    sw_page.exist_icon()
    assert sw_page.exist_icon()
