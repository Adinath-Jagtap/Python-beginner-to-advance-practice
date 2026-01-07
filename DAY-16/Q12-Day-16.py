# 12. Use regex to extract all dates in the format DD-MM-YYYY from a text

import re
text = "Events: 01-01-2020, invalid 32-13-2020, 15-08-1947 and 05-06-2021."
pattern = r"\b\d{2}-\d{2}-\d{4}\b"
dates = re.findall(pattern, text)
print(dates)  # ['01-01-2020', '15-08-1947', '05-06-2021']