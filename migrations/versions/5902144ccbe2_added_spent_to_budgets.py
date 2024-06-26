"""Added spent to Budgets

Revision ID: 5902144ccbe2
Revises: ed064702add1
Create Date: 2024-04-04 11:07:05.409879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5902144ccbe2'
down_revision = 'ed064702add1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('budget_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['budget_id'], ['budgets.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expenses')
    # ### end Alembic commands ###
