class India:
    def capital(self):
        print("Delhi")
    def language(self):
        print("Hindi")

class USA:
    def capital(self):
        print("Washington D C")
    def language(self):
        print("English")

country_i = India()
country_u = USA()
for i in (country_i, country_u):
    i.capital()
    i.language()