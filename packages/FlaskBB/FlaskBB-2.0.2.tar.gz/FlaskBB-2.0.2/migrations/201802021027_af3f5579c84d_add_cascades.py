"""Add cascades

Revision ID: af3f5579c84d
Revises: 7c3fcf8a3335
Create Date: 2018-02-02 10:27:50.290095

"""
import logging

from alembic import op
import sqlalchemy as sa

import flaskbb

logger = logging.getLogger("alembic.runtime.migration")

# revision identifiers, used by Alembic.
revision = 'af3f5579c84d'
down_revision = '7c3fcf8a3335'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    con = op.get_bind()

    if con.engine.dialect.name == "sqlite":
        # its not possible to remove unnamed constraints...
        logger.warning("SQLite is only partially supported for revision {}."
                       .format(revision))

    with op.batch_alter_table('conversations', schema=None) as batch_op:
        if con.engine.dialect.name == "mysql":
            # user_id
            batch_op.drop_constraint("conversations_ibfk_3", type_='foreignkey')
            # to_user_id
            batch_op.drop_constraint("conversations_ibfk_2", type_='foreignkey')
            # from_user_id
            batch_op.drop_constraint("conversations_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('conversations_to_user_id_fkey', type_='foreignkey')
            batch_op.drop_constraint('conversations_from_user_id_fkey', type_='foreignkey')
            batch_op.drop_constraint('conversations_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_conversations_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_conversations_from_user_id_users'), 'users', ['from_user_id'], ['id'], ondelete='SET NULL')
        batch_op.create_foreign_key(batch_op.f('fk_conversations_to_user_id_users'), 'users', ['to_user_id'], ['id'], ondelete='SET NULL')


    with op.batch_alter_table('forumgroups', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_forum_id', type_='foreignkey')
        elif con.engine.dialect.name == "mysql":
            # group_id
            batch_op.drop_constraint("forumgroups_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('forumgroups_group_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_forumgroups_group_id_groups'), 'groups', ['group_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_forumgroups_forum_id_forums'), 'forums', ['forum_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('forums', schema=None) as batch_op:
        if con.engine.dialect.name == "mysql":
            # category_id
            batch_op.drop_constraint("forums_ibfk_1", type_='foreignkey')
            # last_post_user_id
            batch_op.drop_constraint("forums_ibfk_3", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('forums_category_id_fkey', type_='foreignkey')
            batch_op.drop_constraint('forums_last_post_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_forums_category_id_categories'), 'categories', ['category_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_forums_last_post_user_id_users'), 'users', ['last_post_user_id'], ['id'], ondelete='SET NULL')

    with op.batch_alter_table('forumsread', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_fr_forum_id', type_='foreignkey')
        elif con.engine.dialect.name == "mysql":
            # user_id
            batch_op.drop_constraint("forumsread_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('forumsread_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_forumsread_forum_id_forums'), 'forums', ['forum_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_forumsread_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('groups_users', schema=None) as batch_op:
        if con.engine.dialect.name == "mysql":
            # group_id
            batch_op.drop_constraint("groups_users_ibfk_1", type_='foreignkey')
            # user_id
            batch_op.drop_constraint("groups_users_ibfk_2", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('groups_users_group_id_fkey', type_='foreignkey')
            batch_op.drop_constraint('groups_users_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_groups_users_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_groups_users_group_id_groups'), 'groups', ['group_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

        if con.engine.dialect.name == "mysql":
            # conversation_id
            batch_op.drop_constraint("messages_ibfk_1", type_='foreignkey')
            # user_id
            batch_op.drop_constraint("messages_ibfk_2", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('messages_conversation_id_fkey', type_='foreignkey')
            batch_op.drop_constraint('messages_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_messages_conversation_id_conversations'), 'conversations', ['conversation_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_messages_user_id_users'), 'users', ['user_id'], ['id'], ondelete='SET NULL')

    with op.batch_alter_table('moderators', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_forum_id', type_='foreignkey')
        elif con.engine.dialect.name == "mysql":
            # user_id
            batch_op.drop_constraint("moderators_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('moderators_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_moderators_forum_id_forums'), 'forums', ['forum_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_moderators_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('plugin_store', schema=None) as batch_op:
        if con.engine.dialect.name == "mysql":
            # plugin_id
            batch_op.drop_constraint("plugin_store_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('plugin_store_plugin_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_plugin_store_plugin_id_plugin_registry'), 'plugin_registry', ['plugin_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_post_topic_id', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_posts_topic_id_topics'), 'topics', ['topic_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('settings', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_settingsgroup', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_settings_settingsgroup_settingsgroup'), 'settingsgroup', ['settingsgroup'], ['key'], ondelete='CASCADE')

    with op.batch_alter_table('topics', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_topic_forum_id', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_topics_forum_id_forums'), 'forums', ['forum_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('topicsread', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_tr_forum_id', type_='foreignkey')
            batch_op.drop_constraint('fk_tr_topic_id', type_='foreignkey')
        elif con.engine.dialect.name == "mysql":
            # user_id
            batch_op.drop_constraint("topicsread_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('topicsread_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_topicsread_topic_id_topics'), 'topics', ['topic_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_topicsread_forum_id_forums'), 'forums', ['forum_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_topicsread_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('topictracker', schema=None) as batch_op:
        if con.engine.dialect.name == "sqlite":
            batch_op.drop_constraint('fk_tracker_topic_id', type_='foreignkey')
        elif con.engine.dialect.name == "mysql":
            # user_id
            batch_op.drop_constraint("topictracker_ibfk_1", type_='foreignkey')
        elif con.engine.dialect.name == "postgresql":
            batch_op.drop_constraint('topictracker_user_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(batch_op.f('fk_topictracker_topic_id_topics'), 'topics', ['topic_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_topictracker_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topictracker', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_topictracker_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_topictracker_topic_id_topics'), type_='foreignkey')
        batch_op.create_foreign_key('fk_topictracker_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('topicsread', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_topicsread_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_topicsread_forum_id_forums'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_topicsread_topic_id_topics'), type_='foreignkey')
        batch_op.create_foreign_key('fk_topicsread_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_topics_forum_id_forums'), type_='foreignkey')

    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_settings_settingsgroup_settingsgroup'), type_='foreignkey')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_posts_topic_id_topics'), type_='foreignkey')

    with op.batch_alter_table('plugin_store', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_plugin_store_plugin_id_plugin_registry'), type_='foreignkey')
        batch_op.create_foreign_key('fk_plugin_store_plugin_id_plugin_registry', 'plugin_registry', ['plugin_id'], ['id'])

    with op.batch_alter_table('moderators', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_moderators_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_moderators_forum_id_forums'), type_='foreignkey')
        batch_op.create_foreign_key('fk_moderators_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_messages_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_messages_conversation_id_conversations'), type_='foreignkey')

        batch_op.alter_column('user_id', existing_type=flaskbb.utils.database.UTCDateTime(timezone=True), nullable=False)

        batch_op.create_foreign_key('fk_messages_user_id_users', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('fk_messages_conversation_id_conversations', 'conversations', ['conversation_id'], ['id'])

    with op.batch_alter_table('groups_users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_groups_users_group_id_groups'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_groups_users_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_groups_users_user_id_users', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('fk_groups_users_group_id_groups', 'groups', ['group_id'], ['id'])

    with op.batch_alter_table('forumsread', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_forumsread_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_forumsread_forum_id_forums'), type_='foreignkey')
        batch_op.create_foreign_key('fk_forumsread_user_id_users', 'users', ['user_id'], ['id'])

    with op.batch_alter_table('forums', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_forums_last_post_user_id_users'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_forums_category_id_categories'), type_='foreignkey')
        batch_op.create_foreign_key('fk_forums_last_post_user_id_users', 'users', ['last_post_user_id'], ['id'])
        batch_op.create_foreign_key('fk_forums_category_id_categories', 'categories', ['category_id'], ['id'])

    with op.batch_alter_table('forumgroups', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_forumgroups_forum_id_forums'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_forumgroups_group_id_groups'), type_='foreignkey')
        batch_op.create_foreign_key('fk_forumgroups_group_id_groups', 'groups', ['group_id'], ['id'])

    with op.batch_alter_table('conversations', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_conversations_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_conversations_user_id_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
