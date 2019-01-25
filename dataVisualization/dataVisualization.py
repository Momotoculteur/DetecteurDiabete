import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




def plotAllGraphByType(data, arg):
    '''
    Permet de tracer l'emsemble des graphiques par type d'information
    :param data: dataset
    :param arg:
        - all : Affiche l'ensemble des données
        - 0 :  Affiche seulement les coubres des non diabetiques
        - 1 : Affiche seulement les courbes des diabetiques
    :return:
    '''

    if arg == 'all':
        displayDf = data.iloc[:,0:7]
        displayDf.hist(bins=20, edgecolor='black')
    elif arg == '0':
        data = data[data.Outcome == 0]
        displayDf = data.iloc[:,0:7]
        displayDf.hist(bins=20, edgecolor='black')

    elif arg == '1':
        data = data[data.Outcome == 1]
        displayDf = data.iloc[:, 0:7]
        displayDf.hist(bins=20, edgecolor='black')

    #plt.tight_layout()
    #plt.savefig('Graphique tout individu confondu')
    #plt.show()

def pairPlot(data):
    '''
    Fonction permettant de mettre en relation l'ensemble de nos attributs
    :param data:
    :return:
    '''
    sns.pairplot(data, hue='Outcome', diag_kind='kde')
    plt.savefig('Pair plot')
    

def main():
    '''
    Fonction principal
    :return:
    '''

    # Chargement du dataset
    data = pd.read_csv('..\\dataset\\dataset.csv')

    # 2nd arg : all, 0, 1
    #plotAllGraphByType(data, 'all')

    pairPlot(data)



if __name__== "__main__":
    main()