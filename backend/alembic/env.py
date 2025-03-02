import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, create_engine, pool
from alembic import context

# Adiciona o diretório do projeto ao sys.path (corrige possíveis erros de importação)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Carregar a configuração do Alembic
config = context.config

# Configuração de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importar os modelos para que o Alembic possa detectá-los
from app.models.base import Base
import app.models.user  # Importar modelos individuais
import app.models.chef  # Se houver um modelo 'chef', inclua ele também

# Definir a metadata para autogenerate
target_metadata = Base.metadata  

# Obter a URL do banco de dados a partir da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Se DATABASE_URL não estiver definida, definir um valor padrão
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:123456@localhost:5432/chefcasa"

config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
    """Executa as migrações no modo offline (sem conexão com o banco)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações no modo online (com conexão ao banco)."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
