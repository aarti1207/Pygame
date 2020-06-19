import cx_Freeze

executables = [cx_Freeze.Executable("SpaceInvader.py")]

cx_Freeze.setup(
    name="SpaceInvaders",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["background.png","background.wav","bullet.png","Chasy.otf","CHICKEN Pie.ttf","enemy.png","explosion.wav","laser.wav","player.png","spaceship.png"]}},
    executables = executables

    )
