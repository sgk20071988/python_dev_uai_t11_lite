"""Пакет library_manager — управление библиотекой книг.

Экспортирует основные компоненты:
    - Library
    - generate_report
"""

from .catalog import Library
from .report import generate_report

__all__ = ["Library", "generate_report"]