#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Использование: $0 <путь_к_изображению>" >&2
  exit 1
fi

img="$1"

# По желанию: проверим существование файла
if [[ ! -f "$img" ]]; then
  echo "Файл не найден: $img" >&2
  exit 1
fi

# Показ изображения на локальной консоли (tty1) через framebuffer
sudo fbi -T 1 -d /dev/fb1 -a "$img"

