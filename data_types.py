"""data_types"""
#int
print(type(1))

#float
print(type(0.121))

#string
print(type('hello_world'))

#bool
print(type(True))
print(type(16<8))

#list
print(type([]))
print(type([1,2,3]))
a=[1,2,3]
a.clear()
print(a)

#tuple
print(type((1,)))
a=1,
print(type(a))

#set
a={1,2,3}
print(type(a))

#dict
a={1:"python"}
print(type(a))

#complex
print(type(1+2j))
print(type(4j))

#bytes
print(type(b'hiiii'))

#bytearray
print(type(bytearray(b'hi')))