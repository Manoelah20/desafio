#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Teste do sistema de respostas
from backend.utils.responder_local import gerar_resposta_inteligente, identificar_tipo_email
from backend.utils.classifier import classificar_email

def testar_sistema():
    # Teste 1: Email produtivo
    email1 = "Preciso de suporte com minha conta. Há uma pendência no pagamento."
    categoria1 = classificar_email(email1)
    resposta1 = gerar_resposta_inteligente(email1, categoria1)
    
    print("=== TESTE 1: Email Produtivo ===")
    print(f"Email: {email1}")
    print(f"Categoria: {categoria1}")
    print(f"Resposta: {resposta1}")
    print()
    
    # Teste 2: Email improdutivo
    email2 = "Olá! Como você está? Tudo bem por aí?"
    categoria2 = classificar_email(email2)
    resposta2 = gerar_resposta_inteligente(email2, categoria2)
    
    print("=== TESTE 2: Email Improdutivo ===")
    print(f"Email: {email2}")
    print(f"Categoria: {categoria2}")
    print(f"Resposta: {resposta2}")
    print()
    
    # Teste 3: Verificar tipo de email
    tipo1 = identificar_tipo_email(email1, categoria1)
    tipo2 = identificar_tipo_email(email2, categoria2)
    
    print("=== TIPOS IDENTIFICADOS ===")
    print(f"Email 1 - Tipo: {tipo1}")
    print(f"Email 2 - Tipo: {tipo2}")

if __name__ == "__main__":
    testar_sistema() 