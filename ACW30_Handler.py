#=============== Handle keywords for Avaya Communicator 3.0 for Windows ===============#
def ACW30_Handler(sData):
    #--- Split received string to array ---#
    sData += ";"    # Make the last element is null (For functions which have optional parameters
    sData = sData.split(";")
    resultString = ""
    #--- Execute functions ---#
    if sData[0]=="ACW30_LaunchApp":
        if ACW30_LaunchApp()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_MakeAudioCall":
        if ACW30_MakeAudioCall(sData[1])==True:  
            resultString =  "Pass"
    elif sData[0]=="ACW30_MakeVideoCall":
        if ACW30_MakeVideoCall(sData[1])==True:           
            resultString =  "Pass"
    elif sData[0]=="ACW30_AnswerAudioCall":
        if ACW30_AnswerAudioCall(sData[1])==True:            
            resultString =  "Pass"
    elif sData[0]=="ACW30_AnswerVideoCall":
        if ACW30_AnswerVideoCall(sData[1])==True:            
            resultString =  "Pass"
    elif sData[0]=="ACW30_MuteSelf":
        if ACW30_MuteSelf()==True:            
            resultString =  "Pass"
    elif sData[0]=="ACW30_UnmuteSelf":
        if ACW30_UnmuteSelf()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_PutOnHold":
        if ACW30_PutOnHold()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_UnHold":
        if ACW30_UnHold(sData[1])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_PauseVideo":
        if ACW30_PauseVideo()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_UnpauseVideo":
        if ACW30_UnpauseVideo()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_DeescalateToAudioCall":
        if ACW30_DeescalateToAudioCall()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_EscalateToVideoCall":
        if ACW30_EscalateToVideoCall()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_EndCall":
        if ACW30_EndCall(sData[1])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_IgnoreCall":
        if ACW30_IgnoreCall()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_LoginVOIP":
        if ACW30_LoginVOIP(sData[1],sData[2],sData[3])==True:            
            resultString =  "Pass"
    elif sData[0]=="ACW30_LoginVOIPWithServerInfo":
        if ACW30_LoginVOIPWithServerInfo(sData[1],sData[2],sData[3],sData[4],sData[5])==True:
            resultString =  "Pass"
    elif sData[0] == "ACW30_MakeAudioMeetme":
        if ACW30_MakeAudioMeetme(sData[1],sData[2])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_MeetmeDialOut":
        if ACW30_MeetmeDialOut(sData[1])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_Logout":
        if ACW30_Logout()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_CleanUp":
        if ACW30_CleanUp()==True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_KillApp":
        if ACW30_KillApp()==True:
            resultString =  "Pass"    
    elif sData[0]=="ACW30_ActiveApp":
        if ACW30_ActiveApp()==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_MoveWindow":
        if ACW30_MoveWindow(sData[1])==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_LaunchAppProcess":
        if ACW30_LaunchAppProcess()==True:
            resultString =  "Pass"    
    elif sData[0]=="ACW30_InviteByDTMF":
        if ACW30_MeetmeDialOut(sData[1])==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_MakeVideoMeetme":
        if ACW30_MakeVideoMeetme(sData[1],sData[2])==True:
            resultString =  "Pass"          
    elif sData[0]=="ACW30_JoinAACMeetmeConference":
        if ACW30_JoinAACMeetmeConference(sData[1],sData[2],sData[3])==True:
            resultString =  "Pass"        
    elif sData[0]=="ACW30_RecoverLoggedIn":
        if ACW30_RecoverLoggedIn()==True:
            resultString =  "Pass"    
    elif sData[0]=="ACW30_VerifyIdle":
        if ACW30_VerifyIdle()==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_VerifyHeldCall":
        if ACW30_VerifyHeldCall(sData[1])==True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_VerifyCallType":
        if ACW30_VerifyCallType(sData[1])==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_DeclineCall":
        if ACW30_DeclineCall(sData[1])==True:            
            resultString =  "Pass"      
    elif sData[0]=="ACW30_PickupCall":
        if ACW30_PickupCall(sData[1], sData[2])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureAudio":
        if ACW30_ConfigureAudio()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_TransferCall":
        if ACW30_TransferAndMergeCall("TransferCall", sData[1], sData[2])==True:
            resultString =  "Pass"    
    elif sData[0]=="ACW30_MergeCall":
        if ACW30_TransferAndMergeCall("MergeCall", sData[1], sData[2])==True:
            resultString =  "Pass"    
    elif sData[0]=="ACW30_TurnOnLectureMode":
        if ACW30_LectureMode("TurnOn")==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_TurnOffLectureMode":
        if ACW30_LectureMode("TurnOff")==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_MuteAllConference":
        if ACW30_MuteAndUnmuteAllConference("Mute")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_UnmuteAllConference":
        if ACW30_MuteAndUnmuteAllConference("Unmute")==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_DropParticipant":
        if ACW30_DropParticipant(sData[1])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_PromoteModerator":
        if ACW30_PromoteModerator(sData[1])==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_TurnOnLockConf":
        if ACW30_LockConf("TurnOn")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_TurnOffLockConf":
        if ACW30_LockConf("TurnOff")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_SortParticipant":
        if ACW30_SortParticipant(sData[1])==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_InputDTMFInConference":
        if ACW30_InputDTMFInConference(sData[1])==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_MuteParticipant":
        if ACW30_MuteUnmuteParticipant(sData[1],sData[2],"mute")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_UnmuteParticipant":
        if ACW30_MuteUnmuteParticipant(sData[1],sData[2],"unmute")==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_DropConference":
        if ACW30_DropConference()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_InviteByDialpad":
        if ACW30_InviteByDialpad(sData[1])==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_IgnoreCrashLog":
        if ACW30_IgnoreCrashLog()==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_BlindTransfer":
        if ACW30_BlindTransfer(sData[1],sData[2])==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_ViewVideoCallStatistics":
        if ACW30_ViewVideoCallStatistics()==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_ViewAudioCallStatistics":
        if ACW30_ViewAudioCallStatistics()==True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_BlockVideoCamera":
        if ACW30_BlockAndUnblockVideoCamera("block")==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_UnblockVideoCamera":
        if ACW30_BlockAndUnblockVideoCamera("unblock")==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_PutAppToBackground":
        if ACW30_PutAppToBackground()==True:
            resultString =  "Pass"
    elif sData[0]=="ACW30_PutAppToForeground":
        if ACW30_ActiveApp()==True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_ConfigureVideo":
        if ACW30_ConfigureVideo(sData[1])==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_EnableRecordingInConference":
        if ACW30_RecordingInConference("enable")==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_DisableRecordingInConference":
        if ACW30_RecordingInConference("disable")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_DismissAllPopups":
        if ACW30_DismissAllPopups()==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_EndAllCalls":
        if ACW30_EndAllCalls()==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_CopyLogFile":
        if ACW30_CopyLogFile()==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_VerifyIncomingCall":
        if ACW30_VerifyIncomingCall(sData[1],sData[2])==True:
            resultString =  "Pass"       
    elif sData[0]=="ACW30_AutoConfiguration":
        if ACW30_AutoConfiguration(sData[1], sData[2], sData[3], sData[4], sData[5]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureAdhocURI":
        if ACW30_ConfigureAdhocURI(sData[1]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_CreateAACAdhocConferenceByDialpad":
        if ACW30_CreateAACAdhocConferenceByDialpad(sData[1]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_ConfigureCallForwardAllCalls":
        if ACW30_ConfigureIncomingCallsFeatures("CallForwardAllCalls", sData[1],sData[2]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_ConfigureCallForwardBusy":
        if ACW30_ConfigureIncomingCallsFeatures("CallForwardBusy", sData[1],sData[2]):
            resultString =  "Pass"   
    elif sData[0]=="ACW30_ConfigureSendAllCalls":
        if ACW30_ConfigureIncomingCallsFeatures("SendAllCalls", sData[1],sData[2]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_VerifyConferenceType":
        if ACW30_VerifyConferenceType(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_TurnOnContinuation":
        if ACW30_Continuation("on"):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_TurnOffContinuation":
        if ACW30_Continuation("off"):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_ConfigureExclusion":
        if ACW30_ConfigureExclusion(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureLDAP":
        if ACW30_ConfigureLDAP(sData[1],sData[2],sData[3],sData[4],sData[5],sData[6]):
            resultString =  "Pass"   
    elif sData[0]=="ACW30_ConfigureAMM":
        if ACW30_ConfigureAMM(sData[1],sData[2],sData[3],sData[4], sData[5]):
            resultString =  "Pass"            
    elif sData[0]=="ACW30_LeaveConversation":
        if ACW30_LeaveConversation():
            resultString =  "Pass"   
    elif sData[0]=="ACW30_SendSimpleMessage":
        if ACW30_SendSimpleMessage(sData[1]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_InitiateCallFromFirstCalllog":
        if ACW30_InitiateCallFromFirstCalllog(sData[1]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_CallFromSearchedContact":
        if ACW30_CallFromSearchedContact(sData[1],sData[2],sData[3],sData[4]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_MakeCallFromLDAPContact":
        if ACW30_CallFromSearchedContact(sData[1],"LDAP","Work", "Audio"):
            resultString =  "Pass"
            if ACW30_CallFromSearchedContact(sData[1],"communicator","Handle", "Audio"):
                resultString =  "Pass"
    elif sData[0]=="ACW30_AddContactFromLDAP":
        if ACW30_AddContactFromLDAP(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_SearchForContact":
        if ACW30_SearchForContact(sData[1], sData[2]):
            resultString =  "Pass"     
    elif sData[0]=="ACW30_ChooseContact":
        if ACW30_ChooseContact(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_DeleteContact":
        if ACW30_DeleteContact(sData[1]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_AddContactFromCallLog":
        if ACW30_AddContactFromCallLog(sData[1], sData[2], sData[3]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_Share":
        if ACW30_Share(sData[1]):
            resultString =  "Pass"     
    elif sData[0]=="ACW30_EndSharing":
        if ACW30_EndSharing():
            resultString =  "Pass" 
    elif sData[0]=="ACW30_StopSharing":
        if ACW30_StopSharing():
            resultString =  "Pass"  
    elif sData[0]=="ACW30_PauseSharing":
        if ACW30_PauseSharing():
            resultString =  "Pass" 
    elif sData[0]=="ACW30_ResumeSharing":
        if ACW30_ResumeSharing():
            resultString =  "Pass"  
    elif sData[0]=="ACW30_Redial":
        if ACW30_Redial(sData[1]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_AddContactsToStagingArea":
        if ACW30_AddContactsToStagingArea(sData[1]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_GoToService":
        if ACW30_GoToService()==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_ClearHistory":
        if ACW30_ClearHistory()==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_PromotePresenter":
        if ACW30_PromotePresenter(sData[1]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_VerifySharing":
        if ACW30_VerifySharing(sData[1]):
            resultString =  "Pass"   
    elif sData[0]=="ACW30_VerifyRoleInConference":
        if ACW30_VerifyRoleInConference(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyExistingImage":
        if VerifyExistingImage(sData[1], sData[2])==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_ChangePresenceState":
        if ACW30_ChangePresenceState(sData[1]):
            resultString =  "Pass"    
    elif sData[0]=="ACW30_CreateNewContact":
        if ACW30_CreateNewContact(sData[1], sData[2]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_TurnOnEntryTones":
        if ACW30_EntryTonesMode("TurnOn")==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_TurnOffEntryTones":
        if ACW30_EntryTonesMode("TurnOff")==True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_ViewContactDetails":
        if ACW30_ViewContactDetails(sData[1]) == True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_SendIMs" or sData[0] =="ACW30_InitiateAMMFromSearchedContact":
        if ACW30_SendIMs(sData[1], sData[2], sData[3], sData[4]) == True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_ReceiveIMs":
        if ACW30_ReceiveIMs(sData[1], sData[2]) == True:
            resultString =  "Pass"   
    elif sData[0]=="ACW30_OpenConversation":
        if ACW30_OpenConversation(sData[1]) == True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_VerifyCallLog":
        if ACW30_VerifyCallLog(sData[1], sData[2] ):
            resultString =  "Pass"
    elif sData[0]=="ACW30_LeaveAllConversation":
        if ACW30_LeaveAllConversation() == True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_CreateNewContactWithManyExtension":
        if ACW30_CreateNewContactWithManyExtension(sData[1]):
            resultString =  "Pass"                
    elif sData[0]=="ACW30_ConfigureExclusion":
        if ACW30_ConfigureExclusion(sData[1]) == True:
            resultString =  "Pass"        
    elif sData[0]=="ACW30_SelectStatus":
        if ACW30_ChangePresenceState(sData[1]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_ChangePresenceState":
        if ACW30_ChangePresenceState(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_CheckContactStatus" or sData[0]=="ACW30_CheckContactPresenceState":
        if ACW30_CheckContactPresenceState(sData[1], sData[2]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_ConfigureAutoSetToAway":
        if ACW30_ConfigureAutoSetToAway(sData[1]):
            resultString =  "Pass"     
    elif sData[0]=="ACW30_disableAMM":
        if ACW30_disableAMM() == True:
            resultString =  "Pass"              
    elif sData[0]=="ACW30_CheckContactStatusDetail":
        if ACW30_CheckContactStatusDetail(sData[1], sData[2]):
            resultString =  "Pass"     
    elif sData[0]=="ACW30_VerifyContactPresenceInContactDetailView":
        if ACW30_VerifyContactPresenceInContactDetailView(sData[1]) == True:
            resultString =  "Pass"               
    elif sData[0]=="ACW30_VerifyContactStatusMessageInContactDetailView":
        if ACW30_VerifyContactStatusMessageInContactDetailView(sData[1]) == True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_ChangeStatusMessage" or sData[0]=="ACW30_ChangePresenceNote":
        if ACW30_ChangeStatusMessage(sData[1]) == True:
            resultString =  "Pass"      
    elif sData[0]=="ACW30_CheckSelfPresenceState":
        if ACW30_CheckSelfPresenceState(sData[1]) == True:
            resultString =  "Pass"       
    elif sData[0]=="ACW30_OpenCallLogDetail":
        if ACW30_OpenCallLogDetail(sData[1], sData[2]) == True:
            resultString =  "Pass"        
    elif sData[0]=="ACW30_VerifyPresenceStateFromCallLogDetail":
        if ACW30_VerifyPresenceStateFromCallLogDetail(sData[1]) == True:
            resultString =  "Pass"            
    elif sData[0]=="ACW30_MakeCallFromCallLogDetail":
        if ACW30_MakeCallFromCallLogDetail(sData[1]) == True:
            resultString =  "Pass"        
    elif sData[0]=="ACW30_SendIMsFromCallLogDetail":
        if ACW30_SendIMsFromCallLogDetail(sData[1], sData[2]) == True:
            resultString =  "Pass"     
    elif sData[0]=="ACW30_DeleteCallLog":
        if ACW30_DeleteCallLog(sData[1], sData[2]) == True:
            resultString =  "Pass"                  
    elif sData[0]=="ACW30_ConfigureIncomingCallsFeatures":
        if ACW30_ConfigureIncomingCallsFeatures(sData[1], sData[2], sData[3]):
            resultString =  "Pass"        
    elif sData[0]=="ACW30_AddContactFromCallLogDetail":
        if ACW30_AddContactFromCallLogDetail(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_ConfigureDndSacLink":
        if ACW30_ConfigureDndSacLink(sData[1]):
            resultString =  "Pass"        
    elif sData[0]=="ACW30_RememberPassword":
        if ACW30_RememberPassword(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_LoginWithRememberPassword":
        if ACW30_LoginWithRememberPassword():
            resultString =  "Pass"       
    elif sData[0]=="ACW30_ChangeConversationSubject":
        if ACW30_ChangeConversationSubject(sData[1]):
            resultString =  "Pass"        
    elif sData[0]=="ACW30_AddSomeoneToCall":
        if ACW30_AddSomeoneToCall(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_AddSomeoneToCallMeetMe":
        if ACW30_AddSomeoneToCallMeetMe(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureDialRule":
        if ACW30_ConfigureDialRule(sData[1], sData[2]):
            resultString =  "Pass"  
    elif sData[0]=="ACW30_MakeCallAndVerifyDialRule":
        if ACW30_MakeCallAndVerifyDialRule(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyFirstCallLogDisplayName":
        if ACW30_VerifyFirstCallLogDisplayName(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_CallFromConversation":
        if ACW30_CallFromConversation(sData[1], sData[2]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_ParkCall":
        if ACW30_ParkCall(sData[1]):
            resultString =  "Pass"               
    elif sData[0]=="ACW30_UnparkCall":
        if ACW30_UnparkCall(sData[1]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_PickupGroupCall":
        if ACW30_PickupGroupCall():
            resultString =  "Pass"      
    elif sData[0]=="ACW30_ExtendedPickupCall":
        if ACW30_ExtendedPickupCall(sData[1]):
            resultString =  "Pass"          
    elif sData[0]=="ACW30_FilterParticipants":
        if ACW30_FilterParticipants(sData[1], sData[2]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_DragDropContactToConference":
        if ACW30_DragDropContactToConference(sData[1], sData[2]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_DirectedPickupCall":
        if ACW30_DirectedPickupCall(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_SendMessageInPublicChat":
        if ACW30_SendMessageInPublicChat(sData[1]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_ReceiveMessageInPublicChat":
        if ACW30_ReceiveMessageInPublicChat(sData[1]):
            resultString =  "Pass"    
    elif sData[0]=="ACW30_CheckPresenceStateFromTopOfMind":
        if ACW30_CheckPresenceStateFromTopOfMind(sData[1], sData[2]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_OpenConversationFromTopOfMind":
        if ACW30_OpenConversationFromTopOfMind(sData[1]):
            resultString =  "Pass"       
    elif sData[0]=="ACW30_ReceiveAttachment":
        if ACW30_ReceiveAttachment(sData[1],sData[2]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_AddContactsToStagingAreaUsingDialPad":
        if ACW30_AddContactsToStagingAreaUsingDialPad(sData[1]):
            resultString =  "Pass"      
    elif sData[0]=="ACW30_AddContactsToStagingAreaUsingDragDrop":
        if ACW30_AddContactsToStagingAreaUsingDragDrop(sData[1], sData[2]):
            resultString =  "Pass"   
    elif sData[0]=="ACW30_MakeCallFromStagingArea":
        if ACW30_MakeCallFromStagingArea(sData[1]):
            resultString =  "Pass" 
    elif sData[0]=="ACW30_RemoveAllContactsFromStagingArea":
        if ACW30_RemoveAllContactsFromStagingArea():
            resultString =  "Pass" 
    elif sData[0]=="ACW30_SendAttachment":
        if ACW30_SendAttachment(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifySelfViewVideo":
        if ACW30_VerifySelfViewVideo(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyVideoStream":
        if ACW30_VerifyVideoStream(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_SwitchContentView":
        if ACW30_SwitchContentView():
            resultString =  "Pass"        
    elif sData[0]=="ACW30_CloseSelfViewVideo":
        if ACW30_OpenAndCloseSelfViewVideo("Close"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_OpenSelfViewVideo":
        if ACW30_OpenAndCloseSelfViewVideo("Open"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_MaximizeContentView":
        if ACW30_MaximizeAndRestoreContentView("Maximize"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_RestoreContentView":
        if ACW30_MaximizeAndRestoreContentView("Restore"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_DetachContentView":
        if ACW30_DetachContentView():
            resultString =  "Pass"
    elif sData[0]=="ACW30_ReattachContentView":
        if ACW30_ReattachContentView():
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyIncomingCallFeatures":
        if ACW30_VerifyIncomingCallFeatures(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_MaximizeVideoView":
        if ACW30_MaximizeAndRestoreVideoView("Maximize"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_RestoreVideoView":
        if ACW30_MaximizeAndRestoreVideoView("Restore"):
            resultString =  "Pass"
    elif sData[0]=="ACW30_CountParticipantInTheMeeting":
        if ACW30_CountParticipantInTheMeeting(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_AddParticipantIntoConversationUsingDragDrop":
        if ACW30_AddParticipantIntoConversationUsingDragDrop(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ChangeNicknameOfContact":
        if ACW30_ChangeNicknameOfContact(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_CheckNicknameOfContact":
        if ACW30_CheckNicknameOfContact(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureACS":
        if ACW30_ConfigureACS(sData[1], sData[2], sData[3], sData[4]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_BridgeInCall":
        if ACW30_BridgeInCall(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_AnswerBridgeCall":
        if ACW30_AnswerBridgeCall(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyIncomingBridgeCall":
        if ACW30_VerifyIncomingBridgeCall(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_ConfigureCallAs":
        if ACW30_ConfigureCallAs(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_MakeCallfromSecondary":
        if ACW30_MakeCallfromSecondary(sData[1], sData[2], sData[3]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_OnP2PStartSharing":
        if ACW30_P2PStartSharing("On")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_OffP2PStartSharing":
        if ACW30_P2PStartSharing("Off")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_LoginPortal":
        if ACW30_LoginPortal(sData[1], sData[2], sData[3], sData[4], sData[5]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_JoinScopiaConferenceAsMeetmeMode":
        if ACW30_JoinScopiaConferenceAsMeetmeMode(sData[1], sData[2], sData[3], sData[4], sData[5]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_JoinScopiaConferenceAsMeetmeModeWithPOM":
        if ACW30_JoinScopiaConferenceAsMeetmeModeWithPOM(sData[1], sData[2], sData[3], sData[4], sData[5], sData[6]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_RaiseHand":
        if ACW30_RaiseHand(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_LowerHand":
        if ACW30_LowerHand(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyRaisingHand":
        if ACW30_VerifyRaisingLoweringHand(sData[1],"raising")==True:
            resultString =  "Pass"  
    elif sData[0]=="ACW30_VerifyLoweringHand":
        if ACW30_VerifyRaisingLoweringHand(sData[1],"lowering")==True:
            resultString =  "Pass" 
    elif sData[0]=="ACW30_JoinScopiaConferenceAsTEMode":
        if ACW30_JoinScopiaConferenceAsTEMode(sData[1], sData[2], sData[3]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_JoinScopiaConferenceAsTEModeWithPOM":
        if ACW30_JoinScopiaConferenceAsTEModeWithPOM(sData[1], sData[2], sData[3], sData[4], sData[5], sData[6], sData[7]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_AdmitRequest":
        if ACW30_AdmitRequest():
            resultString =  "Pass"
    elif sData[0]=="ACW30_RefuseRequest":
        if ACW30_RefuseRequest():
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyRequestNotification":
        if ACW30_VerifyRequestNotification():
            resultString =  "Pass"
    elif sData[0]=="ACW30_BecomeModerator":
        if ACW30_BecomeModerator(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_SwitchToMeetmeMode":
        if ACW30_SwitchToMeetmeMode():
            resultString =  "Pass"
    elif sData[0]=="ACW30_JoinExchangeMeeting":
        if ACW30_JoinExchangeMeeting(sData[1],sData[2]):
            resultString = "Pass"
    elif sData[0]=="ACW30_JoinExchangeMeetingUsingURL":
        if ACW30_JoinExchangeMeetingUsingURL(sData[1], sData[2]):
            resultString = "Pass"
    elif sData[0]=="ACW30_ViewCallStatistics":
        if ACW30_ViewCallStatistics(sData[1]):
            resultString = "Pass"

    elif sData[0]=="ACW30_VerifyParticipantNameInRosterList":
        if ACW30_VerifyParticipantNameInRosterList(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_EnterPasscode":
        if ACW30_EnterPasscode(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_PromoteLecturer":
        if ACW30_PromoteLecturer(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_DemoteLecturer":
        if ACW30_DemoteLecturer(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyLectureMode":
        if ACW30_VerifyLectureMode(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyLecturer":
        if ACW30_VerifyLecturer(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_AutoConfiguration_CI":
        if ACW30_AutoConfiguration_CI(sData[1], sData[2], sData[3], sData[4], sData[5]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_LoginWithAutoConfig":
        if ACW30_LoginWithAutoConfig(sData[1], sData[2], sData[3], sData[4], sData[5]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_EnableShareControls":
        if ACW30_EnableShareControls(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_DisableShareControls":
        if ACW30_DisableShareControls(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyEncryption":
        if ACW30_ViewAudioCallStatistics("audioEncryption"):
            resultString = "Pass"
    elif sData[0]=="ACW30_JoinEquinoxMeetingFromCallLogDetails":
        if ACW30_JoinEquinoxMeetingFromCallLogDetails(sData[1]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_VerifyMeetingMode":
        if ACW30_VerifyMeetingMode(sData[1], sData[2]):
            resultString =  "Pass"
    elif sData[0]=="ACW30_JoinMeetingFromCallLogDetails":
        if ACW30_JoinMeetingFromCallLogDetails(sData[1], sData[2], sData[3]):
            resultString =  "Pass"
    # resultString =  Fail immediately if keyword not found
    else:     
        WriteResults(1,"Keyword not found")
        resultString =  "Fail\nKeyword not found!"
    
    if resultString == "Pass":
        WriteResults(1,"Result is Pass") 
    else:
        resultString =  resultWithLogs(sData[0])
        WriteResults(1,"Result is Fail")
    
    return resultString
