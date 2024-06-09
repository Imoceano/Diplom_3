from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_PROFILE_BUTTON = By.LINK_TEXT, 'Профиль'
    ACCOUNT_HISTORY_BUTTON = By.XPATH, '//*[@href="/account/order-history"]'
    ACCOUNT_EXIT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]' 

class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")

class MainPageLocators:
    
    MAIN_PAGE = (By.CLASS_NAME, "App_App__aOmNj")
    LOGO_BUTTON = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    PERSONAL_ACCOUNT_LINK = By.XPATH, ".//p[text()='Личный Кабинет']"
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    CONSTRUCTOR_FORM = (By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")
    ORDERS_LIST_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    INGREDIENT_BUTTON = (By.XPATH, ".//p[@class = 'BurgerIngredient_ingredient__text__yp3dH' and text()='{}']")
    INGREDIENT_DETAILS_FORM = (By.XPATH, ".//p[@class = 'text text_type_main-medium mb-8' and text()='{}']")
    INGREDIENT_DETAILS_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    INGREDIENT_COUNT = (By.XPATH, ".//p[@class = 'counter_counter__num__3nue1' and text()='{}']")
    INGREDIENTS_IN_BURGER_LIST = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CONFIRM_ORDER_FORM = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")



class OrderPageLocators:
    ORDERS_LIST_FORM = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDER_DETAILS = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    FIRST_ORDER_IN_LIST = (By.XPATH, "/descendant::div[@class='OrderHistory_textBox__3lgbs mb-6'][position() = (1)]")
    CREATED_ORDER_FORM = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    CREATED_ORDER_FORM_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    CREATED_ORDER_IN_LIST = (By.XPATH, ".//p[@class = 'text text_type_digits-default' and text()='{}']")
    ALL_TIME_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (1)]")
    TODAY_COUNT = (By.XPATH, "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (2)]")
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2' and text()='{}']")

class RecoveryPageLocators:
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    RECOVERY_CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    RECOVERY_PASSWORD_FIELD = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = 'Введите новый пароль']")
    PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']")