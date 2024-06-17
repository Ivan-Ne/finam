from models.pages.finam_page import finamPage
import allure


# https://jenkins.autotests.cloud/job/build_nvr_0406241/

def test_open_investments_topic(browser_personal_settings):
    with allure.step("Открываем сайт 'Финам'"):
        finamPage.open()
    with allure.step("Открываем раздел 'Инвестиции'"):
        finamPage.open_investments()
    with allure.step("Проверяем раздел 'Инвестиции'"):
        finamPage.assert_investments()


def test_open_premium_topic(browser_personal_settings):
    with allure.step("Открываем сайт 'Финам'"):
        finamPage.open()
    with allure.step("Открываем раздел 'Премиум'"):
        finamPage.open_premium()
    with allure.step("Проверяем раздел 'Премиум'"):
        finamPage.assert_premium()


def test_open_education_topic(browser_personal_settings):
    with allure.step("Открываем сайт 'Финам'"):
        finamPage.open()
    with allure.step("Открываем раздел 'Обучение'"):
        finamPage.open_education()
    with allure.step("Проверяем раздел 'Обучение'"):
        finamPage.assert_education()


def test_open_loyal_program_topic(browser_personal_settings):
    with allure.step("Открываем сайт 'Финам'"):
        finamPage.open()
    with allure.step("Открываем раздел 'Программа лояльности'"):
        finamPage.open_loyal_program()
    with allure.step("Проверяем раздел 'Программа лояльности'"):
        finamPage.assert_loyal_program()


def test_open_ipo_calendar(browser_personal_settings):
    with allure.step("Открываем сайт 'Финам'"):
        finamPage.open()
    with allure.step("Открываем раздел 'Календарь -> IPO'"):
        finamPage.open_calendar_of_ipo()
    with allure.step("Проверяем раздел 'Календарь -> IPO'"):
        finamPage.assert_calendar_of_ipo()
