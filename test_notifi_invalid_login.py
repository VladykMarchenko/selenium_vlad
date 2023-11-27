from pages.home_page import LoginPage

def test_notifi_invalid_login(driver) -> None:
    invalid_user = "invalid.user123@gmail1.comm"
    invalid_password = "invalid.user123@gmail1.comm"
    expected_error_message = "Incorrect login or password"

    login_page = LoginPage(driver)
    login_page.navigate()
    driver.implicitly_wait(10)
    login_page.enter_username(invalid_user)
    login_page.enter_password(invalid_password)
    login_page.click_login_button()
    driver.implicitly_wait(10)
    login_page.incorrect_login_or_password()
    assert "Incorrect login or password" in driver.page_source
    assert login_page.is_displayed_incorrect_login_or_password(), "Error message not displayed"
    assert expected_error_message in login_page.incorrect_login_or_password(), f"Expected error message '{expected_error_message}' not found in page source"


# EC is_visible добавить в тест done
# убрать проперти из хом пейдж
# EC вместо implicitly_wait
# navigate как отдельную централизованый метод отдельно вынести
