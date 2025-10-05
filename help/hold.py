import re

# 주어진 문자열에서 숫자만 추출해서 float 으로 변환
# 문자가 비었을 경우 공백 리턴
def num(text):
 if text is None:
     return None
 # 문자의 양 끝 공백 제거
 text = text.strip()

 # 텍스트에 '%' 기호가 포함되어 있는지 확인 (수익률과 같은 경우)
 if '%' in text:
     # '%'를 제외한 모든 비숫자, '-', '.', ',' 문자를 제거하고 쉼표를 없앤 후 float으로 변환
     return float(re.sub(r'[^0-9\-\.,]', '', text).replace(',', ''))

 #숫자, '-', '.', ','를 제외한 모든 문자를 제거하고 쉼표를 없앤 후 공백 제거
 cleaned = re.sub(r'[^0-9\-\.,]', '', text).replace(',', '').strip()

 try:
     return float(cleaned)

 except ValueError:
     # 숫자로 변환할 수 없는 경우 원래의 텍스트로 리턴
     return text
