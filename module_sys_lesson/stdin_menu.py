import sys

sys.stdin.reconfigure(encoding='utf-8')

print("Меню ресторана:")
for line in sys.stdin:
    dish = line.strip()
    print("- ", dish) 