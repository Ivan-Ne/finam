from models.pages.finam_page import finamPage


def test_open_investments_topic():
    finamPage.open()
    finamPage.open_investments()
    finamPage.assert_investments()


def test_open_premium_topic():
    finamPage.open()
    finamPage.open_premium()
    finamPage.assert_premium()


def test_open_education_topic():
    finamPage.open()
    finamPage.open_education()
    finamPage.assert_education()


def test_open_loyal_program_topic():
    finamPage.open()
    finamPage.open_loyal_program()
    finamPage.assert_loyal_program()


def test_open_ipo_calendar():
    finamPage.open()
    finamPage.open_calendar_of_ipo()
    finamPage.assert_calendar_of_ipo()
