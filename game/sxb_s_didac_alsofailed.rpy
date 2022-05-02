    ## SHE ALSO FAILED.
##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################

label afternight04_Didac_AlsoFailed:

if current_girl.roll_success == False:

    #When she also FAILS.

    if current_girl.total_fail == 1:

        $ debug ("Both failed. Once. Slapping her Left Boob. BOTOPOM 009.")

        pt "No parece que le haya gustado,"

        extend " pero tampoco ha reaccionado tan mal..."

    elif current_girl.total_fail == 2:

        pt "Parece que no le ha gustado,"

        extend " pero tengo otra oportunidad..."

    elif current_girl.total_fail == 3:

        pt "Puede que no haya sido la mejor idea,"

        extend " pero por suerte no ha reaccionado de la peor manera..."

        # NOT FINISHED #Add more possible fails?

    elif current_girl.total_fail >= 4:

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            pt "Afortunadamente esta vez no ha intentado follarme..."

        elif randomnum_1to5 == 2:

            pt "Esta vez me he podido salvar de que tome la iniciativa..."

        elif randomnum_1to5 == 3:

            pt "Por suerte aún tengo otra oportunidad sin que se me adelante..."

        elif randomnum_1to5 == 4:

            pt "Es arriesgado volver a intentar lo mismo..."

        elif randomnum_1to5 == 5:

            pt "Por lo menos me ha dejado la polla en paz..."

        else:

            "This message should not appear. BOTOPOM 0010"

    else: 

        "This message should not appear. BOTOPOM 006"

    #if current_girl.repeat == "once":
    #if current_girl.total_try == 1: #Is this really necessary?

        #if current_girl.total_fail == 1:

            #"Both failed. Once. Slapping her Left Boob. Checking Message 02."


else:

    "This message should not appear. BOTOPOM 007"


return