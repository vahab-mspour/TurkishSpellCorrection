
github_link ='https://github.com/emres/turkish-deasciifier'
projeh_moshabeh_js="https://github.com/f/deasciifier/blob/master/deasciifier.js"
from Turkish_Deasciifier_01.turkish.deasciifier import Deasciifier

my_ascii_turkish_txt = str("Yardim Kilavuzu'nu")
deasciifier = Deasciifier(my_ascii_turkish_txt) #.decode("utf-8")
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print (my_deasciified_turkish_txt) #.encode("utf-8")