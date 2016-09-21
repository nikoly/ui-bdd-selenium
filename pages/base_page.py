from page_objects import PageObject, PageElement


class BasePage(PageObject):
    """ All pages should inherit this class. 
        The class implements some important methons such as:
        - trait: this is the most importnat element of the page, which defines the presence of the page
        - wait_for: this is the method to wait for a page to load. By defaul it waits for a trait value 
    """

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
