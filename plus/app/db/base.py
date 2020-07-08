# Import all the models, so that Base has them before being
# imported by Alembic

# append noqa in the back so our formatter would not clear this line

from app.db.base_class import Base  # noqa
from app.models.college import College  # noqa
