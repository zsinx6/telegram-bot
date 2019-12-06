"""empty message

Revision ID: 637cbd4ef606
Revises: c6896bfe778c
Create Date: 2019-11-13 01:30:54.530497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "637cbd4ef606"
down_revision = "c6896bfe778c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("channels", sa.Column("restrict", sa.Boolean(), nullable=True))
    op.drop_column("channels", "restrict_users")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "channels",
        sa.Column("restrict_users", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.drop_column("channels", "restrict")
    # ### end Alembic commands ###