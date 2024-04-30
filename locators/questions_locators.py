from selenium.webdriver.common.by import By

class Questions:
    QUESTION_1_LOCATOR = (By.ID, 'accordion__heading-0')
    ANSWER_1_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")

    QUESTION_2_LOCATOR = (By.ID, 'accordion__heading-1')
    ANSWER_2_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]")

    QUESTION_3_LOCATOR = (By.ID, 'accordion__heading-2')
    ANSWER_3_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")

    QUESTION_4_LOCATOR = (By.ID, 'accordion__heading-3')
    ANSWER_4_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")

    QUESTION_5_LOCATOR = (By.ID, 'accordion__heading-4')
    ANSWER_5_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]")

    QUESTION_6_LOCATOR = (By.ID, 'accordion__heading-5')
    ANSWER_6_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]")

    QUESTION_7_LOCATOR = (By.ID, 'accordion__heading-6')
    ANSWER_7_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]")

    QUESTION_8_LOCATOR = (By.ID, 'accordion__heading-7')
    ANSWER_8_LOCATOR = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]")