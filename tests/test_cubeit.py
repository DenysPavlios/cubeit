from playwright.sync_api import Page, expect


BASE_URL = "http://127.0.0.1:8000/"


def test_check_empty(page:Page):

    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("")

    button_cube = page.locator('button.btn')
    button_cube.click()

    results = page.locator("css=p#result")
    expect(results).to_contain_text('Enter something!')



def test_check(page:Page):

    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("2")

    button_cube = page.locator('button.btn')
    button_cube.click()

    results = page.locator("css=p#result")
    expect(results).to_contain_text('8')

    