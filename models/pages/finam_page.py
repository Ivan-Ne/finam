from selene import browser, have, by


class FinamPage:

    def open_investments(self):
        browser.open('https://www.finam.ru/')
        browser.element('.p15x.window-close.pointer').click()
        browser.element(by.text('Инвестиции')).click()
        browser.element('#issf').should(have.text('Все для инвестиций'))

    def open_premium(self):
        browser.open('https://www.finam.ru/')
        browser.element('.p15x.window-close.pointer').click()
        browser.element(by.text('Премиум')).click()
        browser.element('#igia').should(have.text('Инвестиции для состоятельных клиентов'))

    def open_education(self):
        browser.open('https://www.finam.ru/')
        browser.element('.p15x.window-close.pointer').click()
        browser.element(by.text('Обучение')).click()
        browser.element('.page-content__title').should(have.text('Каталог'))

    def open_loyal_program(self):
        browser.open('https://www.finam.ru/')
        browser.element('.p15x.window-close.pointer').click()
        browser.element(by.text('Программа лояльности')).click()
        browser.element('#i5sc').should(have.text('Станьте участником программы лояльности «Финам Бонус»'))

    def open_calendar_of_ipo(self):
        browser.open('https://www.finam.ru/')
        browser.element('.p15x.window-close.pointer').click()
        browser.element(by.text('Календарь')).click()
        browser.element(by.text('IPO')).click()
        browser.element('.font-xxxl.mb15x.pt1x').should(have.text('Участие в IPO через «Финам»'))


finamPage = FinamPage()
