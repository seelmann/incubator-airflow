# flake8: noqa
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add task reschedule table

Revision ID: efb1cfe702a3
Revises: 86770d1215c0
Create Date: 2018-06-10 17:45:14.804645

"""

# revision identifiers, used by Alembic.
revision = 'efb1cfe702a3'
down_revision = '86770d1215c0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

TABLE_NAME = 'task_reschedule'

def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('task_id', sa.String(length=250), nullable=False),
        sa.Column('dag_id', sa.String(length=250), nullable=False),
        sa.Column('execution_date', sa.DateTime(), nullable=False),
        sa.Column('start_date', sa.DateTime(), nullable=True),
        sa.Column('end_date', sa.DateTime(), nullable=True),
        sa.Column('duration', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )   


def downgrade():
    op.drop_table(TABLE_NAME)

