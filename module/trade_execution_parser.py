from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import help.hold
from data.selectors import ORDER_CONTAINER_XPATH, ROW_LIST_PARENT_XPATH, \
    ORDER_ITEM_RELATIVE_XPATH


def trade_execution_parser(driver: WebDriver):
    try:
        wait = WebDriverWait(driver, 10)
        print("주문 목록 컨테이너 로딩 대기 중...")

        # 1. 체결 목록에서 가져올 요소들을 한번에 담는 공통 부모 요소 먼저 찾기
        parent_container = wait.until(
            EC.presence_of_element_located(ROW_LIST_PARENT_XPATH))
        print("반복되는 주문 목록의 부모 요소 찾기 성공")

        # 2. 부모 요소 내부에서 모든 개별 주문 항목(Div)을 리스트로 가져옴
        # row_list는 이제 for 루프에서 사용할 수 있는 [WebElement, WebElement, ...] 리스트임
        row_list = parent_container.find_elements(*ORDER_ITEM_RELATIVE_XPATH)

        if len(row_list) < 4:
            print("경고: 주문 항목이 부족하거나 구조가 예상과 다름 (최소 4개 필요)")
            return

        print(f"총 {len(row_list)}개의 데이터 Div를 찾았습니다. 추출 시작.")
        # 요소들을 담을 리스트
        extracted_data = []



        for i in range(0, len(row_list),4):
            try:
                # 주문 Row의 4개 Div를 인덱스로 지정
                date_div = row_list[i]  # Div 1: 날짜/시간
                coin_div = row_list[i + 1]  # Div 2: 코인명/구분
                price_div = row_list[i + 2]  # Div 3: 체결가격/체결량
                amount_div = row_list[i + 3]  # Div 4: 체결금액/수수료

                # 3-1. Div 1 (날짜/시간) 추출
                date_text = date_div.find_element(By.XPATH, "./span[1]").text
                time_text = date_div.find_element(By.XPATH, "./span[2]").text

                # 3-2. Div 2 (코인명/구분) 추출
                coin_name = coin_div.find_element(By.XPATH, "./span[1]").text
                order_type = coin_div.find_element(By.XPATH, "./span[2]").text

                # 3-3. Div 3 (체결가격/체결량) 추출
                price = price_div.find_element(By.XPATH, "./span[1]").text
                amount = price_div.find_element(By.XPATH, "./span[2]").text

                # 3-4. Div 4 (체결금액/수수료) 추출
                # (구조에 따라 span[1], span[2] 등으로 추출)
                quantity = amount_div.find_element(By.XPATH, "./span[1]").text

                extracted_data.append({
                    "날짜": date_text,
                    "시간": time_text,
                    "코인명": coin_name,
                    "구분": order_type,
                    "체결가격": price,
                    "체결수량": amount,
                    "체결금액": quantity
                })



            except IndexError:
                # 불완전한 Row가 감지될 경우
                print(f"경고: 불완전한 Row 데이터가 발견되어 처리 중단 (Index {i}).")
                break

            except NoSuchElementException:
                print(f"Row {i} 에서 필요한 span 요소를 찾지 못했슴")
            except Exception as e:
                print(f"Row {i} 에서 데이터 추출 중 오류 발생: {e}")
                continue

        print("\n--- 체결 목록 추출 결과 ---")
        print("-" * 90)
        print(f"| {'날짜':<12} | {'시간':<6} | {'코인명':<10} | {'구분':<4} | {'체결가격':<10} | {'체결수량':<10} | {'체결금액':<10} |")
        print("-" * 90)

        for data in extracted_data:
            try:
                # 쉼표 제거 및 float 변환
                price_val = help.hold.num(data['체결가격'])
                quantity_val = help.hold.num(data['체결수량'])

                # 체결금액은 이미 float 문자열이므로 바로 사용
                amount_val = help.hold.num(data['체결금액'])

                # f-string 형식 지정:
                # 날짜/시간/코인명/구분은 좌측 정렬 (<)
                # 가격/수량/금액은 숫자이므로 우측 정렬 (>) 및 쉼표 형식 지정 (,)

                output = (
                    f"| {data['날짜']:<12} | {data['시간']:<6} | {data['코인명']:<10} | {data['구분']:<4} | "
                    f"{price_val:10,.1f} | "  # 가격은 소수점 1자리까지 표시 (예시 데이터 기반)
                    f"{quantity_val:10,.0f} | "  # 수량은 정수로 표시
                    f"{amount_val:14.8f} |"  # 금액은 소수점 8자리까지 표시 (정밀한 값)
                )
                print(output)

            except ValueError as e:
                print(f"| 데이터 형식 오류 (Row 스킵): {e} - 데이터: {data}")

        print("-" * 90)






    except TimeoutException:
        print(f" 시간내에 주문 목록 컨테이너를 로드하지 못함. (XPath: {ORDER_CONTAINER_XPATH})")

    except Exception as e:
        print(f" 오류 발생: {e}")
