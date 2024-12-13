from selene import browser, by, be
from selene.support.shared.jquery_style import s

def test_github():

    browser.open("https://github.com")
    browser.config.driver.set_window_size(1920, 1080)
    s("[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").click().type("eroshenkoam/allure-example").press_enter()


    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("95")).should(be.visible)