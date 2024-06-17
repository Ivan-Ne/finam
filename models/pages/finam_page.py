from selene import browser, have, by


class FinamPage:

    def open(self):
        browser.open('/')

    def open_investments(self):
        browser.element(by.text('Инвестиции')).click()

    def assert_investments(self):
        browser.element('#issf').should(have.text('Все для инвестиций'))

    def open_premium(self):
        browser.element(by.text('Премиум')).click()

    def assert_premium(self):
        browser.element('#igia').should(have.text('Инвестиции для состоятельных клиентов'))

    def open_education(self):
        browser.element(by.text('Обучение')).click()

    def assert_education(self):
        browser.element('.page-content__title').should(have.text('Каталог'))

    def open_loyal_program(self):
        browser.element(by.text('Программа лояльности')).click()

    def assert_loyal_program(self):
        browser.element('#i5sc').should(have.text('Станьте участником программы лояльности «Финам Бонус»'))

    def open_calendar_of_ipo(self):
        browser.element(by.text('Календарь')).click()
        browser.element(by.text('IPO')).click()

    def assert_calendar_of_ipo(self):
        browser.element('.font-xxxl.mb15x.pt1x').should(have.text('Участие в IPO через «Финам»'))


finamPage = FinamPage()
