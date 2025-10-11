from datetime import datetime
from typing import List, Dict, Any
# 출력 함수

def print_login_failure(driver: Any):
    # 로그인 실패 시 메시지를 출력
    print(" 로그인에 실패하여 작업을 종료합니다.")


def print_holdings_summary(holdings_data: List[Dict[str, Any]]):
    ## 거래소 메인 화면에서 파싱한 코인별 보유 자산 목록을 출력

    if not holdings_data:
        print(" 보유 자산 출력 실패")
        return

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n==================================================")
    print(f"=== 보유 자산 스냅샷 (거래소 화면) ({current_time}) ===")
    print(f"==================================================")

    for r in holdings_data:
        # 데이터가 None일 경우 오류 방지를 위해 임시로 0으로 대체 (실제로는 파싱 단계에서 처리되어야 함)
        coin = r.get('코인명', 'N/A')
        holding_raw = r.get('보유', 0)
        holding_krw = r.get('평가금액', 0)
        avg_price_raw = r.get('매수평균', 0)
        profit_raw = r.get('수익률', 0)
        profit_kwr = r.get('손익금액', 'N/A')

        print(
            f"{coin:10} | 보유: {holding_raw:20} | 평가금액 : {holding_krw :20} |매수평균가: {avg_price_raw:15} | 수익률: {profit_raw:10} | 손익금액 : {profit_kwr}")
    print("--------------------------------------------------")


def print_total_asset_report(my_rows: List[Dict[str, float]]):
   # 'My' 페이지에서 파싱한 총 자산 보고서를 출력
    if not my_rows:
        print(" My 페이지 자산 정보가 불러오기 실패.")
        return

    # my_rows는 단일 항목 리스트라고 가정
    m = my_rows[0]

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n==================================================")
    print(f"=== My - 총 자산 보고서 ({current_time}) ===")
    print(f"==================================================")

    print(f"| 보유 KRW       : {m['assets_krw_value']:15,.0f} KRW ")
    print(f"| 총 보유자산    : {m['total_assets_krw']:15,.0f} KRW ")
    print(f"| 총 매수        : {m['total_purchases_krw']:15,.0f} KRW ")
    print(f"| 총 평가손익    : {m['total_profit']:15,.0f} KRW ")
    print(f"| 총 평가        : {m['evaluation_balance']:15,.0f} KRW ")
    print(f"| 총평가수익률   : {m['total_profit_rate']:15.2f}% ")
    print(f"| 주문가능       : {m['total_evaluation_balance']:15,.0f} KRW")
    print("--------------------------------------------------")


def print_trade_failure(is_success: bool):
    if not is_success:
       print(" 매수/매도 작업 실패 ")
       return
    print("")
# TODO : 함수 매수/매도 나눠서 만들기 : 결과값 출력