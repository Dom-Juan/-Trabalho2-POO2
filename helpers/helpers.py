
# ############################################################### #
# Classe para operações lógicas não específicas de modelo,        #
# ajudando em lógicas de negócio e derivados.                     #
# ############################################################### #

# Converte STR para boolean
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")