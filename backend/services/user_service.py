# TODO : VALIDAR HASH PASSWORD
# TODO : DEAL WITH NOT UNIQUE EXCEPTIONS FROM BEANIE
# TODO : VALIDATE UPDATED AT ALWAYS GREATER THAN CREATED AT
# TODO : LEMBRAR DE SÓ PERMITIR ROTAS COM IDS PARA USUÁRIOS AUTENTICADOS (também vale para o list e create)
# no controller as exceções de validação são tratadas pelo fastapi então é ok, mas...
#  ... para exceções disparadas pela camada de serviço eu preciso tratar elas usando @app.exception_handler

# TODO: usar Passlib ou Bcrypt para hashear a senha

# LEMBRAR:
#   - CRIAÇÃO DA INTERAÇÃO VAI SER NO FINALLY DEPOIS DE EXECUTAR A CONEXÃO COM A IA E TER A RESPOSTA
#   - lembrar de implementar no story service um método que busque o path das interações a partir do draft id
