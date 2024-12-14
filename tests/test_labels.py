import allure
from allure_pytest.utils import allure_title
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи и репозитории")
    allure.dynamic.story("Неавтоизованный пользователь не может создавать задачу и репозитории")
    allure.dynamic.link("https://github.com", name="Testing")


pass


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "aimonichev")
@allure.feature("Задачи")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
