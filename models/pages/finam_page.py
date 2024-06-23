from selene import browser, have, by
import allure


class FinamPage:

    def open(self):
        with allure.step("Открываем сайт 'Финам'"):
            browser.open('/')

    def open_investments(self):
        with allure.step("Открываем раздел 'Инвестиции'"):
            browser.element(by.text('Инвестиции')).click()

    def assert_investments(self):
        with allure.step("Проверяем раздел 'Инвестиции'"):
            browser.element('#issf').should(have.text('Все для инвестиций'))

    def open_premium(self):
        with allure.step("Открываем раздел 'Премиум'"):
            browser.element(by.text('Премиум')).click()

    def assert_premium(self):
        with allure.step("Проверяем раздел 'Премиум'"):
            browser.element('#igia').should(have.text('Инвестиции для состоятельных клиентов'))

    def open_education(self):
        with allure.step("Открываем раздел 'Обучение'"):
            browser.element(by.text('Обучение')).click()

    def assert_education(self):
        with allure.step("Проверяем раздел 'Обучение'"):
            browser.element('.page-content__title').should(have.text('Каталог'))

    def open_loyal_program(self):
        with allure.step("Открываем раздел 'Программа лояльности'"):
            browser.element(by.text('Программа лояльности')).click()

    def assert_loyal_program(self):
        with allure.step("Проверяем раздел 'Программа лояльности'"):
            browser.element('#i5sc').should(have.text('Станьте участником программы лояльности «Финам Бонус»'))

    def open_calendar_of_ipo(self):
        with allure.step("Открываем раздел 'Календарь -> IPO'"):
            browser.element(by.text('Календарь')).click()
            browser.element(by.text('IPO')).click()

    def assert_calendar_of_ipo(self):
        with allure.step("Проверяем раздел 'Календарь -> IPO'"):
            browser.element('.font-xxxl.mb15x.pt1x').should(have.text('Участие в IPO через «Финам»'))


finamPage = FinamPage()
