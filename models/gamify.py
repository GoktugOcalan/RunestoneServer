db.define_table('user_points',
  Field('user_id', 'integer'),
  Field('first_name', 'string'),
  Field('last_name', 'string'),
  Field('points','integer'),
  Field('all_time_points','integer'),
  migrate='runestone_user_points.table'
)

db.define_table('achievements',
  Field('achievement_name', 'string'),
  Field('achievement_description', 'string'),
  Field('achievement_threshold', 'integer'),
  migrate='runestone_achievements.table'
)

db.define_table('images',
  Field('user_id', 'integer', writable=False,readable=False),
  Field('image', 'upload'),
  migrate='runestone_images.table'
)

db.define_table('unlockables',
  Field('user_id', 'integer'),
  Field('image','integer'),
  Field('if_code','integer'),
  Field('for_code','integer'),
  Field('while_code','integer'),
  migrate='runestone_unlockables.table'
)
