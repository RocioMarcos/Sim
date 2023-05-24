init python:
    import random
    
    def setupTargets():

        #Cuchillo
        target1_start_x = 1110
        target1_start_y = 298
        target1_down_time = (3.0, 5.0)
        target1_up_time = (3.0, 5.0)

        #Pistola
        target2_start_x = 1565
        target2_start_y = 347
        target2_down_time = (5.0, 8.0)
        target2_up_time = (3.0, 5.0)

        # Hacha
        target3_start_x = 396
        target3_start_y = 286
        target3_down_time = (3.0, 5.0)
        target3_up_time = (1.0, 3.0)

        for i in range(1):

            im1 = Image("images/target-1-6.png")
            target1_sprites.append(target1_SM.create(im1))
            target1_sprites[-1].down_time = random.uniform(target1_down_time[0], target1_down_time[1])
            target1_sprites[-1].up_time = random.uniform(target1_up_time[0], target1_up_time[1])
            target1_sprites[-1].x = target1_start_x 
            target1_sprites[-1].y = target1_start_y


        for i in range(1):

            im2 = Image("images/target-2-5.png")
            target2_sprites.append(target2_SM.create(im2))
            target2_sprites[-1].down_time = random.uniform(target2_down_time[0], target2_down_time[1])
            target2_sprites[-1].up_time = random.uniform(target2_up_time[0], target2_up_time[1])
            target2_sprites[-1].x = target2_start_x
            target2_sprites[-1].y = target2_start_y

            

        for i in range(1):

            im3 = Image("images/target-3-6.png")
            target3_sprites.append(target3_SM.create(im3))
            target3_sprites[-1].down_time = random.uniform(target3_down_time[0], target3_down_time[1])
            target3_sprites[-1].up_time = random.uniform(target3_up_time[0], target3_up_time[1])
            target3_sprites[-1].x = target3_start_x
            target3_sprites[-1].y = target3_start_y


        target1_sprites[-1].idle_animation_direction = "up"
        target1_sprites[-1].current_frame = 9
        target1_sprites[-1].animation_time = 2.0
        target1_sprites[-1].hit = False

        target2_sprites[-1].idle_animation_direction = "up"
        target2_sprites[-1].current_frame = 5
        target2_sprites[-1].animation_time = 2.0
        target2_sprites[-1].hit = False

        target3_sprites[-1].idle_animation_direction = "up"
        target3_sprites[-1].current_frame = 6
        target3_sprites[-1].animation_time = 0.0
        target3_sprites[-1].hit = False


    def target1Update(st):
        for li, target1 in enumerate(target1_sprites):
            if target1.hit == True:
                if target1.current_frame == 1:
                    i = Image("images/target-1-2.png")
                    target1.current_frame = 2
                    target1.set_child(i)

                elif target1.current_frame == 2 and target1.animation_time >= 0.15:
                    i = Image("images/target-1-3.png")
                    target1.current_frame = 3
                    target1.set_child(i)

                elif target1.current_frame == 3 and target1.animation_time >= 0.3:
                    i = Image("images/target-1-4.png")
                    target1.current_frame = 4
                    target1.set_child(i)

                elif target1.current_frame == 4 and target1.animation_time >= 0.45:
                    i = Image("images/target-1-5.png")
                    target1.current_frame = 5
                    target1.set_child(i)

                elif target1.current_frame == 5 and target1.animation_time >= 0.6:
                    i = Image("images/target-1-6.png")
                    target1.current_frame = 6
                    target1.set_child(i)

                elif target1.current_frame == 6 and target1.animation_time >= 0.75:
                    i = Image("images/target-1-7.png")
                    target1.current_frame = 7
                    target1.set_child(i)

                elif target1.current_frame == 7 and target1.animation_time >= 0.9:
                    i = Image("images/target-1-8.png")
                    target1.current_frame = 8
                    target1.set_child(i)

                elif target1.current_frame == 8 and target1.animation_time >= 1.05:
                    i = Image("images/target-1-9.png")
                    target1.current_frame = 9
                    target1.animation_time = 0
                    target1.hit = False
                    target1.set_child(i)
            
            else:
                if target1.idle_animation_direction == "up":
                    if target1.animation_time >= target1.down_time:
                        if target1.current_frame == 9:
                            i = Image("images/target-1-9.png")
                            target1.current_frame = 8
                            target1.set_child(i)

                        elif target1.current_frame == 8 and target1.animation_time >= target1.down_time + 0.1:
                            i = Image("images/target-1-8.png")
                            target1.current_frame = 7
                            target1.set_child(i)

                        elif target1.current_frame == 7 and target1.animation_time >= target1.down_time + 0.2:
                            i = Image("images/target-1-7.png")
                            target1.current_frame = 6
                            target1.set_child(i)

                        elif target1.current_frame == 6 and target1.animation_time >= target1.down_time + 0.3:
                            i = Image("images/target-1-6.png")
                            target1.current_frame = 5
                            target1.set_child(i)

                        elif target1.current_frame == 5 and target1.animation_time >= target1.down_time + 0.4:
                            i = Image("images/target-1-5.png")
                            target1.current_frame = 4
                            target1.set_child(i)

                        elif target1.current_frame == 4 and target1.animation_time >= target1.down_time + 0.5:
                            i = Image("images/target-1-4.png")
                            target1.current_frame = 3
                            target1.set_child(i)

                        elif target1.current_frame == 3 and target1.animation_time >= target1.down_time + 0.6:
                            i = Image("images/target-1-3.png")
                            target1.current_frame = 2
                            target1.set_child(i)

                        elif target1.current_frame == 2 and target1.animation_time >= target1.down_time + 0.7:
                            i = Image("images/target-1-2.png")
                            target1.current_frame = 1
                            target1.idle_animation_direction = "down"
                            target1.animation_time = 0
                            target1.set_child(i)

                elif target1.idle_animation_direction == "down":
                    if target1.animation_time >= target1.down_time:
                        if target1.current_frame == 1:
                            i = Image("images/target-1-2.png")
                            target1.current_frame = 2
                            target1.set_child(i)

                        elif target1.current_frame == 2 and target1.animation_time >= target1.up_time + 0.1:
                            i = Image("images/target-1-3.png")
                            target1.current_frame = 3
                            target1.set_child(i)

                        elif target1.current_frame == 3 and target1.animation_time >= target1.up_time + 0.2:
                            i = Image("images/target-1-4.png")
                            target1.current_frame = 4
                            target1.set_child(i)

                        elif target1.current_frame == 4 and target1.animation_time >= target1.up_time + 0.3:
                            i = Image("images/target-1-5.png")
                            target1.current_frame = 5
                            target1.set_child(i)

                        elif target1.current_frame == 5 and target1.animation_time >= target1.up_time + 0.4:
                            i = Image("images/target-1-6.png")
                            target1.current_frame = 6
                            target1.set_child(i)

                        elif target1.current_frame == 6 and target1.animation_time >= target1.up_time + 0.5:
                            i = Image("images/target-1-7.png")
                            target1.current_frame = 7
                            target1.set_child(i)

                        elif target1.current_frame == 7 and target1.animation_time >= target1.up_time + 0.6:
                            i = Image("images/target-1-8.png")
                            target1.current_frame = 8
                            target1.set_child(i)

                        elif target1.current_frame == 8 and target1.animation_time >= target1.up_time + 1.7:
                            i = Image("images/target-1-9.png")
                            target1.current_frame = 9
                            target1.idle_animation_direction = "up"
                            target1.animation_time = 0
                            target1.hit = False
                            target1.set_child(i)

            target1.animation_time += 0.01
        return 0


    def target2Update(st):
        for li, target2 in enumerate(target2_sprites):
            if target2.hit == True:
                if target2.current_frame == 1:
                    i = Image("images/target-2-2.png")
                    target2.animation_time = 0
                    target2.current_frame = 2
                    target2.set_child(i)

                elif target2.current_frame == 2:
                    i = Image("images/target-2-3.png")
                    target2.current_frame = 3
                    target2.set_child(i)

                elif target2.current_frame == 3 and target2.animation_time >= 0.1:
                    i = Image("images/target-2-4.png")
                    target2.current_frame = 4
                    target2.set_child(i)

                elif target2.current_frame == 4 and target2.animation_time >= 0.12:
                    i = Image("images/target-2-5.png")
                    target2.current_frame = 5
                    target2.set_child(i)

                elif target2.current_frame == 5 and target2.animation_time >= 0.13:
                    i = Image("images/target-2-5.png")
                    target2.current_frame = 5
                    target2.animation_time = 0
                    target2.hit = False
                    target2.set_child(i)
            
            else:
                if target2.idle_animation_direction == "up":
                    if target2.animation_time >= target2.down_time:
                        if target2.current_frame == 6:
                            i = Image("images/target-2-5.png")
                            target2.current_frame = 3
                            target2.set_child(i)

                        elif target2.current_frame == 5 and target2.animation_time >= target2.down_time + 0.1:
                            i = Image("images/target-2-5.png")
                            target2.current_frame = 2
                            target2.set_child(i)

                        elif target2.current_frame == 4 and target2.animation_time >= target2.down_time + 0.1:
                            i = Image("images/target-2-4.png")
                            target2.current_frame = 2
                            target2.set_child(i)

                        elif target2.current_frame == 3 and target2.animation_time >= target2.down_time + 0.1:
                            i = Image("images/target-2-3.png")
                            target2.current_frame = 2
                            target2.set_child(i)

                        elif target2.current_frame == 2 and target2.animation_time >= target2.down_time + 0.12:
                            i = Image("images/target-2-2.png")
                            target2.current_frame = 1
                            target2.idle_animation_direction = "down"
                            target2.animation_time = 0
                            target2.set_child(i)

                elif target2.idle_animation_direction == "down":
                    if target2.animation_time >= target2.down_time:
                        if target2.current_frame == 1:
                            i = Image("images/target-2-2.png")
                            target2.current_frame = 2
                            target2.set_child(i)

                        elif target2.current_frame == 2:
                            i = Image("images/target-2-3.png")
                            target2.current_frame = 3
                            target2.set_child(i)

                        elif target2.current_frame == 3:
                            i = Image("images/target-2-4.png")
                            target2.current_frame = 4
                            target2.set_child(i)

                        elif target2.current_frame == 4:
                            i = Image("images/target-2-5.png")
                            target2.current_frame = 5
                            target2.idle_animation_direction = "up"
                            target2.animation_time = 0
                            target2.hit = False
                            target2.set_child(i)

            target2.animation_time += 0.01
        return 0


    def target3Update(st):
        for li, target3 in enumerate(target3_sprites):
            if target3.hit == True:
                if target3.current_frame == 1:
                    i = Image("images/target-3-2.png")
                    target3.animation_time = 0
                    target3.current_frame = 2
                    target3.set_child(i)

                elif target3.current_frame == 2:
                    i = Image("images/target-3-3.png")
                    target3.current_frame = 3
                    target3.set_child(i)

                elif target3.current_frame == 3 and target3.animation_time >= 0.1:
                    i = Image("images/target-3-4.png")
                    target3.current_frame = 4
                    target3.set_child(i)

                elif target3.current_frame == 4 and target3.animation_time >= 0.12:
                    i = Image("images/target-3-5.png")
                    target3.current_frame = 5
                    target3.set_child(i)

                elif target3.current_frame == 5 and target3.animation_time >= 0.13:
                    i = Image("images/target-3-6.png")
                    target3.current_frame = 5
                    target3.animation_time = 0
                    target3.hit = False
                    target3.set_child(i)
            
            else:
                if target3.idle_animation_direction == "up":
                    if target3.animation_time >= target3.down_time:
                        if target3.current_frame == 6:
                            i = Image("images/target-3-6.png")
                            target3.current_frame = 3
                            target3.set_child(i)

                        elif target3.current_frame == 5 and target3.animation_time >= target3.down_time + 0.1:
                            i = Image("images/target-3-5.png")
                            target3.current_frame = 2
                            target3.set_child(i)

                        elif target3.current_frame == 4 and target3.animation_time >= target3.down_time + 0.1:
                            i = Image("images/target-3-4.png")
                            target3.current_frame = 2
                            target3.set_child(i)

                        elif target3.current_frame == 3 and target3.animation_time >= target3.down_time + 0.1:
                            i = Image("images/target-3-3.png")
                            target3.current_frame = 2
                            target3.set_child(i)

                        elif target3.current_frame == 2 and target3.animation_time >= target3.down_time + 0.12:
                            i = Image("images/target-3-2.png")
                            target3.current_frame = 1
                            target3.idle_animation_direction = "down"
                            target3.animation_time = 0
                            target3.set_child(i)

                elif target3.idle_animation_direction == "down":
                    if target3.animation_time >= target3.down_time:
                        if target3.current_frame == 1:
                            i = Image("images/target-3-2.png")
                            target3.current_frame = 2
                            target3.set_child(i)

                        elif target3.current_frame == 2:
                            i = Image("images/target-3-3.png")
                            target3.current_frame = 3
                            target3.set_child(i)

                        elif target3.current_frame == 3:
                            i = Image("images/target-3-4.png")
                            target3.current_frame = 4
                            target3.set_child(i)

                        elif target3.current_frame == 4:
                            i = Image("images/target-3-5.png")
                            target3.current_frame = 5
                            target3.set_child(i)

                        elif target3.current_frame == 5:
                            i = Image("images/target-3-6.png")
                            target3.current_frame = 5
                            target3.idle_animation_direction = "up"
                            target3.animation_time = 0
                            target3.hit = False
                            target3.set_child(i)

            target3.animation_time += 0.01


        return 0

    def bulletEvents(event, x, y, st):
        mousepos = renpy.get_mouse_pos()
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1 and y < config.screen_height - 140:
                bullet_sprites.append(bullet_SM.create(bullet_image))
                bullet_sprites[-1].original_size = (20, 43)
                bullet_sprites[-1].x = mousepos[0]
                bullet_sprites[-1].y = mousepos[1]
                bullet_sprites[-1].original_pos = (bullet_sprites[-1].x, bullet_sprites[-1].y)
                bullet_sprites[-1].zoom = 0.5
                bullet_sprites[-1].move_to_pos = (x, y)
                bullet_SM.redraw(0)

    def bulletUpdate(st):
        global score
        for bullet in bullet_sprites:
            if bullet.y > bullet.move_to_pos[1]:
                bullet.y -= abs(bullet.move_to_pos[1] - bullet.original_pos[1]) / 15
                t = Transform(child = bullet_image)
                bullet.zoom -= 0.05
                bullet.x += 1.2
                bullet.original_size = (bullet.original_size[0] * bullet.zoom, bullet.original_size[1] * bullet.zoom)
                t.zoom = bullet.zoom
                t.update()
                bullet.set_child(t)
            else:
                for i, target1 in enumerate(target1_sprites):
                    if target1.current_frame == 1 and target1.x <= (bullet.x - bullet.original_size[0] / 2) <= (target1.x + target1_sizes[0]) and target1.y <= (bullet.y - bullet.original_size[1]/2) <= (target1.y + target1_sizes[1]):
                        target1.hit = True
                        score += 5
                        target1_SM.redraw(0)
                        bullet.destroy()
                        bullet_sprites.remove(bullet)
                        renpy.restart_interaction()
                        break

                    elif i == len(target1_sprites) - 1:
                        bullet.destroy()


                for i, target2 in enumerate(target2_sprites):
                    if target2.current_frame == 1 and target2.x <= (bullet.x - bullet.original_size[0] / 2) <= (target2.x + target2_sizes[0]) and target2.y <= (bullet.y - bullet.original_size[1]/2) <= (target2.y + target2_sizes[1]):
                        target2.hit = True
                        score += 5
                        target2_SM.redraw(0)
                        bullet.destroy()
                        bullet_sprites.remove(bullet)
                        renpy.restart_interaction()
                        break

                    elif i == len(target2_sprites) - 1:
                        bullet.destroy()


                for i, target3 in enumerate(target3_sprites):
                    if target3.current_frame == 1 and target3.x <= (bullet.x - bullet.original_size[0] / 2) <= (target3.x + target3_sizes[0]) and target3.y <= (bullet.y - bullet.original_size[1]/2) <= (target3.y + target3_sizes[1]):
                        target3.hit = True
                        score += 5
                        target3_SM.redraw(0)
                        bullet.destroy()
                        bullet_sprites.remove(bullet)
                        renpy.restart_interaction()
                        break

                    elif i == len(target3_sprites) - 1:
                        bullet.destroy()

        return 0


    def prepareShootingGallery():
        global countdown_time
        global score

        countdown_time = initial_countdown_time
        score = 0

        for target1 in target1_sprites:
            target1.hit = False
            target1.idle_animation_direction = "up"
            target1.animation_time = 0.0
            target1.current_frame = 6
            i = Image("images/target-1-9.png")
            target1.set_child(i)

        for target2 in target2_sprites:
            target2.hit = False
            target2.idle_animation_direction = "up"
            target2.animation_time = 0.0
            target2.current_frame = 5
            i = Image("images/target-2-5.png")
            target2.set_child(i)

        for target3 in target3_sprites:
            target3.hit = False
            target3.idle_animation_direction = "up"
            target3.animation_time = 0.0
            target3.current_frame = 6
            i = Image("images/target-3-6.png")
            target3.set_child(i)


