# -*- coding: utf-8 -*-
"""Machine_Learning_ Alura_care.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xp2-sSt70X6Fy31Bs5f7319WHGWeTpiu

# Importando pacote pandas
"""

import pandas as pd

"""#importando os dados """

Resultados = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Alura/Machine Learning: lidando com dados de muitas dimensões /reducao-dimensionalidade-master/reducao-dimensionalidade-master/data-set/exames.csv")
Resultados.head()

Resultados.shape

from sklearn.model_selection import train_test_split
from numpy import random

SEED = 123143
random.seed(SEED)

valores_exames = Resultados.drop(columns=['id', 'diagnostico'])
diagnostico = Resultados.diagnostico

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames, 
                                                        diagnostico)

treino_y.head()

#from sklearn.ensemble import RandomForestClassifier

#classificador = RandomForestClassifier(n_estimators = 100)
#classificador.fit(treino_x, treino_y)
#classificador.score(teste_x, teste_y)

Resultados.isnull()

Resultados.isnull().sum()

int(False)

419/569

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from numpy import random

SEED = 123143
random.seed(SEED)

valores_exames = Resultados.drop(columns=['id', 'diagnostico'])
diagnostico = Resultados.diagnostico
valores_exames_v1 = valores_exames.drop(columns="exame_33")

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v1, 
                                                        diagnostico, 
                                                        test_size=0.3)


classificador = RandomForestClassifier(n_estimators = 100)
classificador.fit(treino_x, treino_y)
print("Resultado da Classificação %.2f%%" %(classificador.score(teste_x, teste_y)*100))

from sklearn.dummy import DummyClassifier

SEED = 123143
random.seed(SEED)

classificador_bobo = DummyClassifier(strategy = "most_frequent")
classificador_bobo.fit(treino_x, treino_y)
print("Resultado da Classificação bobo %.2f%%" %(classificador_bobo.score(teste_x, teste_y)*100))

#dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                   #var_name="exames",
                   #value_name="valores")

#dados_plot.head()

import seaborn as sns
import matplotlib.pyplot as plt


dados_plot = pd.concat([diagnostico, valores_exames_v1.iloc[:,0:10]], axis=1)
dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                   var_name="exames",
                   value_name="valores")
plt.figure(figsize=(10, 10))
sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
               data = dados_plot)

plt.xticks(rotation = 90)

from sklearn.preprocessing import StandardScaler

padronizador = StandardScaler()
padronizador.fit(valores_exames_v1)
valores_exames_v2 = padronizador.transform(valores_exames_v1)
valores_exames_v2

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

padronizador = StandardScaler()
padronizador.fit(valores_exames_v1)
valores_exames_v2 = padronizador.transform(valores_exames_v1)
valores_exames_v2 = pd.DataFrame(data = valores_exames_v2, 
                                 columns=valores_exames_v1. keys())

dados_plot = pd.concat([diagnostico, valores_exames_v2.iloc[:,0:10]], axis=1)
dados_plot = pd.melt(dados_plot, id_vars="diagnostico",
                   var_name="exames",
                   value_name="valores")
plt.figure(figsize=(10, 10))
sns.violinplot(x = "exames", y = "valores", hue = "diagnostico",
               data = dados_plot, split=True)

plt.xticks(rotation = 90)

valores_exames_v1.exame_4

def grafico_violino(valores, inicio, fim):

    dados_plot = pd.concat([diagnostico, valores.iloc[:,inicio:fim]], axis = 1)
    dados_plot = pd.melt(dados_plot, id_vars="diagnostico", 
                         var_name="exames",
                         value_name="valores")

    plt.figure(figsize=(10,10))

    sns.violinplot(x = "exames", y = "valores", hue = "diagnostico", 
                    data = dados_plot, split = True)

    plt.xticks(rotation = 90)

grafico_violino(valores_exames_v2, 10, 21)

grafico_violino(valores_exames_v2, 21, 32)

valores_exames_v3 = valores_exames_v2.drop(columns=["exame_29", "exame_4"])

def classificar(valores):
    SEED = 123143
    random.seed(SEED)
    treino_x, teste_x, treino_y, teste_y = train_test_split(valores, 
                                                            diagnostico, 
                                                            test_size = 0.3)

    classificador = RandomForestClassifier(n_estimators = 100)
    classificador.fit(treino_x, treino_y)
    classificador.fit(treino_x, treino_y)
    print("Resultado da classificação %.2f%%" % (classificador.score(teste_x, teste_y)* 100))

classificar(valores_exames_v3)

"""# Calculando a coorelação """

matriz_correlacao = valores_exames_v3.corr()
plt.figure(figsize= (17, 15))
sns.heatmap(matriz_correlacao, annot=True, fmt=".1f")

matriz_correlacao_v1 = matriz_correlacao[matriz_correlacao>0.99]
matriz_correlacao_v1

matriz_correlacao_v2 = matriz_correlacao_v1.sum()
matriz_correlacao_v2

variaveis_correlacionadas = matriz_correlacao_v2[matriz_correlacao_v2>1]
variaveis_correlacionadas

valores_exames_v4 = valores_exames_v3.drop(columns=variaveis_correlacionadas.keys())

valores_exames_v4.head()

classificar(valores_exames_v4)

