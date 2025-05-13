#!/usr/bin/env python
import os
import sys
import argparse
from app import app
from generate_placeholders import generate_placeholder_images

def setup_environment():
    """Configura o ambiente para a aplicação"""
    # Verificar se as pastas necessárias existem
    if not os.path.exists('static'):
        os.makedirs('static')
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    if not os.path.exists('static/css'):
        os.makedirs('static/css')
    if not os.path.exists('static/js'):
        os.makedirs('static/js')
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Gerar imagens placeholder se não existirem
    if not os.path.exists('static/images/placeholder1.jpg'):
        print("Gerando imagens placeholder...")
        generate_placeholder_images()
    
    print("Ambiente configurado com sucesso!")

def main():
    parser = argparse.ArgumentParser(description='Servidor web para Na Lenha com Ferreira')
    parser.add_argument('--setup', action='store_true', help='Configurar ambiente')
    parser.add_argument('--host', default='0.0.0.0', help='Host para o servidor (padrão: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=5000, help='Porta para o servidor (padrão: 5000)')
    parser.add_argument('--debug', action='store_true', help='Executar em modo debug')
    
    args = parser.parse_args()
    
    if args.setup:
        setup_environment()
        return
    
    # Configurar ambiente se não existir pastas necessárias
    if not os.path.exists('static/images'):
        print("Configuração inicial necessária...")
        setup_environment()
    
    print(f"Iniciando servidor em http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == '__main__':
    main()
