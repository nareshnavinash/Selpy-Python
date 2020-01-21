from selpy.locator import Locator


class AmazonProductPageLocator:
    # Use the following description for different locators
    # CSS - 'css selector'
    # XPATH - 'xpath'
    # ID - 'id'
    # NAME - 'name'
    # LINK TEXT - 'link text'
    # PARTIAL LINK TEXT - 'partial link text'
    # TAG NAME - 'tag name'
    # CLASS NAME - 'class name'
    amazon_deliver_to_link = Locator("css selector", "div#contextualIngressPt")
    amazon_deliver_to_pincode = Locator("css selector", "div.a-column input[aria-label='or enter a pincode']")
    amazon_deliver_to_pincode_apply = Locator("css selector", "div.a-column input.a-button-input")
    amazon_product_page_identifier = Locator("css selector", "div#dp")
    # Product details locator
    amazon_product_title = Locator("css selector", "span#productTitle")
    amazon_product_byline_info = Locator("css selector", "div#bylineInfo")
    amazon_product_show_more_format = Locator("css selector", "span#showMoreFormatsPrompt")
    amazon_product_formats = Locator("css selector", "div#formats")
    amazon_product_detail_description_iframe = Locator("css selector", "iframe#bookDesc_iframe")
    amazon_product_detail_description = Locator("css selector", "div#iframeContent")
    amazon_product_description = Locator("css selector", "div#productDescription_feature_div.a-row")
    amazon_product_offers = Locator("css selector", "div#sopp_feature_div")
    amazon_product_details = Locator("css selector", "div#detail_bullets_id")

    def __init__(self):
        print("Amazon Product page locator")
