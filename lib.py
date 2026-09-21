"""Модуль допоміжних утиліт для аналізу мережевих адрес."""

import ipaddress


def validate_ip(ip_str: str) -> bool:
    """Функція перевіряє, чи є переданий рядок валідною IP-адресою."""
    try:
        ipaddress.ip_address(ip_str.strip())
        return True
    except ValueError:
        return False


def get_network_details(cidr_str: str) -> dict:
    """Функція обчислює базові характеристики підмережі за її CIDR-записом."""
    network = ipaddress.ip_network(cidr_str.strip(), strict=False)
    return {
        "network_address": str(network.network_address),
        "netmask": str(network.netmask),
        "num_addresses": network.num_addresses,
        "is_private": network.is_private,
    }