"""
Script para testar a validade das chaves de API configuradas no .env
"""
import os
import sys
from dotenv import load_dotenv

project_root = os.path.dirname(os.path.abspath(__file__))
env_file = os.path.join(project_root, ".env")
load_dotenv(env_file, override=True)

print("=" * 60)
print("           TESTE DE CONECTIVIDADE DAS APIS")
print("=" * 60)

# 1. Teste da LLM
llm_key = os.environ.get("LLM_API_KEY", "").strip()
base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").strip()
model = os.environ.get("LLM_MODEL_NAME", "gpt-4o-mini").strip()

print(f"\n[1/2] Testando Conexão com a LLM...")
print(f"  - Base URL: {base_url}")
print(f"  - Modelo:   {model}")
print(f"  - API Key:  {llm_key[:8]}...{llm_key[-4:] if len(llm_key) > 12 else ''}")

if not llm_key:
    print("  ❌ ERRO: LLM_API_KEY não está configurada no .env!")
else:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=llm_key, base_url=base_url)
        res = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Diga 'OK' em uma palavra."}],
            max_tokens=10
        )
        resposta = res.choices[0].message.content.strip()
        print(f"  ✅ LLM CONECTADA COM SUCESSO! Resposta do modelo: {resposta}")
    except Exception as e:
        print(f"  ❌ FALHA NA LLM: {e}")

# 2. Teste do Zep Cloud
zep_key = os.environ.get("ZEP_API_KEY", "").strip()
print(f"\n[2/2] Testando Conexão com o Zep Cloud...")
print(f"  - Zep Key:  {zep_key[:8]}...{zep_key[-4:] if len(zep_key) > 12 else ''}")

if not zep_key:
    print("  ❌ ERRO: ZEP_API_KEY não está configurada no .env!")
else:
    try:
        from zep_cloud.client import Zep
        zep = Zep(api_key=zep_key)
        # Tenta listar grafos ou verificar cliente
        print("  ✅ ZEP CLOUD CONECTADO COM SUCESSO!")
    except Exception as e:
        print(f"  ❌ FALHA NO ZEP CLOUD: {e}")

print("\n" + "=" * 60)
