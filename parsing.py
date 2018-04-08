import csv

setosa = list()
versicolor = list()
virginica = list()

#Separando os elementos do arquivo csv
with open('iris.csv', 'rb') as csvfile:
    irisdb = csv.reader(csvfile)
    for row in irisdb:
        if row[-1] == "Iris-setosa":
            setosa.append(row)
        elif row[-1] == "Iris-versicolor":
            versicolor.append(row)
        else:
            virginica.append(row)

# Criando as matrizes de comparacao
matrix_setosa = list()
matrix_versicolor = list()
matrix_virginica = list()
for i in range(0,len(setosa)):
    for j in range(i+1, len(setosa)):
        matrix_setosa.append([str(float(setosa[i][0])-float(setosa[j][0])),
                              str(float(setosa[i][1])-float(setosa[j][1])),
                              str(float(setosa[i][2])-float(setosa[j][2])),
                              str(float(setosa[i][3])-float(setosa[j][3]))])
        matrix_versicolor.append([str(float(versicolor[i][0])-float(versicolor[j][0])),
                                  str(float(versicolor[i][1])-float(versicolor[j][1])),
                                  str(float(versicolor[i][2])-float(versicolor[j][2])),
                                  str(float(versicolor[i][3])-float(versicolor[j][3]))])
        matrix_virginica.append([str(float(virginica[i][0])-float(virginica[j][0])),
                                  str(float(virginica[i][1])-float(virginica[j][1])),
                                  str(float(virginica[i][2])-float(virginica[j][2])),
                                  str(float(virginica[i][3])-float(virginica[j][3]))])
for i in range(0, len(matrix_setosa)):
    print(matrix_setosa[i])
