import json
from dataclasses import dataclass

@dataclass
class Invoice:
    service_name: str
    amount: float
    historical_avg: float

class ZenBillAgent:
    def __init__(self, threshold_percentage: float = 0.15):
        self.threshold = threshold_percentage

    def process_invoice(self, invoice: Invoice) -> dict:
        """
        Lógica do Strands Agent para avaliar se a fatura roda em segundo plano 
        ou requer intervenção humana (Human-in-the-Loop).
        """
        diff = (invoice.amount - invoice.historical_avg) / invoice.historical_avg

        if diff > self.threshold:
            return {
                "status": "HUMAN_APPROVAL_REQUIRED",
                "reason": f"Anomalia de {diff * 100:.1f}% detectada.",
                "action_recommended": "CONTEST_OR_APPROVE",
                "service": invoice.service_name,
                "amount": invoice.amount
            }
        
        return {
            "status": "AUTONOMOUS_EXECUTION",
            "reason": "Valor dentro da média aceitável.",
            "action": "SCHEDULED_PAYMENT",
            "service": invoice.service_name,
            "amount": invoice.amount
        }

if __name__ == "__main__":
    agent = ZenBillAgent(threshold_percentage=0.15)
    
    # Exemplo 1: Conta dentro do normal (Execução Silenciosa)
    fatura_luz = Invoice(service_name="Enel Luz", amount=132.40, historical_avg=130.00)
    print("Processando Fatura Luz:", json.dumps(agent.process_invoice(fatura_luz), indent=2, ensure_ascii=False))

    # Exemplo 2: Conta com anomalia (Ativa Human-in-the-Loop)
    fatura_internet = Invoice(service_name="Fibra Telecom", amount=180.00, historical_avg=140.00)
    print("\nProcessando Fatura Internet:", json.dumps(agent.process_invoice(fatura_internet), indent=2, ensure_ascii=False))
