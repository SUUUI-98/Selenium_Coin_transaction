from selenium.webdriver.common.by import By

# 로그인 관련 요소
LOGIN_BUTTON = (By.XPATH, "//span[text()='로그인']")
QR_LOGIN_BUTTON = (By.XPATH, "//a[text()='QR코드 로그인']")

# 보유 자산 페이지 관련 요소
HOLDINGS_LINK = (By.XPATH, "//a[text()='보유']")
HOLDINGS_ROWS = (By.CSS_SELECTOR, "table.highlight.holdings tbody tr")

# 각 코인 행(row) 내부의 요소
COIN_NAME = (By.CSS_SELECTOR, "th a strong")

# 보유 수량/평가 금액을 포함하는 첫 번째 td
HOLDING_ELEMENT = (By.CSS_SELECTOR, "td:nth-of-type(1)")
# 첫번째 td 안에 있는 strong ,em 태그
HOLDING_QUANTITY = (By.CSS_SELECTOR, "strong")
HOLDING_AMOUNT_KRW = (By.CSS_SELECTOR, "em")

# 매수평균가를 포함하는 두 번째 td
AVG_PRICE_ELEMENT = (By.CSS_SELECTOR, "td:nth-of-type(2)")
# 두번째 td 태그 안에 있는 em 태그
AVG_PRICE_TEXT = (By.CSS_SELECTOR, "em")

# 수익률을 포함하는 세 번째 td
PROFIT_ELEMENT = (By.CSS_SELECTOR, "td:nth-of-type(3)")
# 세번째 td 안에 있는 요소들
# 수익률 퍼센테이지
PROFIT_RATIO = (By.CSS_SELECTOR, ".PriceRate--Ratio")
# 손익금액
PROFIT_AMOUNT_KRW = (By.CSS_SELECTOR, ".PriceRate--Measure")

# My 버튼
MY_BUTTON = (By.XPATH,"//span[text()='My']")

# 내 자산 보기 버튼
GET_MY_ASSET_BUTTON = (By.XPATH, "//span[text()='내 자산 보기']")


# 보유 KRW
GET_MY_KRW = (By.CSS_SELECTOR, 'span:nth-of-type(2)')

# 총 보유자산
GET_TOTAL_ROWS = (By.CSS_SELECTOR, 'span:nth-of-type(5)')