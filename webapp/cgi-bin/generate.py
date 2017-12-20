#! /usr/local/bin/python3

import keyreader
import template_engine

#HTTP Header
print(template_engine.cgi_content())

#HTML Webpage
print(template_engine.webpage_start())
print(template_engine.web_title('Simple WebApp'))
print(template_engine.body_start('My Public Key is : '))
keyreader.getkey('data/public_key.txt')
print(template_engine.body_end())
print(template_engine.webpage_end())