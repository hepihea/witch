

label day06_night_homeWithoutDidac_phonePolice:

    show morning04_livingroom_mc_resting_handphone

    if p_ao_started:
        show morning04_bg_livingroom_mc_resting_phone home_tuesday

    else:
        show morning04_bg_livingroom_mc_resting_phone home_monday
    with dissolve

    n "Te dispones a marcar al número de emergencias {a=https://es.wikipedia.org/wiki/112_(teléfono)}112{/a}."

    call WIP

    # NOT FINISHED

    jump gameover