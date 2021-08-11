# 4. Допишіть ще один декоратор, який загорне результат роботи з попереднього завдання в теги <body> </body>.
# Щоб отримати ось такий код
#
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
#


def decor_body(func):
    def wrap(name_list):
        template = f"<body>\n"
        template += func(name_list)
        return template + "\n</body>"
    return wrap


# ще один декоратор який приклеїть до існуючого куска html - head блок, де *title* це аргумент що отримується декоратором
#
# <head>
# <title>*title*</title>
# </head>
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
#

class DecorHead:
    def __init__(self, title):
        self.title = title

    def __call__(self, func):
        def wrap(name_list):
            template = f"<head>\n<title>*{self.title}*</title>\n</head>\n"
            template += func(name_list)
            return template
        return wrap


# Ще один декоратор який загорне все що є в <html> </html> теги
#
# <html>
# <head>
# <title>*title*</title>
# </head>
# <body>
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
# </html>
#
# Зверніть увагу що у вас на одну функцію повинно назначатись 4 декоратори, тому потрібно не тільки їх написати, а й
# вибрати правильний порядок декорування щоб після всіх декорацій отримати наприклад ось такий html
# Також деякі декоратори доцільно буде робити через функції в "2 рівні", деякі в "3 рівні", деякі через функтори
#
# <html>
# <head>
# <title>Users</title>
# </head>
# <body>
# <div class=users_block>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>
# </body>
# </html>

def decor_html(func):
    def wrap(name_list):
        template = f"<html>\n"
        template += func(name_list)
        return template + "\n</html>"
    return wrap


class DecorDiv:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(name_list):
            template = f"<div class=*{self.style_class}*>\n"
            template += func(name_list)
            return template + "</div>"
        return wrap


@decor_html
@DecorHead("Hello")
@decor_body
@DecorDiv('jjj')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>\n"
    template = template_head
    for name in names_list:
        template += "<p> {} </p>\n".format(name)
    return template


print(get_names_page(["Misha", "Olia", "Vitaliy", "Vita"]))