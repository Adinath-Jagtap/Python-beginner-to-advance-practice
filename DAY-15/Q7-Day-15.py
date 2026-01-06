# 7) Validate password (min 8 chars, 1 digit, 1 special char)
import re

passwords = ["password", "Passw0rd!", "short1!", "NoSpecial123", "Good@1234"]

# Use lookahead assertions:
# (?=.*\d)  -> at least one digit
# (?=.*[^\w\s]) -> at least one special char (non-alphanumeric, not whitespace)
# .{8,} -> at least 8 characters total
pwd_pattern = r"^(?=.*\d)(?=.*[^\w\s]).{8,}$"

for pwd in passwords:
    ok = bool(re.fullmatch(pwd_pattern, pwd))
    print(f"{pwd:12} -> valid? {ok}")     