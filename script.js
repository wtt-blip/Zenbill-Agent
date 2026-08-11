function responderAgente(acao) {
    const alertCard = document.getElementById('alertCard');
    const logTable = document.getElementById('logTable');
    
    if (acao === 'contestar') {
        alertCard.innerHTML = `
            <div class="card-body bg-light-subtle text-success">
                <h5 class="fw-bold"><i class="bi bi-check-circle-fill me-2"></i>Ação Enviada ao Agente!</h5>
                <p class="mb-0">O Strands Agent gerou um e-mail formal de contestação para a operadora citando o histórico de cobrança. Você receberá atualizações assim que a operadora responder.</p>
            </div>`;
        
        setTimeout(() => {
            const newRow = `
                <tr>
                    <td>Hoje - Agora</td>
                    <td>Internet / Fibra Telecom</td>
                    <td>Contestação enviada automaticamente para a operadora.</td>
                    <td>R$ 180,00</td>
                    <td><span class="badge bg-warning text-dark status-pill">Em Contestação</span></td>
                </tr>`;
            logTable.innerHTML = newRow + logTable.innerHTML;
        }, 800);
    } else {
        alertCard.innerHTML = `
            <div class="card-body text-secondary">
                <p class="mb-0"><i class="bi bi-check-circle me-1"></i>Pagamento aprovado. Agendamento realizado com sucesso.</p>
            </div>`;
    }
}

function simularUpload() {
    alert("Simulação: Agente lendo nova fatura enviada em PDF e extraindo os dados via Strands SDK...");
}
