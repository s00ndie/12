import re
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        match = re.findall(r'>{1}.+<{1}', html)
        result = (str(match).replace('>', '').replace('<', ''))
        print(result)
    with open(result_file,'w') as file:
        file.write(result)

delete_html_tags('draft.html')
