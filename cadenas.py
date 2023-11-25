mi_texto = "abcdefghijklmnopqrstuvwxyz"
#print(mi_texto[3])
#print(mi_texto[-1])

#print(mi_texto.index("z"))
#print(mi_texto.index("v", 7, 25)) #si no lo encuentra arroja error
#.index() busca del principio al final
#.rindex() busca del final al principio
#.find("a") si no lo encuentra no debuelve un error como index



#######################     SUB-STRINGS     #########################

sub = mi_texto[2]
sub2 = mi_texto[2:6]
sub3 = mi_texto[1:20:3]
sub4 = mi_texto[10:]
#print(sub3)



##############      METODOS     ############
verso = "hola aca aran un split"
split = verso.split()  #saca un vector
split2 = verso.split("a")
#print(split2)

a = "Python"
b = "is"
c = "the"
d = "better"
e = "languaje"
union = " ".join([a,b,c,d,e])
print(union)


texto = "cosas que remplazar"
nuevoTexto = texto.replace("a","e") #.ramplaza("esto","por esto")