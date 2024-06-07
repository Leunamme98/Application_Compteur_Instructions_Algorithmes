

operation = 0
code = """operation = 0
a = 0
operation+=1
b = 50
operation+=1
while a<b:
    operation+=1
    a+=1 


operation+=1

"""

exec(code)

print(operation)

def traitementCode(code: str) -> str:
    """
    La fonction permet d'insérer des compteurs d'instructions dans un code python
    @param: code initial sans compteur
    @return: code avec compteur d'instructions
    """

def compteurDoperation(code: str) -> int:
    operation = 0
