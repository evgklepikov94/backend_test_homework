import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Обычное сообщение (stdout)
print("Заказ № 123 принят")

# Сообщение об ошибке (stderr)
sys.stderr.write("ОШИБКА: Курьер не может принять заказ!\n")
sys.stderr.write("ПРОБЛЕМА: Ресторан не отвечает\n") 