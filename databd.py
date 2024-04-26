from app.models.specialty import Specialty
from app.models.profession import Profession
from database import SessionLocal

# Criação de sessão
db = SessionLocal()

# ...

# Inserção da especialidade "TI"
ti_specialty = Specialty(name='TI')
db.add(ti_specialty)
db.commit()

# ...

# Inserção da especialidade "Marketing"
marketing_specialty = Specialty(name='Marketing')
db.add(marketing_specialty)
db.commit()

# ...

# Inserção da especialidade "Influenciador"
influencer_specialty = Specialty(name='Influenciador')
db.add(influencer_specialty)
db.commit()

# Inserção das profissões associadas a "Influenciador"
influencer_professions = [
    'Modelo',
    'Influenciador',
    'Podcast Host',
    'Produtor'
]
for profession_name in influencer_professions:
    profession = Profession(name=profession_name, specialty=influencer_specialty)
    db.add(profession)

db.commit()  # Fazer commit após adicionar todos os dados

# Este script adiciona a especialidade "Influenciador" ao banco de dados e associa a ela várias profissões relacionadas ao mundo dos influenciadores digitais e criadores de conteúdo.
