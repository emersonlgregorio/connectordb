import base64
import os

# Sua variável
nfsePdf = "data:application/pdf;name=NF 232.pdf;base64,spifffiledatadigest+6749fde0112f0e5f4471b924e87239b68774ee593dd9dab3a0cc2887a13677f8"

# Função para extrair o nome do arquivo
def extrair_nome_arquivo(s):
    chave = "name="
    idx_inicio = s.find(chave)
    if idx_inicio == -1:
        return "documento.pdf"
    idx_inicio += len(chave)
    idx_fim = s.find(";", idx_inicio)
    if idx_fim == -1:
        idx_fim = len(s)
    return s[idx_inicio:idx_fim]

nome_arquivo = extrair_nome_arquivo(nfsePdf)

# Pega apenas a parte base64 (depois da última vírgula)
base64_data = nfsePdf.split(",")[-1]

# Diretório de destino
pasta_destino = "/app/anexos"
os.makedirs(pasta_destino, exist_ok=True)

# Caminho completo do arquivo
caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

# Salva o arquivo no disco
with open(caminho_arquivo, "wb") as f:
    f.write(base64.b64decode(base64_data))

print(f"Arquivo salvo em: {caminho_arquivo}")
