#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walia_blog.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except (ImportError, ModuleNotFoundError) as exc:
        if os.getenv('VERCEL'):
            print(f"manage.py: {exc} during Vercel inspection (dependencies will be installed in build).")
            return
        raise ImportError(
            "Couldn't import Django or its dependencies. Are you sure they are installed "
            "and available on your PYTHONPATH environment variable?"
        ) from exc


if __name__ == '__main__':
    main()
