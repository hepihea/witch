#################################################################################
################################################################################
###############################################################################
###################################################################### SEX_CHECK

label afternight04_sex_check_before:

    ###################################################################### RAPES CONDITIONAL

    ## Does Didac still rapes you?

    ##if afternight04_SheRapingYou == True: # This conditional is active while she rapes you. # NOT FINISHED

    if (afternight04__prehfix_Pussy_dick_out == True or afternight04__prehfix_Pussy_dick_low == True or afternight04__prehfix_Pussy_dick_med == True or afternight04__prehfix_Pussy_dick_deep == True): # DICK OUT

        if mc_body.roll_success == True:

            #$ debug ("She´s not raping you anymore. 8683") # DELETE THIS

            $ afternight04_SheRapingYou = False


    return


