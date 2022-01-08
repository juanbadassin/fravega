class HomePage():
    URL = "https://fravega.com"
    CLOSE_MODAL_BTN = '[data-test-id="close-modal-button"]'
    SEARCH_BOX = 'keyword'
    SEARCH_BTN = 'button'
    SEARCH_BOX_AREA = '[style="grid-area:search"]'

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.URL)
        self.driver.find_element_by_css_selector(self.CLOSE_MODAL_BTN).click()

    def search_product(self, product):
        search_box_area = self.driver.find_element_by_css_selector(self.SEARCH_BOX_AREA)
        search_box_area.find_element_by_name(self.SEARCH_BOX).send_keys(product)
        search_box_area.find_element_by_tag_name(self.SEARCH_BTN).click()
