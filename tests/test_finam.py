from models.pages.finam_page import finamPage
import allure


# https://jenkins.autotests.cloud/job/build_nvr_0406241/

def test_open_investments_topic():
    with allure.step("Открываем раздел 'Инвестиции'"):
        finamPage.open_investments()


def test_open_premium_topic():
    with allure.step("Открываем раздел 'Премиум'"):
        finamPage.open_premium()


def test_open_education_topic():
    with allure.step("Открываем раздел 'Обучение'"):
        finamPage.open_education()


def test_open_loyal_program_topic():
    with allure.step("Открываем раздел 'Программа лояльности'"):
        finamPage.open_loyal_program()


def test_open_ipo_calendar():
    with allure.step("Открываем раздел 'Календарь -> IPO'"):
        finamPage.open_calendar_of_ipo()
