from playwright.sync_api import sync_playwright 


# initialisation & globals vars : 
search_template = 'ebay item "{product_id}"'

# helper functions : 


# main functionality : 

if __name__ == '__main__':
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page() 
        page.goto('https://www.google.com')
        page.fill('//textarea[@name="q"]',search_template.format(product_id='385504019553'))
        page.keyboard.press('Enter')
        page.click('//h3[ancestor::a]')
        breakpoint()