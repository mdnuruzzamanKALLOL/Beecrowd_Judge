main_value = input()

N1, N2, N3, N4 = main_value.split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

Media = (N1*2 + N2*3 + N3*4 + N4*1) / (2+3+4+1)

if Media >= 7:
    print("Media: {:.1f}\nAluno aprovado.".format(Media))
elif Media < 5:
    print("Media: {:.1f}\nAluno reprovado.".format(Media))
elif 5.0 <= Media <=6.9:
    print("Media: {:.1f}\nAluno em exame.".format(Media))
    N5 = float(input())
    print("Nota do exame:", N5)
    Media = (Media + N5) / 2
    if Media >= 5:
        print("Aluno aprovado.")
    elif Media <= 4.9:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(Media))