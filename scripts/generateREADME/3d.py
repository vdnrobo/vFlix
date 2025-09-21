import os
import argparse
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser(description='Generate markdown index for model files.')
    parser.add_argument('directory', type=str, help='Path to the directory to scan')
    args = parser.parse_args()

    # Extensions
    extensions = {'.m3d', '.stp', '.png'}
    groups = defaultdict(set)

    # Scanning directory and generate files
    for filename in os.listdir(args.directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in extensions:
            groups[name].add(ext.lower())

    # Creating README.md
    output_path = os.path.join(args.directory, 'README.md')
    with open(output_path, 'w', encoding='utf-8') as md_file:
        # Write README-handle
        md_file.write(f'# {args.directory.split("/")[-1]}\n\n---\n\n')

        for name in sorted(groups.keys()):
            # Write handle
            md_file.write(f'# {name}\n\n')

            # Insert image
            if '.png' in groups[name]:
                md_file.write(f'''<table>
<tr valign="top">
<td><img src="{name}.png" height="180"></td>
</tr>
</table>\n\n''')

            # Generate links for all extensions
            links = []
            for ext in sorted(extensions):
                if ext in groups[name]:
                    links.append(f'[{ext}](./{name}{ext})')

            md_file.write(' '.join(links) + '\n\n---\n\n')

if __name__ == '__main__':
    main()
