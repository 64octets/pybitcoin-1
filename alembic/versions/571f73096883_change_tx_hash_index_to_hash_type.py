"""change tx_hash index to hash type

Revision ID: 571f73096883
Revises: 197c134d68e9
Create Date: 2015-11-22 15:45:03.891038

"""

# revision identifiers, used by Alembic.
revision = '571f73096883'
down_revision = '197c134d68e9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_transaction_tx_hash')
    op.create_index('ix_transaction_tx_hash', 'transaction', ['tx_hash'], postgresql_using='hash')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_transaction_tx_hash')
    op.create_index('ix_transaction_tx_hash', 'transaction', ['tx_hash'])
    ### end Alembic commands ###
