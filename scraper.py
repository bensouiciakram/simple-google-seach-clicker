from playwright.sync_api import sync_playwright 


# initialisation & globals vars : 
search_template = 'ebay item "{product_id}"'
browsers = [
    'chromium',
    'firefox',
    'webkit'
]

# helper functions : 
def choose_browser_type() -> int :
    for index,browser_type in enumerate(browsers):
        print(f'{browser_type} : {index}')
    return int(input('Choose you browser id : '))

# main functionality : 
if __name__ == '__main__':
    with sync_playwright() as p :
        #browser = p.chromium.launch(headless=False)
        exec(f'browser = p.{browsers[choose_browser_type()]}.launch(headless=False)')
        context = browser.new_context()
        page = context.new_page() 
        page.goto('https://www.google.com')
        page.fill(
            '//textarea[@name="q"]',
            search_template.format(
                product_id=input('Enter the product id : ')
                )
            )
        page.keyboard.press('Enter')
        page.click('//h3[ancestor::a]')
        breakpoint()