screen shooting_gallery:
    on "show" action [Function(prepareShootingGallery), SetVariable("default_mouse", "targetgame"), SetVariable("shooting_gallery", True)]
    image "images/shooting-gallery-background.png"
    add target1_SM
    add target2_SM
    add target3_SM
    add bullet_SM
    image "images/score-background.png" pos (660, 950)
    text "Tiempo: {:.0f}        Puntaje: [score]".format(countdown_time) color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 32 align (0.5, 0.95)
    #text "Tiempo: {:.0f}".format(countdown_time) color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 28 pos (1025, 990) anchor(0.0, 0.0)
    timer 1.0 action If(countdown_time > 0, true = SetVariable("countdown_time", countdown_time - 1.0), false = Show("shooting_end")) repeat If(countdown_time > 0, true = True, false = False)


screen shooting_end:
    modal True
    frame:
        xfill True
        yalign 0.5
        background "#000000bc"
        padding (540, 540)
        text "¡Terminó el tiempo!" color "#ffffff" align(0.5, 2.0) size 60
        text "Tu puntaje es de [score] puntos" color "#ffffff" align(0.5, 0.75) size 50

        imagebutton auto "images/button-restart-%s.png" align(0.5, -0.75) action [Hide("shooting_gallery"), Function(prepareShootingGallery), Show("shooting_gallery")]
        #imagebutton auto "images/button-exit-%s.png" align(0.55, 0.7) action[Hide("shooting_gallery"), Function(prepareShootingGallery), SetVariable("default_mouse", None), SetVariable("shooter_gallery", False)]
    timer 2.0 action [Function(prepareShootingGallery)]



# Configs 

define config.mouse = {}
define config.mouse["targetgame"] = [("images/target-pointer.png", 17, 10)]

define config.font_name_map["bold"] = "NotoSans-ExtraBold.ttf"

# Start

label start:


    # Target variables
    $target1_SM = SpriteManager(update = target1Update)
    $target1_sizes = (289, 406)
    $target1_sprites = []

    $target2_SM = SpriteManager(update = target2Update)
    $target2_sizes = (319, 241)
    $target2_sprites = []

    $target3_SM = SpriteManager(update = target3Update)
    $target3_sizes = (134, 327)
    $target3_sprites = []

    $setupTargets()

    # Bullet variables
    $bullet_image = Image("images/bullet.png")
    $bullet_sprites = []
    $bullet_SM = SpriteManager(update = bulletUpdate, event = bulletEvents)

    # Other variables
    $score = 0
    $initial_countdown_time = 60.0
    $countdown_time = initial_countdown_time
    $shooting_gallery = False

    call screen shooting_gallery
    
    return