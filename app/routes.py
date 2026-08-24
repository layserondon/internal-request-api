from flask import Blueprint, request, jsonify

tickets_bp = Blueprint("tickets", __name__)

# registrar e acompanhar slicitaçõs internas
# cada ticket terá: 
                # id "ticket/<int:ticket_id>"
                # title e description "ticket/<ticket_title>?description=<ticket_description>"
                # requester - quem solicitou a ação "ticket/<ticket_title>?requester=<requester_name&requester_contato>"
                # assignee - quem cumprirá a solicitação
                # priority - open, in_progress, resolved, cancelled
                # status - Low, medium, High, critical
                # created_at - solicitado em (email, whatasapp)
                # updated_at - atualizado em (email, whatasapp) na data tal.

tickets = [

        {
            "id": 1,
            "title": "Action 1",
            "description": "Descrição detalhada da solicitação",
            "requester": {
                "name": "Nome do Solicitante",
                "contact": "Contato do Solicitante"
            },
        "assignee": {
            "name": "Nome do Responsável",
            "contact": "Contato do Responsável"
        },
        "priority": "Alta",
        "status": "Aberto",
        "created_at": "2024-06-01T10:00:00Z",
        "updated_at": "Ainda não foi atualizado"
        },
        
        {
        "id": 2,
        "title": "Action 2",   
        "description": "Descrição detalhada da solicitação 2",
        "requester": {
            "nome": "Nome do Solicitante 2",
            "contato": "Contato do Solicitante 2"
        },
        "assignee": {
            "nome": "Nome do Responsável 2",
            "contato": "Contato do Responsável 2"
        },
        "priority": "Média",
        "status": "Em andamento",
        "created_at": "2024-06-02T14:30:00Z",
        "updated_at": "2024-06-03T09:15:00Z"
        }

]

@tickets_bp.route('/', methods=['GET'])

def get_ticket():
    return jsonify(tickets), 200   # lista atual de tickets

@tickets_bp.route('/<int:ticket_id>', methods=['GET'])

def get_ticket_by_id(ticket_id):
    
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            return jsonify(ticket), 200 # retorna o ticket com o id especificado

    return jsonify({"message": "Ticket não encontrado"}), 404 # retorna mensagem de erro caso o ticket não seja encontrado

@tickets_bp.route('/create-ticket', methods=['POST'])

def create_ticket():
    data = request.get_json()
    tickets.append(data)
    return jsonify(data), 201 # adiciona um novo ticket à lista de tickets

@tickets_bp.route('/change-status/<int:ticket_id>', methods=['PATCH'])

def change_ticket_status(ticket_id):
    data = request.get_json()

    for ticket in tickets:
        if ticket['id'] == ticket_id:
                ticket.update(data)
                return jsonify(ticket), 200

    return jsonify({"message": "Status não encontrado"}), 404

@tickets_bp.route('/delete-ticket/<int:ticket_id>', methods=['DELETE'])

def delete_ticket(ticket_id):

    for ticket in tickets:
        if ticket['id'] == ticket_id:
            tickets.remove(ticket)
            return jsonify({"message": "Ticket deletado com sucesso!"}), 200
        
    return jsonify({"message": "Ticket não encontrado!"}), 404


if __name__ == '__main__':
    tickets_bp.run(debug=True)