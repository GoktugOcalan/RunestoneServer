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

#
# when a user registers add them to the user_points table
#
def make_gamify_entry(field_dict,id_of_insert):
    fName = db(db.auth_user.id == id_of_insert).select(db.auth_user.first_name).first()['first_name']
    lName = db(db.auth_user.id == id_of_insert).select(db.auth_user.last_name).first()['last_name']

    db.user_points.update_or_insert(user_id=id_of_insert, first_name=fName, last_name=lName, points=0, all_time_points=0)
    db.unlockables.update_or_insert(user_id=id_of_insert, image=0, if_code=0, for_code=0, while_code=0)
    db.images.update_or_insert(user_id=id_of_insert)
    
def fill_achievements_table():
    db.achievements.truncate()
    db.achievements.update_or_insert(
        achievement_name = "Beginner Programmer",
        achievement_description = "You earned your first point! Starting is half the battle!",
        achievement_threshold = 1,
    )
    db.achievements.update_or_insert(
        achievement_name = "Novice Programmer",
        achievement_description = "You earned 50 points! It's a marathon, not a sprint!",
        achievement_threshold = 50,
    )
    db.achievements.update_or_insert(
        achievement_name = "Promising Programmer",
        achievement_description = "You earned 150 points! Your future is bright!",
        achievement_threshold = 150,
    )
    db.achievements.update_or_insert(
        achievement_name = "Competent Programmer",
        achievement_description = "You earned 500 points! Now you are getting the hang of it!",
        achievement_threshold = 500,
    )
    db.achievements.update_or_insert(
        achievement_name = "Professional Programmer",
        achievement_description = "You earned 1000 points! You have mastered your craft!",
        achievement_threshold = 1500,
    )
    db.achievements.update_or_insert(
        achievement_name = "Veteran Programmer",
        achievement_description = "You earned 3000 points! Your wisdom inspires new generations!",
        achievement_threshold = 3000,
    )
    
fill_achievements_table()

if 'auth_user' in db:
    db.auth_user._after_insert.append(make_gamify_entry)
