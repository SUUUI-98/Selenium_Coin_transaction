import re


def num(text):
 if text is None:
     return None
 text = text.strip()

 if '%' in text:
     return float(re.sub(r'[^0-9\-\.,]', '', text).replace(',', ''))

 cleaned = re.sub(r'[^0-9\-\.,]', '', text).replace(',', '').strip()
 try:
     if cleaned == "N/A":
         return None

     return float(cleaned)
 except ValueError:
     return text
