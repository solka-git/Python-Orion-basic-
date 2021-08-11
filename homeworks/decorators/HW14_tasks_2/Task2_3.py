# 3. def get_names_page(names_list):
#         template_head = "<h3> User names: </h3>"
#         template = "<p> {} </p>"
#
# Допишіть дану функцію так, щоб коли на вхід приходить names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
# функція повертала таку строку
#
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
#
# До даної функції напишіть декоратор який загорне отриману строку в div блок. style_class -
# це аргумент який приймається
# декоратором, тобто декоратор або в 3 рівні, або функтор (краще зробіть через функтор)
#
# <div class=*style_class*>
# <h3> User names: </h3>
# <p> Misha </p>
# <p> Olya </p>
# <p> Vitaliy </p>
# <p> Vita </p>
# </div>


class DecorDiv:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(name_list):
            template = f"<div class=*{self.style_class}*>\n"
            template += func(name_list)
            return template + "</div>"
        return wrap


@DecorDiv('jjj')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>\n"
    template = template_head
    for name in names_list:
        template += "<p> {} </p>\n".format(name)
    return template


print(get_names_page(["Misha", "Olya", "Vitaliy", "Vita"]))


