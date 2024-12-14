import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        browser.config.driver.set_window_size(1920, 1080)
    with allure.step("Ищем репозиторий"):
        s("[data-target='qbsearch-input.inputButtonText']").click()
        s("#query-builder-test").click().type("eroshenkoam/allure-example").press_enter()

    with allure.step("Переходим к репозиторию"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим к вкладке 'issues'"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 95"):
        s(by.partial_text("95")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    go_to_issues()
    check_issues_visible_number("#95")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.config.driver.set_window_size(1920, 1080)


@allure.step("Ищем репозиторий {repo} ")
def search_for_repository(repo):
    s("[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").click().type(repo).press_enter()


@allure.step("Переходим к репозиторию {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Переходим к вкладке 'issues'")
def go_to_issues():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def check_issues_visible_number(number):
    s(by.partial_text(number)).should(be.visible)
