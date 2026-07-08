import re

with open('d:/PORTFOLIO_THREAD/ngoculis/ngoculis/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('data-count=\"6\"', 'data-count=\"15\"')
content = content.replace('<span class=\"wl\">Tu?n</span>', '<span class=\"wl\">Bài</span>')
content = content.replace('Bài t?p Tu?n ', 'Bài t?p Bài ')
content = content.replace('? Tu?n ', '? Bài ')

with open('d:/PORTFOLIO_THREAD/ngoculis/ngoculis/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
