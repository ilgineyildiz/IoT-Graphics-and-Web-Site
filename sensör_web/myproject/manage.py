#!/usr/bin/env python
import os
import sys

def main():
    """Django yönetim görevlerini çalıştır."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django is not imported in your environment."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
