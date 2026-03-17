from typing import Literal

class Ano:
    def __init__(self, ano: int):
        self.ano = ano
        self.bissexto = self.verificar_bissexto() #o ano já sabe se é bissexto ou não, não precisa ficar verificando toda hora

    def verificar_bissexto(self) -> bool: # Verificar se o ano é bissexto
        # Bissexto se divisível por 400, OU divisível por 4 mas não por 100
        if self.ano % 400 == 0:
            return True
        if self.ano % 100 == 0:
            return False
        if self.ano % 4 == 0:
            return True
        return False

    
def anos_sao_x(anos: list[Ano], situacao: Literal["bissexto", "nao_bissexto"]) -> bool:
    
    for ano in anos:
        if situacao == "bissexto":
            if not ano.bissexto:
                return False
        else:
            if ano.bissexto:
                return False
    return True

valores = [Ano(2017), Ano(2020), Ano(2023), Ano(2026), Ano(2030)]

if anos_sao_x(valores, "bissexto"):
    print("Todos os anos são bissextos")
elif anos_sao_x(valores, "nao_bissexto"):
    print("Nenhum ano é bissexto")
else:
    print("Alguns anos não são bissextos")