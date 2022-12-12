# to test how does googletrans work :
# 1-in the vertiual environment like what we did befor pip install falsk and pymysql and numpy 
# with google translate we do same thing--> pip install googletrans ==3.1.0e0
# 2-next from googletrans import Translator
#3- craete an instance of class Translator 
#4- use translate method and this method takes 3 args word,source,destenation 
#5-to get the translated word we access it by using output.and the output is:
# Translated(src=ar, dest=en, text=Hello, pronunciation=None, extra_data="{'translat...")
# 6-now  we got the translated text (text) and to access it output.text
from googletrans import Translator
translater=Translator()
output=translater.translate("أهلا",src="ar",dest='en')
print(output)#Translated(src=ar, dest=en, text=Hello, pronunciation=None, extra_data="{'translat...")
print('%%%%%%%%%%%%%%%%%%%',output.text)#o/p%%%%%%%%%%%%%%%%%%% Hello