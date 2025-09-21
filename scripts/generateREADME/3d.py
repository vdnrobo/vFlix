import os
import argparse
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser(description='Generate markdown index for model files.')
    parser.add_argument('directory', type=str, help='Path to the directory to scan')
    args = parser.parse_args()

    # Интересующие нас расширения
    extensions = {'.m3d', '.stp', '.png'}
    groups = defaultdict(set)

    # Сканируем директорию и группируем файлы
    for filename in os.listdir(args.directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in extensions:
            groups[name].add(ext.lower())

    # Создаем markdown-файл
    output_path = os.path.join(args.directory, 'README.md')
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f'# {args.directory.split("/")[-1]}\n\n---\n\n')

        for name in sorted(groups.keys()):
            # Записываем заголовок
            md_file.write(f'# {name}\n\n')

            # Вставляем изображение, если есть PNG
            if '.png' in groups[name]:
                md_file.write(f'''<table>
<tr valign="top">
<td><img src="{name}.png" height="180"></td>
</tr>
</table>\n\n''')

            # Генерируем ссылки для всех форматов
            links = []
            for ext in sorted(extensions):
                if ext in groups[name]:
                    links.append(f'[{ext}](./{name}{ext})')

            md_file.write(' '.join(links) + '\n\n---\n\n')

if __name__ == '__main__':
    main()
