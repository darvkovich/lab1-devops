"""Головний модуль запуску перевірки мережевих утиліт."""

from lib import get_network_details, validate_ip

test_ips = ["192.168.1.1", "10.0.0.5", "999.12.34.5"]
test_network = "10.10.0.0/24"

print("=== РЕЗУЛЬТАТ ВАЛІДАЦІЇ АДРЕС ===")
for ip in test_ips:
    status = "ВАЛІДНА" if validate_ip(ip) else "НЕВАЛІДНА"
    print(f"IP-адреса: {ip:<15} -> {status}")

print("\n=== ПАРАМЕТРИ ПІДМЕРЕЖІ ===")
net_info = get_network_details(test_network)
print(f"Підмережа:       {test_network}")
print(f"Адреса мережі:   {net_info['network_address']}")
print(f"Маска підмережі: {net_info['netmask']}")
print(f"Кількість адрес: {net_info['num_addresses']}")
print(f"Приватний пул:   {'Так' if net_info['is_private'] else 'Ні'}")