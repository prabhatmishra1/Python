from pyotp import TOTP
import time
totp = TOTP('base32secret3232')
print(totp.now())  # => '492039'
# OTP verified for current time
print(totp.verify('492039'))  # => True
time.sleep(30)
print(totp.verify('492039'))  # => False
