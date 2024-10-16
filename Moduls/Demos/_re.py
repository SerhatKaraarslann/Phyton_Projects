#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
import re

result = dir(re)
print(result)

#re module

str = "Serhat Karaarslan : A Computer Science Student | 30 age"

#re.findall()
result = re.findall("Serhat",str) # This method finds the given part in str an return a list
print(result)

result = len(result) #1
print(result)

#re.split()
result = re.split(" ",str) # this method parts the str according to given expression and returns a list 
print(result)

#re.sub()

result = re.sub(" ","-",str) # this method change the first given expression to second
print(result)

#re.search()

result = re.search("Serhat",str) # this methof finds the given expression and give us some information about it like this  : <re.Match object; span=(0, 6), match='Serhat'>
print(result)

#result = result.span() #  that give us the place : (0-6)
#print(result)
 
#result = result.start() # 0, where it starts
#result = result.end() # 6 where it ends
#result = result.group() # the given expression : Serhat
#result = result.string # the string that we searched in it  : Serhat Karaarslan : A Computer Science Student | 30 age


"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.
         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[0-5]", str)
result = re.findall("[^abc]", str)
result = re.findall("[^0-9]", str)

"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match ab
              abc  : 1 match ab
              abcd : 2 matches  ab and cd
    
"""

result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""

result = re.findall("^P",str)


"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""

result = re.findall("t$",str)
result = re.findall("saat$",str)
result = re.findall("saatt$",str)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("sa*t",str)

"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa+t",str)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa?t",str)

"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""



"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?
    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
"""