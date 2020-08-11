a=10
b=1
print(a+b)

var = 10
print(var)
print(10)

var1 = 3
var2 = 20
print(var1)
# var1 = var2 # 대입
print(var2)

# print(novar) # 없는 변수 출력시 오류

print(var2/var1) # 소수점까지 출력
print(var2//var1) # 소수점 자르고 출력

var1 = "파이썬"
print(var1)

var1 = "hello"
var2 = "world"
var3 = var1+" "+var2 +"!"

print(var1)
print(var2)
print(var3)

var3 = var3.replace('!','?') # !를 ?로 바꾸기
print(var3)

var1 = 'hello world'
finded1 = var1.find('a')
finded2 = var1.find('world')
print(finded1)
print(finded2)
# 못 찾으면 -1 출력, 찾으면 몇번째 있는지 알려줌

var = "hello world!"
print(var[0]) # 첫 글자 출력
print(var[1]) # 두 번째 글자 출력
print(var[0:4]) # 슬라이싱 하기 첫번째~네번째 출력 (0에서 3까지)

print(var[:]) # 전체 출력
print(var[:2]) # he 출력
print(var[2:]) # llo world 출력
print(var[-6:]) # 7번째부터 끝까지

var = "hello world !@"
print(var.split())

# print(var[20]) # 문자열 길이보다 큰 수를 입력하면 오류

var1 = "hello world"
var2 = "HELLO WORLD"
print(var1.upper())
print(var2.lower())

var = " hello world "
print(var.rstrip()) # 우측 공백 제거
print(var.lstrip()) # 좌측 공백 제거
print(var.strip()) # 양쪽 공백 제거

var0 = 'i am' + ' 홍길동'
print(var0)

var1 = "i am {name}".format(name="홍길동")
print(var1)

var2 = "i am {0}".format("홍길동")
print(var2)

var3 = "i am {0} i am {name}".format("홍길동", name="정보 문화사")
print(var3)

var4 = "i am {0} i am {1}".format("홍길동", "정보 문화사")
print(var4)

###################################################################################################

# list[] 리스트

var = list([1,2,3,4,5])
print(var)

var = [1,2,3,4,5]
print(var)

var = [1,2,"3",4,5,6]
print(var[0])
print(var[1])
print(var[0:4])

var = "hello world"
print(var.split())

a = ["1","2","3","4","5"]
b= ".".join(a)
print(b)

var1 = [1,2,3,4,5]
var2 = [6,7,8,9,10]
num = 3
print(var1 * 3)
print(var1+var2)

var = [1,2,3,4,5]
var.append(10) # 리스트 마지막에 요소 추가
print(var)

var.append(20)
print(var)

var = [1,2,3,4,5]
print(var.pop()) # 리스트 마지막 요소 제거
print(var)

var = ['a','d','c','b']
var.sort() # 정렬기능
print(var)
var.sort(reverse=True)
print(var)

a = [75,"a","A",98,100]
# print(a.sort()) #정렬시 만자와 숫자가 섞여 있다면 에러 발생

var = [1,2,3,4,5,6,7]
print(len(var)) # 리스트 길이

#################################################################################################

# dict{} 딕셔너리

var1 = dict({"key1":"value1","key2":"value2"}) # 딕셔너리 생성 및 키로 데이터 접근
var2 = {"key1":"value1","key2":"value2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])

var = {'key1': 'value1'}
# print(var['key2']) # 존재하지 않는 키를 접근하면 에러 발생

var = {'key1':'value1'}
print(var.get('key1'))
print(var.get('key1','default value'))
print(var.get('key2'))
print(var.get('key2','default value')) # get()을 활용하여 키가 존재하지 않을 때 기본 값을 출력

var = {}
print(var)
var["key1"] = 10
print(var)
var["key1"] = 20 # key: value 추가
var["key2"] = 30
print(var)

var = {}
print(var)
var.setdefault('key1', 10) # setdefault()를 활용하여 키가 존재하지 않을 때만 추가
print(var)
var.setdefault('key1',20)
var.setdefault('key2',30)
print(var)

var = {'key1':'value1','key3':'value3'}
print(var.keys()) #key 리스트 가져오기

var = {'key1': 'value1','key2':'value2'}
print(var.values()) #value 리스트 가져오기

var = {'key1': 'value1','key2':'value2'}
print(var.items()) # key-value 한 쌍으로 리스트 가져오기

var = {'key1': 'value1','key2':'value2'}
print('key1'in var) # True
print('hello'in var) # False
# key 존재 유무 검사

######################################################################################################

# tuple() 튜플

# 튜플은 데이터 변경 삭제가 불가능
var1 = tuple((1,))
var2 = tuple((1,2,3))
var3 = (1,)
var4 = (1,2,3)
# 튜플 생성
print(var1)
print(var2)
print(var3)
print(var4)

var1 = (1,2,3)
print(var1)
# var1[0] = 10 # 오류 발생

var1 = (1,2,3,4,5)
print(var1[3]) # 네번쨰
print(var1[2:]) # 세번째부터 끝까지

var1 = (1,2,3,4,5)
var2 = (11,22,33,44,55)
print(var1)
print(var2)
print(var1+var2)
print(var1*3)
print(var2*3)

#######################################################################################################

# if문 기본 구조

condition_t = True
condition_f = False

if condition_t: # True 이기 때문에 아래 2개 실행
    print('hello')
    print('world')
if condition_f: # False이기 때문에 아래 2개 실행 안함
    print('HELLO')
    print('WORLD')

print('last')

condition1 = True
condition2 = True
condition3 = True

if condition1:
    print('첫 번째 조건')
elif condition2:
    print('두 번째 조건')
elif condition3:
    print('세 번째 조건')
else:
    print('네 번째 조건')

if 'h' in 'hello world':
    print('hello world에 h가 포함되어 있습니다.')

if 1 in [11,22,33,44,55,66]:
    print([11,22,33,44,55,66],'에 1이 포함됩니다.')
else:
    print('1이 포함되지 않습니다.')
# in을 활용하여 포함유무 검사

######################################################################################################

signal_color = input('색을 영문으로 입력하세요: ')
# 값을 입력받을 때 input

if signal_color == 'blue' or signal_color == '파란색':
    print('신호등은 파란색입니다. 건너세요.')
else:
    print('신호등은 빨간색입니다. 기다리세요.')

#######################################################################################################

# 반복문

count = 0
while count<5:
    print('%d 번째 %d'%(count, count))
    count += 1

for i in range(0,5):
    print('%d 번째'%(i))
# range()를 이용한 반복문

for i in 'hello world':
    print(i)
# 문자열을 이용한 반복문

for i in [11,22,33,44,55]:
    print(i)
# 리스트를 이용한 반복문

var = {'key1':'value1', 'key2':'value2'}
for key in var:
    print(key)
    print(var[key])
# 딕셔너리를 이용한 반복문

for i in range(0,10):
    print(i)
    break # 해당 반복문 탈출
    print('test') # break 때문에 샐행 안됨

for i in range(0,10):
    print(i)
    continue # 아래는 실행하지 않고 그 다음으로 넘어감
    print('test') # continue 때문에 실행 안됨

# break는 반복문 자체를 탈출하는 것이고 continue는 continue 다음 실행문을 실행하지 않고 다음 인덱스로 넘어감

# 구구단
for i in range(2,5):
    for j in range(2,5):
        print('%d * %d = %d' %(i,j,i*j))

var = '''The small-business loan, along with the Bodensteins’ own cash reserves, allowed the couple to continue to 
pay their 21 workers for nearly three months. But by June 5, the day the money ran out, only 11 of the 75 children 
who attended the day care before the pandemic had returned, forcing the Bodensteins to furlough or lay off all 
but nine employees.'''

# 여러 줄에 나누고 싶을 때는 따옴표 3개 쓰면 된다. '''   '''  , """  """

space_ps = var.split(' ')
char_frequency = {}

for char in  space_ps:
    char_frequency.setdefault(char, 0)
    char_frequency[char] += 1
    print(char_frequency)

#####################################################################################################################

# def 키워드로 함수 생성

def f(x): # 함수 선언
    return x+10

var = f(10) # 함수 호출
print(var)

def division(x):
    if x%2:
        return True
    else:
        return False

    print('running') # 절대 실행되지 않음

var1 = division(10)
var2 = division(11)

print(var1)
print(var2)

# return 이 호출되면 해당 함수는 즉시 종료가 됨.
# return 아레에 있는 코드는 실행되지 않음
# 만약 함수에 return이 없다면 None 값 반환

def f(x,y):
    print('running' + str(x) + '' + str(y))
    return True

var1 = f(10,11)
print(var1)

def f(x,y):
    print('running' +str(x) + '' + str(y))
    return True

# var1 = f(10)
# print(var1) # 인자가 맞지 않으므로 오류 발생

def f(x, y=20):
    print('running' + str(x) +''+ str(y))
    return x+y

var1 = f(10)
var2 = f(10,40)

print(var1) # y의 값이 디폴트 값이 20 이므로 30출력
print(var2) # 50 출력

###################################################################################################################

# 클래스

def A_move():
    print('A charactor moved')

def B_move():
    print('B charactor moved')

# . . . 캐릭터가 늘어날수록 함수는 무한히 늘어남

class charactor: # 클래스 생성
    def move(self):
        print('move')

    def attack(self):
        print('attack')

player_a = charactor() # 객체 생성
player_b = charactor() # 객체 생성

player_a.move() # move 출력
player_a.attack() # attack 출력

class charactor:
    def move(self):
        print(self, 'move')

    def attack(self):
        print(self, 'attack')

player_a = charactor() # 객체 생성
player_a.move() # move 출력
player_a.attack() # attack 출력

print('-------------------------------------------------------------------------------------------------')

class charactor:
    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

player_a = charactor()
player_b = charactor()

player_a.move()
player_b.move()

class charactor:
    def create(self,hp,attack,defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self,'attack')

    def show_info(self):
        print("hp: %d, attack: %d, defence: %d" %(self.hp, self.attack, self.defence))

player_a = charactor()
player_b = charactor()

player_a.create(10,20,30)
player_b.create(100,200,300)

player_a.show_info()
player_b.show_info()

# 생성자를 만들지 않으면 자동 생성된다.

print('---------------------------------------------------------------------------------------------------')

# 생성자 __init__()
class charactor:
    def __init__(self,hp,attack,defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print('player가 생성되었습니다.')

    def show_info(self):
        print("hp: %d, attack: %d, defence: %d" %(self.hp, self.attack, self.defence))

player_a = charactor(10,20,30)
player_b = charactor(100,200,300)

player_a.show_info()
player_b.show_info()

class charactor:
    def __init__(self,hp,attack,defence):
        pass
    # 아무것도 안할 때는 pass

    def __del__(self):
        print('player가 죽었습니다.')
    # 객체의 할당 해제시 자동으로 호출되는 소멸자

player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)

del player_a
del player_b
del player_c


print('')
print('call')

# __call__
# __call__은 해당 객체가 호출될 때 호출되는 함수

class charactor:

    def __init__(self, hp):
        self.hp = hp
        print("생성")

    def __call__(self):
        print('hp: %d' %(self.hp))

player_a = charactor(10)
player_b = charactor(100)

player_a()
player_b()

callable(player_a) # 실행 가능한지 판별
print(callable(player_a))


# 속성 접근 방법
# 마침표(.)를 이용하여 호출
class charactor:
    def __init__(self,hp):
        self.hp = hp
        print('생성')

player_a = charactor(10)
player_b = charactor(100)

print(player_a.hp)
print(player_b.hp)

##############################################################################################################
print("---------------------------------static---------------------------------------------")

# 스태틱 메소드
# 객체를 생성하지 않아도 접근할 수 있게 하는 것이 스태틱이다.
# 스태틱 메소드는 첫 번째 인자로 self 인자를 받지 않음
class namespace1:
    @staticmethod
    def s1():
        print('namespace1 s1 스태틱 메소드')

    @staticmethod
    def s2():
        print('namespace1 s2 스태틱 메소드')


class namespace2:
    @staticmethod
    def s1():
        print('namespace2 s1 스태틱 메소드')

    @staticmethod
    def s2():
        print('namespace2 s2 스태틱 메소드')

namespace1.s1()
namespace2.s2()

# 클래스 변수에 접근할 땐 self 인자가 아닌 클래스 이름으로 접근할 수 있다.

class charactor:
    char_cnt = 0

    def __init__(self,hp,attack,defence):
        self.info = {
            'hp':hp,
            'attack':attack,
            'defence':defence
        }
        charactor.char_cnt += 1

        print('생성 유닛수 : %d'%(charactor.char_cnt))

player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)

print(charactor.char_cnt)


# 상속

class unit:
    unit_count = 0

    def __init__(self):
        print('생성')
        unit.unit_count += 1

    def move(self):
        print('unit move')

class bird(unit): # 이렇게 상속받는다.
    def __init__(self):
        print('bird 생성')

b1 = bird()
b2 = bird()
b3 = bird()

b1.move()
print(unit.unit_count)

# 하지만 unit 클래스의 생성자가 정상적으로 실행되지 않는 현상 발생
# unit 클래스의 상속자 실행 안됨 (부모 클래스 상속자 실행 안됨)


# super를 이용하면 부모클래스 상속자 실행 가능
class unit:
    unit_count = 0

    def __init__(self):
        print('unit 생성')
        unit.unit_count += 1

    def move(self):
        print('unit move')

class bird(unit): # 이렇게 상속받는다.
    def __init__(self):
        print('bird 생성')
        super(bird, self).__init__() # 부모 클래스 상속자 실행시키기

b1 = bird()
b3 = bird()

b1.move()

print(unit.unit_count)

