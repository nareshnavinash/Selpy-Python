from Locators.amazon_product_page import AmazonProductPageLocator


class AmazonProductPage(AmazonProductPageLocator):

    def __init__(self):
        super().__init__()

    @classmethod
    def is_product_page_displayed(cls):
        return AmazonProductPageLocator.amazon_product_page_identifier.wait_till_displayed()

    @classmethod
    def set_delivery_pincode(cls, string):
        AmazonProductPageLocator.amazon_deliver_to_link.click()
        AmazonProductPageLocator.amazon_deliver_to_pincode.wait_till_displayed()
        AmazonProductPageLocator.amazon_deliver_to_pincode.send_keys(string)
        AmazonProductPageLocator.amazon_deliver_to_pincode_apply.click()
        AmazonProductPageLocator.amazon_deliver_to_pincode_apply.click()
        return AmazonProductPageLocator.amazon_product_page_identifier.wait_till_displayed()

    @classmethod
    def get_delivery_pincode(cls):
        return AmazonProductPageLocator.amazon_deliver_to_link.text()