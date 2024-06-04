from models.pages.finam_page import finamPage
import allure


def test_open_investments_topic(browser_personal_settings):
    with allure.step("Открываем раздел 'Инвестиции'"):
        finamPage.open_investments()


def test_open_premium_topic(browser_personal_settings):
    with allure.step("Открываем раздел 'Премиум'"):
        finamPage.open_premium()


def test_open_education_topic(browser_personal_settings):
    with allure.step("Открываем раздел 'Обучение'"):
        finamPage.open_education()


def test_open_loyal_program_topic(browser_personal_settings):
    with allure.step("Открываем раздел 'Программа лояльности'"):
        finamPage.open_loyal_program()


def test_open_ipo_calendar(browser_personal_settings):
    with allure.step("Открываем раздел 'Календарь -> IPO'"):
        finamPage.open_calendar_of_ipo()
