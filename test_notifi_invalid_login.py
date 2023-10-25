from pages.home_page import LoginPage

def test_notifi_invalid_login(driver) -> None:
    invalid_user = "invalid.user123@gmail1.comm"
    invalid_password = "invalid.user123@gmail1.comm"

    login_page = LoginPage(driver)
    login_page.navigate()
    driver.implicitly_wait(10)
    login_page.enter_username(invalid_user)
    login_page.enter_password(invalid_password)
    login_page.click_login_button()
    driver.implicitly_wait(10)
    login_page.incorrect_login_or_password()
    assert "Incorrect login or password" in driver.page_source

    driver.quit()
