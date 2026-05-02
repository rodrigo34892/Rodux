
# 🛡️ RODUX

**RODUX** é uma ferramenta de **Blue Team** em desenvolvimento, focada em **Monitoramento de Integridade de Arquivos (FIM)** para ambientes Linux.

O projeto visa detectar, de forma automática e recursiva, qualquer criação, alteração ou exclusão de arquivos em diretórios críticos. Ao operar como um serviço nativo (daemon), o Rodux garante vigilância contínua para identificação de possíveis comprometimentos no sistema.

### 🚀 Principais Funções:
*   **Vigilância Recursiva:** Monitoramento completo de pastas e subpastas.
*   **Persistência:** Execução em segundo plano via `systemd` (mesmo após reboot).
*   **Auditoria:** Registro de eventos em log estruturado para análise de incidentes.

