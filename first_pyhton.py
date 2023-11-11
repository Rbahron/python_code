
import math


'''print(16//4)

print(18//4)
print(25/5)
x= 5.4
print(x)
print(18%3)'''

'''#print('toqqizning kvadrati ',9**2,' ga teng')
print('"nexia" ,"tico" \'damas\' korganlar havas qilar ')
#5 ning 4 darajasi
print('5 ning 4 darajasi ',5**4)
#22 ni 4 ga bolganimizda qancha qoldiq qolishi chiqadi
print('22 ni 4 ga bolinganda qoldiq',22%4)
#tomonlari 125 ga teng bolgan kvadratni yuzi
print('tomonlari 125 ga teng bolgan kvadratning yuzi',125*125)
#tomonlari 125 ga teng bolgan kvadratning parametri 
print('tomonlari 125 ga teng bolgan kvadratning paremetri',125*4)
print('diametri 12 ga teng bolgan aylananing yuzi',(12/2)**2*3.14)
#katetlari 6 va 7 ga teng bolgan tog'ri burchakli uchburchakning gipotenuzasi
print('katetlari 6 va 7 ga teng bolgan uchburchak gipotenuzasi',(6**2+7**2)**(1/2))
x = 'hello world'
print(x)
xabar= 5
print(xabar)
xabar= 6
print(xabar)
radius = 5
pi = 3.14
aylananing_yuzi = pi * radius**2
print('radiusi',radius,'ga teng bolgan aylananing yuzi',aylananing_yuzi)
ism = 'ahad'
print('mening ismim ' + ism)
familia = 'kayum'
print (ism + ' ' + familia)
ism_familia = f'{ism} {familia}'
print(ism_familia)

ism = 'James'
familia = 'Bond'
print(f"Salom mening ismim {familia}. {ism} {familia}")
print('Hello World')
print('Hello\tWorld')
print('Hello\nWorld')
ism = "Ahad"
familia = 'Qayum'
ism_familia = f'{ism} {familia}'
print(ism_familia.upper())
print(ism_familia.lower())

ism_sharif= 'james bond'
x= ism_sharif.title()
y = ism_sharif.capitalize()
print('umarov farshid'.upper(),x,y)
inson = '   salno   '
print(inson.rstrip())
print(inson.lstrip())
print(inson.strip())
print(inson)

ism = input('ismingiz nima?\n>>>')
print('Assalomu Aleykum',ism)

kocha = 'Atvor'
mahalla = 'Baxtiyorchi'
tuman = 'Romitan'
viloyat = 'Buxoro'
print(kocha,'ko`chasi,',mahalla,'mahallasi,',tuman,'tumani,',viloyat,'viloyati,')
qishloq = input('Tug`ilgan qishlog`ingizni nomini kiriting\n>>>')
mfy = input('Tug`ilgan mahhallangini nomini kiriting\n>>>')
tumv = input('Tuman nomini kiriting\n>>>')
viloy = input('Viloyat nomini kiriting\n>>>')
print(qishloq,'qishlog`i\n',mfy,'mahallasi\n',tumv,'tumani\n',viloy,'viloyati\n')

manzil = f'{kocha} {mahalla} {tuman} {viloyat}'
print(manzil)
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
print(manzil.upper())

kvdrt_tmn = 20
kvdrt_yuzi = kvdrt_tmn ** 2
print(kvdrt_yuzi)

pi = 3.14159
radius = 10
diametr = 2*radius
print('aylananing uzunligi',pi*diametr)

a,z,x = 110,20,30
print(a)
print(z)
print(x)
ism = 'bahron'
yosh = 36
YOSH = '36'
print(str(yosh),int(YOSH),float(YOSH))

print(type(ism))
print(type(yosh))

ta_yol = input('Tug`ilgan yilingizni kiriting')
ta_yol = int(ta_yol)
yosh = 2023 - ta_yol
print('siz',yosh,'da ekansiz')

mevalar = ['olma','anor','orik','anor','anor']

print('brinchi meva:',mevalar[0].title())
print('ikkinchi meva:',mevalar[1].capitalize()) 

narhlar = [12000,15000,20000,50000]
print(narhlar)

narhlar[0] = 30000
narhlar[1] = 55555
narhlar[2] = 66666
narhlar[3] = 77777

print(narhlar)

mevalar.append('tarvuz')
print(mevalar)

cars = []

cars.append('nexia')
cars.append('lada')
cars.append('auruss')

cars.insert(3,'niva')

print(cars)

del mevalar[2]
print(mevalar)
mevalar.remove('anor')
print(mevalar)
mevalar.insert(3,'anor')

print(mevalar)

bozorlik = ['yog`','sut','banan','go`sht','mevalar']
mahsulot = bozorlik.pop(2)
print(mahsulot)
print(bozorlik)

ismlar = ['mahmud','azizbek','sardor']
print('salom',ismlar[0])
print('salom',ismlar[-1])

sonlar = [12,13,14,-15,-16,-18,-19,20.0,21.0,-22.0]

numb1 = sonlar[2] + sonlar[0]
numb2 = sonlar[3] - sonlar[-1]
numb3 = sonlar[4] * sonlar[5]
numb4 = sonlar[-3] % sonlar[0]
numb5 = sonlar[5] / sonlar[-3]

print(numb1,numb2,numb3,numb4,numb5)

t_shaxslar = ['imom buxoriy','al forobiy','ibn sino','ibn battuta']
z_shaxslar = ['celal sengor','charls darvin','nikol tesla','tomas edison']

print('men tarixiy shaxslardan',t_shaxslar.pop(1),'zamonaviy shaxslardan',z_shaxslar.pop(0),'bilan suhbatlashishni xohlardim')

friends = []
friends.append('avrar')
friends.append('sarsar')
friends.append('narxar')
friends.append('gavsar')
friends.append('shalvar')
print(friends)
friends.remove('sarsar')
friends.remove('narxar')
print(friends)
friends.insert(0, 'birinchi')
friends.insert(3, 'ortasi')
print(friends)

mehmonlar = []

gosts1 = friends.pop(1)
gosts2 = friends.pop(3)
gosts3 = friends.pop(2)

mehmonlar.append(gosts1)
mehmonlar.append(gosts2)
mehmonlar.append(gosts3)

print(mehmonlar,friends)

cars = ['nexia','Damas','Lasetti','bus','helicopter','hitler','airbus']
print(cars)



print(len(cars))
juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print(juft_sonlar,toq_sonlar)

narhlar = [10000,20000,40000,35000]
arzon = min(narhlar)
qimmat =  max(narhlar)
jami = sum(narhlar)

print(arzon,qimmat,jami)

my_cars = cars[0:4]
your_cars = cars[:3]
his_cars = cars[4:]
print(my_cars,your_cars,his_cars)

sonlar = [1,2,3,4,5,6,7,8,9,10]
sonlar2 = sonlar[:]
sonlar2.append(11)
sonlar2.append(12)
print(sonlar)
print(sonlar2)



toys = ('bears','snakes','spyders','monkeys','horses')

print(type(toys))

print(toys[2])
print(toys[-1])
print(toys[4])

toys = list(toys)


toys.append('monsters')
toys.append('frekys')
toys.remove('snakes')
toys[4] = 'snakes'

toys  = tuple(toys)
print(toys,type(toys))

davlatlar = ['USA','Great Britain','France','Spain','German','Italy','Turkey']
davlatlar.sort(reverse=True)
print(davlatlar)
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)

sonlar = list(range(120,1200,2))
sum_0f_sonlar = sum(sonlar)
print(sum_0f_sonlar)

solution = max(sonlar) - min(sonlar)
print(solution)
 
print(len(sonlar))

print(sonlar[0:20])
print(sonlar[250:270])
print(sonlar[300:320])


taomlar = ['lagmon','palov','manti','halim','moshxorda']
nonushta = taomlar[:]
nonushta.remove('lagmon')
nonushta.remove('manti')
nonushta.append('tuxum')
nonushta.append('shirguruch')

print(nonushta)
print(taomlar)

nonushta = tuple(nonushta)
taomlar = tuple(taomlar)

#nonushta[3] = 'qaymoq va non'

    
dostlar = []
print('5 ta eng yaqin dostingizni ismini kiriting')

for n in range(5):
    dostlar.append(input(f'{n+1}-dostingizni kiriting'))
    
print(dostlar)


ismlar = ['selim','davron','nemis','ajdar','askar']


for ism  in ismlar:
    print(f'{ism} xush kelibsan')



sonalar_100 = list(range(101))

for son in sonalar_100:
    print(son**3)


kinolar = []

print('yaxshi ko`rgan filmingizni kiriting')

for n in range(5):
    kinolar.append(input(f"sevgan filmingizni kiriting {n+1}"))


print(kinolar)

odamlar = []

odamlar_soni = input('bugun nechta odam bn suhbat qildingiz ')
odamla = int(odamlar_soni)

for n in range(odamla):
    odamlar.append(input(f'{n+1}-odamni kiriting'))
    
print(odamlar)


avtolar = ['general motors','mersedes benz','bmw','volvo']

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

ism = input(f'Ismingizni nima?\n>>>')

if ism.lower() != 'ali':
    print(f'Uzr {ism.title()} biz alini kutyapmiz')
else:
    print('salom ali')
    
javob = float(input("12x6 necha boladi\n>>>"))
if javob!=72 :
    print('Javob notogri')


yosh = int(input('Yoshingiz nechida?>>>'))
if yosh<18:
    print('uzr yoshingiz yetmaydi')
    
else:
    print('xush kelibsiz')


login = input('loginingizni kiriting\n>>>')
if len(login)< 5:
    print('LOGIN ENG KAMIDA 5 HARFDAN IBORAT BOLSHI KERAK')
else:
    print('xush kelibsiz')

yil = int(input('Tugilgan yilingizni kiriting'))
if 2022-yil < 18:
    print(f'Yoshingiz {2022-yil}-da ekan')
    print('uzr kirish mumkin emas')
else:
    print('xush kelibsiz')



cars = ['toyota','ford','mersedes-benz','gm','aston-martin']
for i in cars:
    if i != 'gm':
        print(i.title())
    else:
        print(i.upper())
   

admin = input('loginni kiriting\n>>>')
if admin == 'admin':
    print("xush kelibsiz admin foydalanuvchi royxatini korishni xoxlaysizmi")
else:
    print(f'xush kelibsiz {admin}')

num1 = int(input('brinchi son\n>>>'))
num2 = int(input('ikkinchi son\n>>>'))
if num1 == num2:
    print('sonlar teng')

son = int(input('son kiriting\n>>>'))
if son<0:
    print('Musbat son kiriting')
else:
    print(f'{son**(1/2)}')

yosh = int(input('Yoshingiz nechida'))
if yosh <= 4 :
    price = 0
elif yosh <= 10:
    price = 5000
elif yosh <= 65:
    price = 10000
elif yosh >= 65:
    price = 8000


print(f'sizga kirish {price} som')

kun = input('Bugun kun nima?')

if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    day = 'dam olish'
else:
    day = 'ish'

print(f'Bugun {day} kuni')

kun = input('bugun kun nima?')
harorat =float(input('harorat necha gradus?'))
if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
    print('chomilgani ketdik')
elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba')and harorat < 30:
    print('uyda dam olamiz')
    
narx = 15000
choy = True
salat = False
non = True
kompot = True
assorti = True

if choy:
    print('mijoz non oldi')
    narx = narx + 3000
if salat:
    print('mijoz salat oldi')
    narx = narx + 5000
if non :
    print('mijoz non oldi')
    narx = narx + 3000
    
if kompot :
    print('mijoz kompot oldi')
    narx = narx + 2000
if assorti :
    print('mijoz assorti oldi')
    narx = narx + 5000
    
print(f'hisob {narx} boldi')

ovqat = input('Nima ovqat yemoqchisiz?>>>')

if ovqat.lower() not in menu:
    print('buyurtma qabul qilindi')
else:
    print('Afsuski bu ovqat bizda yoq')

menu = ['osh','qozonkabob','manti','lagman']
buyurtmalar = []

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f'menyuda {taom} bor')
        else:
            print(f'kechirasiz menyuda {taom} yoq')

else:
    print('savat bosh')

son = int(input('Juft sonni kiriting>>>'))

if son == 2 or son%2 == 0:
    print('rahmat')
else:
    print('bu son juft emas')

yosh = int(input('yoshingizni kiriting'))
price = 0

if yosh < 4 or yosh > 60:
    price = 0
elif yosh < 18 :
    price = 10000
else:
    price = 20000
print(f'sizga kirish {price} som')

birinchi_son = int(input("birinchi sonni kiriting"))
ikkinchi_son = int(input('Ikkinchi sonni kiriting'))

if birinchi_son < ikkinchi_son :
    print(f'{birinchi_son} < {ikkinchi_son}')
else:
    print(f'{birinchi_son} > {ikkinchi_son}')
    
products = ['granade','apple','cherry','orange','banana','penaples','']

savat = []
present_products = []
absent_products = []

for n in range(5):
    savat.append(input(f'Savatga {n+1} - mahsulotni kiriting >>>'))

for fruit in savat:
    if fruit in products:
       present_products.append(fruit) 
    else:
        absent_products.append(fruit)

if not present_products :
    print('berilgan mahsulatlar bizda yoq')
    for n in absent_products:
        print(n)
else:
    print('siz soragan barcha mahsulatlar dokanimizda bor')

users = ['sasha','masha','natasha','andrey','dimon']
login = input('login kiriting')
              
if login in users:
     print('login band yangi login tanlang')
else:
     print('xush kelibsiz')

random_number = int(input('istalgan sonni kiriting >>>'))

for n in range(2,10):
   if not (random_number%n):
       print(f'{random_number} {n} ga qoldiqsiz bolinadi')

son = float(input("Juft son kiriting"))
if not son % 2 == 0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")     


bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print('hammasi bor')
users = ['alisher1983','aziza','yasina' ,'umar']

login = input("Yangi login tanlang:")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")


car = {'model': 'ferrari','rang': 'qizil'}

print(car['rang'])

talaba_0 = {'ism':'bahron ramazonov','tu-yil':1997,'yoshi':26}
print(f"{talaba_0['ism'].title()}, \
 {talaba_0['tu-yil'] } - yilda tug'ilgan \
 {talaba_0['yoshi']} da")
 
talaba_0["kurs"] = 4
talaba_0['fakultet'] = 'informatika'

print(talaba_0)

talaba_1 = {}

talaba_1['ism'] = 'ramazonov bahron'
talaba_1['tu-yil'] = 1997
talaba_1['yoshi'] = 26
talaba_1['kurs'] = 3
talaba_1 ['fakultet'] = 'informatika' 

talaba_1['kurs'] = 4
del talaba_1['yoshi']

print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} kursda")

phone = telefonlr.get('hasan')
print(f'alining telefoni{phone}') 

dadam = {
    'ism':'korvon',
    'yoshi':60,
    'shahri': 'Buxoro',
    'millati': 'tojik',
    }

onam = {
    'ism':'hanifa',
    'yoshi':55,
    'shahri':'buxoro',
    'millati':'ozbek',
    }

opam = {
    'ism':'nigina',
    'yoshi':29,
    'shahri':'Buxoro',
    'millati':'tojik'
    
    }

print(f"Dadam {dadam.get('ism').title()} yoshi {dadam.get('yoshi')} da {dadam.get('shahri')}da tugilgan Millati {dadam.get('millati')}")

taomlar = {
    'otam':'osh',
    'onam':'manti',
    'opam':'salat',
    'xolam':'quymoq',
    'akam':'sumalak'
    }

print(f"otam {taomlar.get('otam')}ni yaxshi koradi")
print("onam {taomlar.get('onam')}ni yaxshi koradi")
print(f"akam {taomlar.get('akam')}ni yaxshi koradi")
kalit = input('kalit sozni kiriting').lower()

if kalit in keywords:
    print(f"{keywords.get(kalit)}")
else:
    print('bizda bunday soz mavjud emas')




keywords = {
    'intiger':'sonlar',
    'list':'royxat',
    'float':'kasr sonlar',
    'variable':'ozgaruvchilar',
    'function':'funksiyalar',
    'class':'obyekt uchun shablonlar',
    'tuply':'ozgarmas royxatlar',
    'set':'umuman ozgarmas royxatlar',
    'dictionary':'ozgaruvchi kalit qiymat ryxati',
    'loops':'tsikllar'
    }
for kalit,qiymat in keywords.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat: {qiymat}")


telefonlar = {
    'ali':'iphone11',
    'vali':'redmi',
    'aziz':'samsung',
    'shamshod':'sony'
    }

for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

print(telefonlar.keys())
print('insonlar')
for inson in telefonlar.keys():
    print(inson.title())


mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'orik': 5000,
    'bugdoy': 15000,
    'arpa': 2000,
    'banan': 30000,
    'mandarin': 15000,
    
    }

bozorlik = ['anor','halim','olma','arpa']

for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f" {mahsulotlar[mahsulot]}so'm")

for buyum in bozorlik:
    if not buyum in mahsulotlar:
        print(f"iltimos dokoningizga {buyum}ni ham olib keling")

print('dokonimizda quyidagi mahsulotlar bor')
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

print(mahsulotlar.values())

print('narxlar')

for price in set(mahsulotlar.values()):
    print(price)

dictionary = {}
dictionary['boolean'] = 'mantiqiy qiymat'
dictionary['float'] = 'onlik qiymat'
dictionary['intiger'] = 'butun son'
dictionary['variable'] = 'ozgaruvchi'
dictionary['for'] = 'tsikl'
dictionary['if'] = 'tekshirish operatori'
dictionary['man'] = 'mantiqiy qiymat'

for key in sorted(dictionary.keys()):
    print(key)

for key in sorted(dictionary.values()):
    print(key)
    
    
dunyo_davlat_poytaxtlari = {
    'aqsh' : 'washington D.C.',
    'france': 'paris',
    'germany':'berlin',
    'Uzbekistan':'Tahkent',
    'Qozogiston': 'Astana',
    'Qirgizistan': 'Bishkek'
    }
print('dunyo davlatlari')
for key in sorted(dunyo_davlat_poytaxtlari.keys()):
    print(key)
print('poytaxtlar')
for value in sorted(dunyo_davlat_poytaxtlari.values()):
    print(value)
print(sorted(dunyo_davlat_poytaxtlari.keys()))
print(sorted(dunyo_davlat_poytaxtlari.values()))



visit = input('qaysi davlatga kirishni xohlaysiz>>>').lower()

capital = dunyo_davlat_poytaxtlari.get(visit)


if capital == None:
    print('kechirasiz buhaqda malumot yoq')
else:
    print(f"{visit.upper()} davlati {capital.title()} poytaxti ")

taomlar = {
    'osh':10000,
    'manti':12000,
    'kabob':15000,
    'qozonkabob':20000,
    'lagmon':12000
    }

print('3 ta taom nomini kiriting')

buyurtmalar = []
for taom in range(3):
    buyurtmalar.append(input(f" {taom+1} - nomi >>>"))

for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()} {taomlar.get(buyurtma)}")
    else:
        print(f"bizda bu {buyurtma} mavjud emas")


'

car_0 = {
    'model': 'cobalt',
    'color': 'qizil',
    'yili': 2020
    }
car_1 = {
    'model': 'cobalt',
    'color': 'qizil',
    'yili': 2020
    }
car_2 = {
    'model': 'cobalt',
    'color': 'qizil',
    'yili': 2020
    }

cars = [car_0,car_1,car_2]
print(cars)

for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['color']} rangda, "
          f"{car['yili']} yil, ")

print(cars[0])
    
print(cars[2]['color'])
    
    
malibus = []
for n in range(10):
    new_car = {
        'model': 'malibu',
        'rang':None,
        'yili': 2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)

for n in malibus[:3]:
    n['rang'] = 'qora'
    
for n in malibus[3:6]:
    n['rang'] = 'qizil'
    
for n in malibus [6:]:
    n['rang'] = 'oq'
    n['korobka'] = 'mexanika'
    
for malibu in malibus:
    if malibu['korobka'] == 'avto' :
        malibu['narh'] = 45000
    else:
        malibu['narh'] = 30000    

print(malibus)
    
    
dasturchilar = {
    'ali': ['php', 'sql'],
    'vali': ['c#' ,'c++'],
    'maryam':['python','c++'],
    'bahron':['html','css']
    } 

for ism,tillar in dasturchilar.items():
    print(f"\n {ism.title()} tillarni biladi" ,end = '')
    for til in tillar:
        print(til.upper() ,end ='')
    
    
print(dasturchilar.items(),end = '')
    
    
hamkasblar = {
    'ali': {
        'yoshi': 18,
        'ishi': 'bekorchi',
        'kasbi': 'bloger',
        'bahron':['html','css']
        },
    'vali': {
        'yoshi': 18,
        'ishi': 'bekorchi',
        'kasbi': 'bloger',
        'bahron':['html','css']
        },
    'gani': {
        'yoshi': 18,
        'ishi': 'bekorchi',
        'kasbi': 'bloger',
        'bahron':['html','css']
        }
    }
    
for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['yoshi']}"
          f"{info['ishi'].title()}"
          f"malumoti {info['kasbi']}")
    for til in info['bahron']:
        print(til.upper())
    
mashhur_shaxslar_N1 = {
    'ism':'abdulla aavloniy',
    'yoshi': 54,
    'kasbi':'shoir',
    'asarlari': ['vatan','hammol']
}
mashhur_shaxslar_N2 = {
    'ism':'hamza hakimzoda',
    'yoshi': 43,
    'kasbi': 'yozuvchi',
    'asarlari':['juvonboz','abulfayzxon']
    }    
mashhur_shaxslar_N3 = {
    'ism':'maxmudxoja behbudiy',
    'yoshi': 47,
    'kasbi': 'yozuvchi',
    'asarlari':['teatr','ibratxonadur']
    }
    
mashhur_shaxslar = [mashhur_shaxslar_N1,mashhur_shaxslar_N2,mashhur_shaxslar_N3]

for mashhur in mashhur_shaxslar:
    ism = mashhur['ism']
    asarlari = mashhur['asarlari']
    print(f"{ism}ning mashhur asarlari")
    for asar in asarlari:
        print(asar)


dostlar = {
    'ali':['rambo','spiderman'],
    'vali':['its','raise of devil'],
    'aziz':['brother','universal'],
    'malun':['kemal','sunan']
    }

for ism,filmlar in dostlar.items():
    print(f"{ism.title()} uning sevimli filmi")
    for film in filmlar:
        print(film)



davlatlar = {
    'o`zbekiston' : {
        'poytaxti':'toshkent',
        'hududi': '445.998 kmkv',
        'aholisi': '35 mln.'
        },
    'rossiya' : {
        'poytaxti':'moskva',
        'hududi':'17 mln kmkv',
        'aholisi': '150 mln'
        },
    'qozogiston' : {
        'poytaxti':'astana',
        'hududi': 'bilmaymiz',
        'aholisi':'18 mln'}
    }

davlat_nomi = input('davlat nomini kiriting>>>>')

for name,info in davlatlar.items():
    name = name.title()
    poytaxti = info['poytaxti'].title()
    hududi = info['hududi']
    aholisi = info['aholisi']
if davlat_nomi != name.lower():
        print('bu davlat haqida bizda malumot yoq')
else:    
        print(f"{name}ning \n poytaxti {poytaxti},\n aholisi {aholisi} \n hududi {hududi}")



son = 1
while son <= 5:
    print(son,end='')
    son += 1

savol = 'istalgan sonni kiriting '
savol += "(dasturni toxtatish uchun `exit` sozini kiriting)"

while True :
    qiymat = input(savol)
    if qiymat =='exit' :
        break
    else:
        print(float(qiymat) **2)

sonlar = list(range(1,11))

for son in sonlar:
    if son == 5 :
        continue
    print(son **2)

    

son = 0

while son<10 :
    son += 1 
    if son%2 != 0:
        continue
    else:
        print(son)

libres = []
pregunta = 'anadir libro favoritos'
while True:
    valor = input(pregunta)
    if valor == 'salida' :
        break
    else:
        libres.append(valor)
        print(libres)


pregunta2 = 'cuantos anos tienes'
while True:
    valor = input(pregunta2)
    
    if valor == 'salida' or valor == 'exit':
        break
    
    elif int(valor)<= 0:
        break
    elif int(valor) <=7 or int(valor) >= 60:
        precio = 0
    elif int(valor) <= 18:
        precio = 10000
    else:
        precio = 20000
    print(f"precio para ti {precio}")


ismlar = []

print('yaqin dostlarimizni royhatini tuzamiz')
n =1
while True:
    savol = 'eng yaqin dostingizning ismini kiriting'
    ism = input(savol)
    ismlar.append(ism)
    javob = input('yana ism qoshasizmi (ha/yoq)')
    if javob == 'ha' :
        continue
        n += 1
    else:
        break


print('dostlarinizni royhatini tuzamiz')
dostlar = {}
ishora = True

while ishora :
    ism = input('dostingizni ismini kiriting')
    yosh = input(f"{ism.title()} yoshini kiriting")
    dostlar[ism] = int(yosh)
    
    javob = input('yana qoshasizmi (ha/yoq)')

    if javob != 'ha' :
        ishora = False
        
for ism,yosh in dostlar.items():
    print(f"{ism.title()} yoshi {yosh}")



talabalar = ['sardor','malun','murdashoy','mayib']
baholangan_talabalar = {}
while talabalar :
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} bahosini kiriting")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
    


orders = []
question = 'what food you want>>>'
while True:
    value = input(question)
    if value == 'exit' :
        break
    else:
        orders.append(value)
        print(orders)
    
foods = {}

while True:
    name = input('add the food')
    price = input('add price of food ')
    
    foods[name] = int(price)
    
    excuses = input('do you wanna keep on(yes/no)')
    if excuses == 'no' :
        break

while len(orders) :
    food = orders.pop()
    if food in foods:
        print(f"{food} : {foods[food]}" )
    else:
        print('sorry !there does not exist that food')

def salom_ber(ism):
    """bu funksiya haqida"""
    print(f"salom {ism.title()}")
    
salom_ber('aziz')

print(salom_ber.__doc__)


def yosh_hisoblash(ism,yosh):
    """bu funksiya yosh hisoblash uchun"""
    joriy_yil = 2023
    print(f"{ism.title()}ning yoshi {joriy_yil - yosh}da")

yosh_hisoblash('sulton', 1997)
son = int(input('istalgan sonni kiriting'))

def kvadrat_kub_hisoblash(son):
    """sonning kvadrat va kubini hisoblaydigan funksiya"""
    print(son**2)
    print(son**3)
    
kvadrat_kub_hisoblash(son)


def check_number():
    """this function for check status number"""
    numb =int(input('add the odd or even number'))
    if numb%2 == 0:
        print('this even number')
    else:
        print('this is odd number')
        
check_number()

def check_inequalites():
    """this function check inequalities"""
    numb_1 = int(input('add the first number'))
    numb_2 = int(input('add th second number'))
    if numb_1 == numb_2:
        print('numbers are equal')
    elif numb_1 > numb_2:
        print('first nummber greater then second')
    else:
        print('second number greater than first')

check_inequalites()
x =int(input('add te first number'))






def calculat(x , y =2) :
    """this function calculate """
    print(x**y)
calculat(x,4)
#son1 = int(input('sonni kiriting'))
def calculate(son):
    i = 2
    while i < 11:
        if not son%i:
            print(f"{son} soni {i}ga qoldiqsiz bolinadi")
        i += 1

calculate(30)

def toliq_ism1(ism,familiya,otasining_ismi = ''):
    
    if otasining_ismi:
        
        toliq_ism = ism +  familiya + otasining_ismi
    
    else:
        toliq_ism = ism + familiya
    
    
    return toliq_ism


toliq_ism = toliq_ism1('bahron', 'ramazonov','korvon ogli')
toliq_ism2 = toliq_ism1('ramz ','raximov')

print(toliq_ism2)

print(toliq_ism)

def avto_info(model,color,price = None):
    avto = {
        'model': model,
        'color': color,
        'price': price
        }
    return avto


avto1 = avto_info('malibu','black',10000)
avto2 = avto_info('gentra', 'white')

avtolar = [avto1,avto2]
print('bozordagi avtomashinalar')

for avto in avtolar:
    if avto['price']:
        price = avto['price']
    else:
        price = 'nomalum'
    print(f"{avto['model']} price : {price}")

def oraliq(min,max,step = 1) :
    array = []
    while min < max :
        array.append(min)
        min += step
    return array


son = oraliq(1,23)
print(son)

avtolar2 = []

while True:
    model = input('avtomashina modeli')
    color = input('rangini kiritng')
    price = int(input('narhni kiriting'))
    
    avtolar2.append(avto_info(model, color,price))
    
    javob = input('davom ettirishni xohlayapmiz')
    if javob == 'no' :
        break
    

def user_info(name,surname,date_of_birth,email_adress = None,phone_number = None) :
    user_info = {
        'name': name,
        'surname' : surname,
        'date_of_birth' : date_of_birth,
        'email' : email_adress,
        'phone_number': phone_number
        }

    return user_info

user = user_info('bahron', 'ramazonov',1997)
print(user)

users = []
while True:
    name = input('add your name')
    surname = input('add your surname')
    date_of_birth = input('add your date of birth')
    
    users.append(user_info(name,surname,date_of_birth))
    
    ask = input('do you want to continue yes or no')
    if ask == 'no' :
        break

print(users)



def equality(a,b,c) :
   if a > b and a > c :
       print(a)
   elif b > c and b > c :
        print(b)
   else:
        print(c)

equality(5,7,1)




def aylana(radius):
    radius = radius
    PI = 3.14
    diametr = 2 * radius
    C = PI * (radius ** 2)
    P = 2*PI*radius
    
    aylana = {
        'radius' : radius,
        'diametri':diametr,
        'yuzi': C,
        'premetri': P
        }
    return aylana


aylana1 = aylana(7)

print(aylana1)
def prime_number(a,b):
    prime_number = []
    if a == 1:
        a += 1
    while a < b:
        if a%2 != 0 or a == 2 :
            prime_number.append(a)
        a += 1
    return prime_number
prime1 =  prime_number()
print(prime1)

def summa(*arg) :
   return sum(arg)
sum_numbers = summa(1,2,3,4,5,6,7)
print(sum_numbers)

def avto_info(kompaniya,model,**kwargs) :
    kwargs['kompaniya'] = kompaniya
    kwargs['model'] = model
    return kwargs

avto1 = avto_info('mersedes', 'maybax', rang = 'qora',summa = '15000')
avto2 = avto_info('bmw', 'sedan', rang = 'oq',summa = '10000')

print(avto1)
print(avto2)


def kopaytma(*args):
    sum_of_numb = 1
    for numb in args:
        sum_of_numb *= numb
    return sum_of_numb

kopaytma1 = kopaytma(4,5,6,7,9,10)
print(kopaytma1)

def talaba(name,familia,**talabalar) :
    talabalar['name'] = name
    talabalar['familia'] = familia
    return talabalar

talaba1 = talaba('aziz', 'bafoev', date_of_birth = 2000, color = 'black')

print(talaba1)

print(math.exp(2))
'''









