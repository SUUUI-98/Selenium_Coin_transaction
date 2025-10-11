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

# My 버튼이 속한 div의 다음 형제 div 를 선택 -> 텍스트가 있는 span 태그를 찾음
USER_NAME = (By.XPATH, "//span[text()='My']/../following-sibling::div//span[string-length(text()) > 0]")

# 내 자산 보기 버튼
GET_MY_ASSET_BUTTON = (By.XPATH, "//span[text()='내 자산 보기']")


# 보유 KRW
MY_KRW = (By.XPATH, ".//span[contains(text(), '보유 KRW')]/../following-sibling::div/span[1]")

# 총 보유자산
TOTAL_ROWS = (By.XPATH, ".//span[contains(text(), '총 보유자산')]/../following-sibling::div/span[1]")

# 총 매수
TOTAL_PURCHASE = (By.XPATH, ".//span[contains(text(), '총 매수')]/../following-sibling::div/span[1]")

# 총 평가손익
TOTAL_PROFIT_LOSS = (By.XPATH, ".//span[contains(text(), '총평가손익')]/../following-sibling::div/span[1]")

# 총 평가
TOTAL_EVALUATION = (By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[1]/article/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/span[1]')

# 총평가수익률
TOTAL_PROFIT_RATE = (By.XPATH, ".//span[contains(text(), '총평가수익률')]/../following-sibling::div/span[1]")

# 주문가능
AVAILABLE_BALANCE = (By.XPATH, ".//span[contains(text(), '주문가능')]/../following-sibling::div/span[1]")

# 거래소 버튼
EXCHANGE_TAB = (By.XPATH,"//a[text()='거래소']")

# DOGE
DOGE_COIN = (By.XPATH, ".//strong[contains(text(), '도지코인')]")

# 매수 탭
BUY_TAB= (By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[1]/div[2]/div[2]/article[1]/span/ul/li[1]/a')

# 시장가 매수 버튼
MARKET_BUY= (By.XPATH, ".//span[contains(text(), '시장가')]")

# 매수 금액 input
PRICE_INPUT_FIELD=(By.CSS_SELECTOR, "input[data-testid='price-order-total-input']")

# 매수 금액 입력값
INPUT_VALUE = "5500"

# 매수 버튼
BUY_BUTTON = (By.XPATH, ".//a[text()='초기화']/following-sibling::a[1]")

#확인 버튼
DONE_BUTTON = (By.XPATH, "//a[./span[text()='확인']]")

#거래내역 탭
HISTORY_TAB= (By.XPATH,".//a[text()='거래내역']")

# 체결 라디오 박스
TRADE_EXECUTION = (By.XPATH, ".//span[text()='체결']")

# 체결 목록에서 가져올 요소들을 한번에 담는 공통 부모 요소
ORDER_CONTAINER_XPATH = (By.XPATH,"//article/div[@class='max']/div[3]")

# 날짜와 시간 요소의 바로 위 부모 요소
ROW_LIST_PARENT_XPATH = (By.XPATH, "//div[contains(@class, 'css-1ljiip')]/parent::div")

# 가져와야할 자식 요소들의 공통된 속성을 담는 요소
ORDER_ITEM_RELATIVE_XPATH =(By.XPATH, "//div[contains(@class, 'css-1ljiip')]")

# 매도 탭
SELL_TAB= (By.XPATH, ".//a[text()='매도']")

# 주문 가능 수량
AVAILABLE_ORDER = (By.XPATH, "//div[text()='주문가능']/following-sibling::div/span[1]")

# 주문 가능 코인명
AVAILABLE_ORDER_COIN_NAME = (By.XPATH, "//div[text()='주문가능']/following-sibling::div/span[2]")

#주문 가능 원화
AVAILABLE_ORDER_KRW = (By.XPATH, "//span[contains(@class, 'font_3')]")

# 주문수량 100%
ORDER_100_SELECT = (By.XPATH, ".//a[text()='100%']")

# 매도 버튼
SELL_BUTTON = (By.XPATH, "//a[@title='초기화']/following-sibling::a[contains(text(), '매도')]")

# 팝업창 딤레이어
DIM_LAYER_SELECTOR = (By.XPATH, "//div[@data-testid='dim']")

#매도 금액 input
SELL_PRICE_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-testid='order-volume-input']")