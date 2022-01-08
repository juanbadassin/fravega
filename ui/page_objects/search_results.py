class SearchResultsPage():
    BRAND_NAME_OPTION = 'brandAggregation'
    RESULTS_LIST = '[data-test-id="results-list"]'


    def __init__(self, driver):
        self.driver = driver

    def filter_by_brand(self):
        brand = self.driver.find_element_by_name(self.BRAND_NAME_OPTION).text.split()[0]
        self.driver.find_element_by_name(self.BRAND_NAME_OPTION).click()
        return brand

    def assert_results_list(self, brand, product):
        results_list = self.driver.find_element_by_css_selector(self.RESULTS_LIST)
        results_items = results_list.find_elements_by_tag_name('article')
        for result in results_items:
            assert brand in result.text
        assert product in self.driver.current_url