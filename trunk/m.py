

isMayaRunning = False
try:
    # if outside maya, init maya!
    #try:
    #    import maya.standalone maya.standalone.initialize( )
    #except:
    #    pass

    # now import the modules we need into m
    from maya.cmds import * 
    from maya import utils
    from maya.mel import eval as mel
    
    # trying to fix OSX
    import sys
    sys.stdin.write = lambda self, data: utils.executeDeferred(data)
    sys.stdin.flush = lambda self: None
    
    isMayaRunning = True


    import os
    global scriptEditorCallbackID
    def redirectScriptEditor( file=os.path.join(os.environ['TMP'], 'mayaScriptEditorOutput.log') ):
        global scriptEditorCallbackID
        def callback(nativeMsg,   messageType, data):
            f=open( file, 'a')
            f.write('%s' % (nativeMsg) )
            f.close()
        
        try: 
            scriptEditorCallbackID
        except:
            import maya.OpenMaya as mo
            f=open( file, 'w')
            f.close()
            scriptEditorCallbackID = mo.MCommandMessage.addCommandOutputCallback(callback, None)

    def redirectScriptEditorStop():
        global scriptEditorCallbackID
        import maya.OpenMaya as mo
        mo.MCommandMessage.removeCallback(scriptEditorCallbackID)
        del scriptEditorCallbackID

    del os
    
except:
    isMayaRunning = False





