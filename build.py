# First, get the template files
top_template = open('template/top.html').read()
bottom_template = open('template/bottom.html').read()

# Read in index HTML code
content = open('content/about.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
content = open('content/experience.html').read()
content_experience = top_template + content + bottom_template
open('docs/experience.html', 'w+').write(content_experience)

# And again, this time with art HTML code
content = open('content/skills.html').read()
content_skills = top_template + content + bottom_template
open('docs/skills.html', 'w+').write(content_skills)

content = open('content/contact.html').read()
content_contact = top_template + content + bottom_template
open('docs/contact.html', 'w+').write(content_contact)