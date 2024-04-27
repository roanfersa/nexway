# app/routes/api.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from models.user import User
from models.token_blacklist import TokenBlacklist
from datetime import datetime, timedelta
from database import SessionLocal
from sqlalchemy.orm import Session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

# Crie um blueprint para as rotas de autenticação
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# Registro de usuários
@auth_blueprint.route('/register', methods=['POST'])
def register():
    # Obtenha os dados do request
    data = request.get_json()
    
    # Valide os dados aqui (exemplo simples, você pode querer fazer uma validação mais robusta)
    if 'email' not in data or 'password' not in data:
        return jsonify({"message": "Email and password are required."}), 400
    
    # Crie a hash da senha
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    # Crie uma sessão com o banco de dados
    db = SessionLocal()
    try:
        # Crie um novo usuário
        new_user = User(email=data['email'], password=hashed_password)
        db.add(new_user)
        db.commit()
        
        # Retorne uma resposta de sucesso
        return jsonify({"message": "User successfully registered."}), 201
    except IntegrityError:
        # Se o e-mail já existir, retorne um erro
        db.rollback()
        return jsonify({"message": "Email already registered."}), 400
    finally:
        db.close()
    pass

# Login de usuários
@auth_blueprint.route('/login', methods=['POST'])
def login():
   def login():
    # Obtenha os dados da requisição
    data = request.get_json()

    # Validação simples dos dados
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Email and password are required."}), 400

    # Crie uma sessão com o banco de dados
    db = SessionLocal()
    try:
        # Tente encontrar o usuário pelo e-mail
        user = db.query(User).filter_by(email=data['email']).first()
        if user and check_password_hash(user.hashed_password, data['password']):
            # Se a senha estiver correta, gere um token JWT
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            # Usuário não encontrado ou senha incorreta
            return jsonify({"message": "Invalid credentials."}), 401
    except Exception as e:
        # Em caso de qualquer outro erro
        return jsonify({"message": "Something went wrong.", "error": str(e)}), 500
    finally:
        db.close()
    pass

# Obter perfil do usuário
@auth_blueprint.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    db: Session = SessionLocal()
    
    try:
        # Aqui você precisa garantir que o modelo User tem uma relação com o modelo Profile
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            # Transforma os dados do perfil do usuário em um dicionário, ajuste conforme seu modelo de perfil
            profile_data = {
                "user_id": user.id,
                "complete_name": user.complete_name,
                "profile_id": user.profile.id if user.profile else None,
                "email": user.email,
                "profession": user.profile.profession.name if user.profile.profession else None,
                "specialty": user.profile.specialty.name if user.profile.specialty else None,
                "company_level": user.profile.company_level if user.profile.company_level else None,
                "product_type": user.profile.product_type.description if user.profile.product_type else None,
                "meeting_preference": user.profile.meeting_preference.description if user.profile.meeting_preference else None,
                "experience": user.profile.experience.description if user.profile.experience else None,
                "networking_goals": [goal.description for goal in user.profile.networking_goals] if user.profile.networking_goals else []
                # Adicione mais campos conforme necessário
            }
            return jsonify(profile_data), 200
        else:
            # Usuário não encontrado
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        # Em caso de erro
        return jsonify({"error": str(e)}), 500
    finally:
        # Sempre feche a sessão do banco de dados
        db.close()
    pass

# Logout de usuários
@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    db = SessionLocal()
    try:
        # Obtenha o token JWT atual
        jti = get_jwt()['jti']
        
        # Crie uma instância de TokenBlacklist com a identificação do token (jti)
        db.add(TokenBlacklist(jti=jti, created_at=datetime.now()))
        
        db.commit()
        return jsonify({"message": "User successfully logged out."}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"message": "Something went wrong.", "error": str(e)}), 500
    finally:
        db.close()
    pass

# Atualização de informações do usuário
@auth_blueprint.route('/user', methods=['PUT'])
@jwt_required()
def update_user():
    # Obtenha o ID do usuário do token JWT
    user_id = get_jwt_identity()
    # Obtenha os dados do corpo da requisição
    data = request.get_json()

    # Inicie uma sessão com o banco de dados
    db: Session = SessionLocal()

    try:
        # Tente encontrar o usuário pelo ID
        user = db.query(User).filter_by(id=user_id).first()

        if user:
            # Atualize os campos do usuário com os dados recebidos
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            # ... Faça o mesmo para outros campos que você deseja atualizar

            # Confirme as alterações
            db.commit()

            return jsonify({"message": "User successfully updated."}), 200
        else:
            # Usuário não encontrado
            return jsonify({"message": "User not found."}), 404
    except Exception as e:
        # Em caso de qualquer outro erro
        db.rollback()
        return jsonify({"message": "Something went wrong.", "error": str(e)}), 500
    finally:
        # Feche a sessão do banco de dados
        db.close()
    pass

# Excluir um usuário
@auth_blueprint.route('/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()  # Assumindo que o ID do usuário está no token JWT
    db: Session = SessionLocal()
    try:
        # Buscar usuário pelo ID
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return jsonify({"message": "User successfully deleted."}), 200
        else:
            return jsonify({"message": "User not found."}), 404
    except Exception as e:
        db.rollback()
        return jsonify({"message": "Something went wrong.", "error": str(e)}), 500
    finally:
        db.close()
    pass

# Não se esquecer de registrar o blueprint no seu app
# app.register_blueprint(auth_blueprint)