valores_exames_v5 = valores_exames_v3.drop(columns=["exame_3", "exame_24"])
classificar(valores_exames_v5)

"""### usando a função SelectKBest para selecionar as melhores features

https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

selecionar_kmelhores = SelectKBest(chi2, k = 5)

selecionar_kmelhores



valores_exames_v6 = valores_exames_v1.drop(columns=(["exame_4", "exame_29", "exame_3", "exame_24"]))

SEED=1234
random.seed(SEED)

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v6, 
                                                        diagnostico, 
                                                        test_size=0.3)


selecionar_kmelhores.fit(treino_x,treino_y)
treino_kbest =selecionar_kmelhores.transform(treino_x)
teste_kbest =selecionar_kmelhores.transform(teste_x)

treino_kbest.shape

classificador = RandomForestClassifier(n_estimators=100, random_state=1234)
classificador.fit(treino_kbest,treino_y)
print("Resuldado da classificação %.2f%%" %(classificador.score(teste_kbest, teste_y)*100))

"""### verificando a eficácia do classificador com a matrix de confusão 

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
"""

from sklearn.metrics import confusion_matrix

matriz_confusao = confusion_matrix(teste_y, classificador.predict(teste_kbest))

sns.set()
sns.heatmap(matriz_confusao, annot=True, fmt="d").set(xlabel = "Predição", ylabel= "Real")

matriz_confusao

"""

https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html"""

from sklearn.feature_selection  import RFE

SEED=1234
random.seed(SEED)

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v6, 
                                                        diagnostico, 
                                                        test_size=0.3)

classificador = RandomForestClassifier(n_estimators=100, random_state=1234)
classificador.fit(treino_x,treino_y)
selecionador_rfe = RFE(estimator = classificador, n_features_to_select= 2, step=1)
selecionador_rfe.fit(treino_x, treino_y)
treino_rfe = selecionador_rfe.transform(treino_x)
teste_rfe = selecionador_rfe.transform(teste_x)
classificador.fit(treino_rfe,treino_y)

matriz_confusao = confusion_matrix(teste_y, classificador.predict(teste_rfe))
sns.set()
sns.heatmap(matriz_confusao, annot=True, fmt="d").set(xlabel = "Predição", ylabel= "Real")


print("Resuldado da classificação %.2f%%" %(classificador.score(teste_rfe, teste_y)*100))

"""# predição """

from sklearn.feature_selection  import RFECV

SEED=1234
random.seed(SEED)

treino_x, teste_x, treino_y, teste_y = train_test_split(valores_exames_v6, 
                                                        diagnostico, 
                                                        test_size=0.3)

classificador = RandomForestClassifier(n_estimators=100, random_state=1234)
classificador.fit(treino_x,treino_y)
selecionador_rfecv = RFECV(estimator = classificador, cv = 5, step=1, scoring = "accuracy")
selecionador_rfecv.fit(treino_x, treino_y)
treino_rfecv = selecionador_rfecv.transform(treino_x)
teste_rfecv = selecionador_rfecv.transform(teste_x)
classificador.fit(treino_rfecv,treino_y)

matriz_confusao = confusion_matrix(teste_y, classificador.predict(teste_rfecv))
sns.set()
sns.heatmap(matriz_confusao, annot=True, fmt="d").set(xlabel = "Predição", ylabel= "Real")


print("Resuldado da classificação %.2f%%" %(classificador.score(teste_rfecv, teste_y)*100))

selecionador_rfecv.n_features_

selecionador_rfecv.support_

treino_x.columns[selecionador_rfecv.support_]

selecionador_rfecv.cv_results_

selecionador_rfecv.cv_results_['mean_test_score']

len(selecionador_rfecv.cv_results_['mean_test_score'])

import matplotlib.pyplot as plt

plt.figure(figsize = (10, 4))
plt.xlabel("Número de exames")
plt.ylabel("Acurácia")

plt.plot(range(1, len(selecionador_rfecv.cv_results_['mean_test_score']) +1), selecionador_rfecv.cv_results_['mean_test_score']) 
plt.show()

Resultados

valores_exames_v7 = selecionador_rfe.transform(valores_exames_v6)

valores_exames_v7.shape

valores_exames_v7

import seaborn as sns
plt.figure(figsize=(10, 6))
sns.scatterplot (x = valores_exames_v7 [:,0], y = valores_exames_v7 [:,1] , hue = diagnostico)

"""# Técnica PCA
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
"""

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

valores_exames_v8 = pca.fit_transform(valores_exames_v6)
plt.figure(figsize=(10, 6))
sns.scatterplot (x = valores_exames_v8 [:,0], y = valores_exames_v8 [:,1] , hue = diagnostico)

valores_exames_v8

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

valores_exames_v8 = pca.fit_transform(valores_exames_v5)
plt.figure(figsize=(10, 6))
sns.scatterplot (x = valores_exames_v8 [:,0], y = valores_exames_v8 [:,1] , hue = diagnostico)

"""# Aplicando TSNE

https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
"""

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)

valores_exames_v9 = tsne.fit_transform(valores_exames_v5)
plt.figure(figsize=(10, 6))
sns.scatterplot (x = valores_exames_v9 [:,0], y = valores_exames_v9 [:,1] , hue = diagnostico)

