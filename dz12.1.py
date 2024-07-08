import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        clean_text = re.sub(r'<.*?>', '', html_content)
        clean_text = '\n'.join(line for line in clean_text.splitlines() if line.strip())
        with open(result_file, 'w', encoding='utf-8') as output_file:
            output_file.write(clean_text)
        print(f'Очищений текст збережено у файлі {result_file}')
    except FileNotFoundError:
        print(f'Файл {html_file} не знайдено.')
delete_html_tags('draft.html', 'cleaned.txt')