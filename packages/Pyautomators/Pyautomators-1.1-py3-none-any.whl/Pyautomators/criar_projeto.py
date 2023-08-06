# script.py
'''
@author: KaueBonfim
'''
'''Este Modulo tem como fun��o gerar apartir de linha de comando um projeto no Padr�o de Pyautomators'''
import argparse
from Pyautomators.pyautomator import Project
if('__main__'==__name__):

    ARG=argparse.ArgumentParser()
    ARG.add_argument("-n",'--nome_projeto',required=True,help="Criar um projeto")
    ARG.add_argument("-d",'--diretorio',required=False,help="diretorio")
    
    projeto=dict(vars(ARG.parse_args()))
    Project().Criar_Projeto(projeto["nome_projeto"], projeto["diretorio"])