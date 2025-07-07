#!/bin/bash

echo "🚀 Iniciando Classificador de E-mails com IA..."

# Detecta o comando Python correto
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✅ Usando python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo "✅ Usando python"
else
    echo "❌ Python não encontrado!"
    exit 1
fi

# Verifica se o Flask está instalado
$PYTHON_CMD -c "import flask; print('Flask version:', flask.__version__)" || {
    echo "❌ Flask não encontrado!"
    exit 1
}

# Inicia a aplicação
echo "🚀 Iniciando aplicação Flask..."
$PYTHON_CMD app_final.py 