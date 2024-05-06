N1, N2, N3 ,N4 = map(float, input().split())
media = (N1*2 + N2*3 + N3*4 + N4)/10
print ("Media: {:.1f}".format(media))
if media >= 7.0:
  print ("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
  print ("Aluno em exame.")
  Nexame = float(input())
  print ("Nota do exame: {:.1f}".format(Nexame))
  mediaf = (media + Nexame)/2
  if mediaf >= 5.0:
    print ("Aluno aprovado.")
  else:
    print ("Aluno reprovado.")

  print("Media final: {:.1f}".format(mediaf))
elif media < 5.0:
     print ("Aluno reprovado.")