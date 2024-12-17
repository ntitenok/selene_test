from selene import browser, have, be
from selene import by
import allure
import os

@allure.title('Заполнить форму студента')
def test_form_student_registration():
    with allure.step('Открыть страницу с формой'):

        browser.open('/automation-practice-form')

    with allure.step('Заполнить форму'):
        browser.element('#firstName').type('Nikolay')
        browser.element('#lastName').type('Titenok')
        browser.element('#userEmail').type('ntitenok@gmail.com')
        browser.element('[for="gender-radio-1').click()
        browser.element('#userNumber').type('1234567890')


        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').click().element(by.text('1989')).click()
        browser.element('.react-datepicker__day--022').click()


        browser.element('#subjectsInput').type('Computer')
        browser.element(by.text('Computer Science')).click()
        browser.element('#subjectsInput').type('Physics').press_enter()



        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()


        browser.element('#uploadPicture').send_keys(os.path.abspath('data\\myfile'))


        browser.element('#currentAddress').type('Мой адрес — ни дом и не улица')
        browser.element('#state').click().element(by.text('Haryana')).click()
        browser.element('#city').click().element(by.text('Panipat')).click()


        browser.element('#submit').click()

    with allure.step('Проверить результат'):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td:nth-child(2)').should(
            have.texts('Nikolay Titenok', 'ntitenok@gmail.com', 'Male', '1234567890', '22 May,1989',
                       'Computer Science, Physics', 'Sports, Reading, Music', 'myfile', 'Мой адрес — ни дом и не улица',
                       'Haryana Panipat'))