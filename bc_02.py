# Python Format Specifiers Practice

# Basic string formatting with f-strings
name = "Alice"
age = 30
price = 19.99

# String format specifier
print(f"{name:s}")  # :s - string

# Integer format specifiers
print(f"{age:d}")  # :d - decimal integer
print(f"{age:b}")  # :b - binary
print(f"{age:o}")  # :o - octal
print(f"{age:x}")  # :x - hexadecimal (lowercase)
print(f"{age:X}")  # :X - hexadecimal (uppercase)

# Float format specifiers
print(f"{price:.2f}")  # :.2f - fixed-point, 2 decimal places
print(f"{price:.3e}")  # :.3e - exponential notation
print(f"{price:.3g}")  # :.3g - general format
print(f"{price:g}")   # :g - general format (removes trailing zeros)

# Width and alignment
print(f"{name:10}")      # :10 - right-aligned, width 10
print(f"{name:<10}")     # :<10 - left-aligned
print(f"{name:>10}")     # :>10 - right-aligned
print(f"{name:^10}")     # :^10 - center-aligned
print(f"{age:0>5}")      # :0>5 - zero-padded, width 5

# Percentage
percentage = 0.85
print(f"{percentage:.1%}")  # :.1% - percentage format

# Thousands separator
big_number = 1000000
print(f"{big_number:,}")    # :, - comma separator
print(f"{big_number:_}")    # :_ - underscore separator