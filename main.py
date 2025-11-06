@namespace
class SpriteKind:
    Shoot = SpriteKind.create()
    Mower = SpriteKind.create()
    Grass = SpriteKind.create()
    Mouse = SpriteKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        myTile0
        """))
scene.on_overlap_tile(SpriteKind.Grass,
    assets.tile("""
        myTile18
        """),
    on_overlap_tile)

def on_mouse_move(x, y):
    pass
browserEvents.on_mouse_move(on_mouse_move)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2, assets.tile("""
        myTile
        """))
scene.on_overlap_tile(SpriteKind.Grass,
    assets.tile("""
        myTile15
        """),
    on_overlap_tile2)

mySprite2: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . 1 1 1 1 1 . . . . . . . . . .
        . 1 f f f f 1 . . . . . . . . .
        . 1 f f f f f 1 1 1 . . . . . .
        . 1 f f f f f f f f 1 . . . . .
        . 1 f f f f f f f 1 . . . . . .
        . . 1 f f f f f 1 . . . . . . .
        . . . 1 f f f f f 1 . . . . . .
        . . . 1 f f 1 f f f 1 . . . . .
        . . . 1 f 1 . 1 f f f 1 . . . .
        . . . . 1 . . . 1 f f f 1 . . .
        . . . . . . . . . 1 f 1 . . . .
        . . . . . . . . . . 1 . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.Mouse)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
scene.set_background_color(7)
@namespace
class userconfig:
    ARCADE_SCREEN_WIDTH = 205
    ARCADE_SCREEN_HEIGHT = 144
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile17
    """)):
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.Grass)
    animation.run_image_animation(mySprite2,
        [img("""
                . . . 7 . . 6 . . . . . . . . .
                . . . . . . . . . 6 . 7 . . . .
                . . . . 8 . . 8 . . 8 . . 8 . .
                . . . 8 8 . . . 8 7 . 6 . . . .
                . . . . . . . . 6 . . . . 7 . .
                . . 7 . . 6 . . . . . 8 . . . .
                . . . . . . . . . . . . . . . .
                . e e e e e 6 7 7 7 7 7 7 7 7 .
                c e c c c e e 8 6 6 6 6 6 6 6 6
                c 8 e e e c e 6 7 7 7 7 7 7 7 7
                c 8 e c e c e 8 8 6 6 6 6 6 6 6
                c c 8 e e c e 6 6 7 7 7 7 7 7 7
                c c c c e c e 8 8 8 8 6 6 6 6 6
                . 8 8 8 8 e 6 6 6 6 6 7 7 7 7 .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . 8 . . 6 6 . . 8 . . . .
                . . . . . 7 . . . . . . 8 . . .
                . . 7 . 6 . 7 . . . . 6 . . 7 .
                . . . . 8 . 7 . . 8 . . . . . .
                . . . . 8 . . 6 . . 8 . 7 8 . .
                . . . . . . . . . . . . . . . .
                . e e e e e 8 6 6 6 6 6 6 6 6 .
                8 e e c c e e 6 7 7 7 7 7 7 7 7
                8 c c e e c e 8 6 6 6 6 6 6 6 6
                8 c e c e c e 6 7 7 7 7 7 7 7 7
                8 c c e e c e 8 8 6 6 6 6 6 6 6
                8 8 8 8 c e e 6 6 6 6 7 7 7 7 7
                . c c c c e 8 8 8 8 8 6 6 6 6 .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . 8 . . . . . . . . . . .
                . . 7 . . . . . . 6 . 8 . . . 7
                . . . . . . . . . . 6 . . 6 . .
                . . . 6 6 . 6 . . . . . . . . .
                . . . 6 . . . 6 . . . . . 8 7 .
                . . 7 . . . . . . 6 6 . 8 . . .
                . . . . . 8 . . . . . . . . . .
                . c c c c e 6 7 7 7 7 7 7 7 7 .
                c e e e e c e 8 6 6 6 6 6 6 6 6
                c c c e e c e 6 7 7 7 7 7 7 7 7
                c 8 e c e c e 8 8 6 6 6 6 6 6 6
                c 8 e e e c e 6 6 7 7 7 7 7 7 7
                c c 8 8 c e e 8 8 8 8 6 6 6 6 6
                . c c c c e 6 6 6 6 6 7 7 7 7 .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . 8 . . 8 . 7 . . 6 . . . .
                . . 7 . . 6 . . 6 7 . . . 7 . .
                . . . . 8 . 6 . . . 8 . . . . .
                8 . . . . . . . 8 7 . . 6 . . .
                . . . 6 . . 7 . . . 7 8 . . . .
                . . . . . . . . . . . . . . . .
                . e e e e e 8 6 6 6 6 6 6 6 6 .
                c e c c e e c 6 7 7 7 7 7 7 7 7
                c 8 e e c e c 8 6 6 6 6 6 6 6 6
                c 8 e c e e c 6 7 7 7 7 7 7 7 7
                c 8 e e e e c 8 8 6 6 6 6 6 6 6
                c c 8 8 c c e 6 6 6 6 7 7 7 7 7
                . c c c c e 8 8 8 8 8 6 6 6 6 .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        50,
        True)
    tiles.place_on_tile(mySprite2, value)
    mySprite2.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
    mySprite2.vx = 60
pause(5000)
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile17
    """)):
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.Mower)
    animation.run_image_animation(mySprite2,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . c . . . . . . . . . . . . .
                . c . b . . . . . . . . . . . .
                c . . . b . . . . . . . . . . .
                . b . . . b . . . . . . . . . .
                . . b e 2 2 . c f b c b . . . .
                . . c e 2 2 2 c f c f c . . . .
                . . c e e 2 2 2 2 2 2 2 2 . . .
                . b c e e e e e e e 2 2 2 2 . .
                . b c c c c c e e e e e 2 2 2 2
                . . f f f . . . . . . . . f f f
                . . f 1 f . . . . . . . . f 1 f
                . . f f f . . . . . . . . f f f
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . c . . . . . . . . . . . . .
                . c . b . . . . . . . . . . . .
                c . . . b . . . . . . . . . . .
                . b . . . b . . . . . . . . . .
                . . b e 2 2 . c f b c b . . . .
                . . c e 2 2 2 c f c f c . . . .
                . . c e e 2 2 2 2 2 2 2 2 . . .
                . b c e e e e e e e 2 2 2 2 . .
                . b c c c c c e e e e e 2 2 2 2
                . . f 1 f . . . . . . . . f 1 f
                . . f f f . . . . . . . . f f f
                . . . . . . . . . . . . . . . .
                """)],
        50,
        True)
    tiles.place_on_tile(mySprite2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        myTile3
        """))