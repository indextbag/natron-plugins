# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_emboss_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_emboss_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_emboss_GL"

def getLabel():
    return "Crok_emboss_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Crok_emboss_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Simulates an emboss effect."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("STYLE", "Style")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.STYLE = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Height : ")
    param.setMinimum(-1000, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(-1000, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(20, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "Specular : ")
    param.setMinimum(-99.99999999999999, 0)
    param.setMaximum(99.99999999999999, 0)
    param.setDisplayMinimum(-99.99999999999999, 0)
    param.setDisplayMaximum(99.99999999999999, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat3", "Light height : ")
    param.setMinimum(-1000, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(-1000, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat4", "View height : ")
    param.setMinimum(-1000, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(-1000, 0)
    param.setDisplayMaximum(1000, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createSeparatorParam("LIGHT", "Light")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LIGHT = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createDouble2DParam("Shadertoy1_2paramValueVec20", "Light position : ")
    param.setDefaultValue(959.9999999999999, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(540, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec20 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createSeparatorParam("OUTPUT", "Output")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OUTPUT = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool5", "Show normal map : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool5 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_emboss_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3911)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueVec20")
    if param is not None:
        param.setValue(959.9999999999999, 0)
        param.setValue(540, 1)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/run/media/root/FABRICE/PERSO/NATRON/GIT_DEV/natron-plugins/Shadertoy/Crok_emboss.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_emboss Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : crok_emboss Matchbox for Autodesk Flame\n\n\n// iChannel0: Source, filter = nearest\n// BBox: iChannel0\n\n// based on https://www.shadertoy.com/view/XdlGz8\n\n\n\nvec2 resolution = vec2(iResolution.x, iResolution.y);\n\nuniform vec2 position = vec2(960,540); // Light position : (light position in x / y)\n\nuniform float fNormalScale = 20.0; // Height : (bump height), min=-1000, max=1000\nuniform float spec = 1.0; // Specular : (adjust the glossiness), min=-100, max=100\nuniform float fLightHeight = 10.0; // Light height : (height of the lightsource), min=-1000, max=1000\nuniform float fViewHeight = 0.0; // View height : (view height), min=-1000, max=1000\n\n\nuniform bool SHOW_NORMAL_MAP = false; // Show normal map : (show normal map)\n\nstruct C_Sample\n{\n\tvec3 vAlbedo;\n\tvec3 vNormal;\n};\n\t\nC_Sample SampleMaterial(const in vec2 vUV, sampler2D sampler,  const in vec2 vTextureSize, const in float fNormalScale)\n{\n\tC_Sample result;\n\t\n\tvec2 vInvTextureSize = vec2(1.0) / vTextureSize;\n\t\n\tvec3 cSampleNegXNegY = texture2D(sampler, vUV + (vec2(-1.0, -1.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSampleZerXNegY = texture2D(sampler, vUV + (vec2( 0.0, -1.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSamplePosXNegY = texture2D(sampler, vUV + (vec2( 1.0, -1.0)) * vInvTextureSize.xy).rgb;\n\t\n\tvec3 cSampleNegXZerY = texture2D(sampler, vUV + (vec2(-1.0, 0.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSampleZerXZerY = texture2D(sampler, vUV + (vec2( 0.0, 0.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSamplePosXZerY = texture2D(sampler, vUV + (vec2( 1.0, 0.0)) * vInvTextureSize.xy).rgb;\n\t\n\tvec3 cSampleNegXPosY = texture2D(sampler, vUV + (vec2(-1.0,  1.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSampleZerXPosY = texture2D(sampler, vUV + (vec2( 0.0,  1.0)) * vInvTextureSize.xy).rgb;\n\tvec3 cSamplePosXPosY = texture2D(sampler, vUV + (vec2( 1.0,  1.0)) * vInvTextureSize.xy).rgb;\n\n\t// convert to linear\t\n\tvec3 cLSampleNegXNegY = cSampleNegXNegY * cSampleNegXNegY;\n\tvec3 cLSampleZerXNegY = cSampleZerXNegY * cSampleZerXNegY;\n\tvec3 cLSamplePosXNegY = cSamplePosXNegY * cSamplePosXNegY;\n\n\tvec3 cLSampleNegXZerY = cSampleNegXZerY * cSampleNegXZerY;\n\tvec3 cLSampleZerXZerY = cSampleZerXZerY * cSampleZerXZerY;\n\tvec3 cLSamplePosXZerY = cSamplePosXZerY * cSamplePosXZerY;\n\n\tvec3 cLSampleNegXPosY = cSampleNegXPosY * cSampleNegXPosY;\n\tvec3 cLSampleZerXPosY = cSampleZerXPosY * cSampleZerXPosY;\n\tvec3 cLSamplePosXPosY = cSamplePosXPosY * cSamplePosXPosY;\n\n\t// Average samples to get albdeo colour\n\tresult.vAlbedo = ( cLSampleNegXNegY + cLSampleZerXNegY + cLSamplePosXNegY \n\t\t    \t     + cLSampleNegXZerY + cLSampleZerXZerY + cLSamplePosXZerY\n\t\t    \t     + cLSampleNegXPosY + cLSampleZerXPosY + cLSamplePosXPosY ) / 9.0;\t\n\t\n\tvec3 vScale = vec3(0.3333);\n\t\n\t\n\t\tfloat fSampleNegXNegY = dot(cLSampleNegXNegY, vScale);\n\t\tfloat fSampleZerXNegY = dot(cLSampleZerXNegY, vScale);\n\t\tfloat fSamplePosXNegY = dot(cLSamplePosXNegY, vScale);\n\t\t\n\t\tfloat fSampleNegXZerY = dot(cLSampleNegXZerY, vScale);\n\t\tfloat fSampleZerXZerY = dot(cLSampleZerXZerY, vScale);\n\t\tfloat fSamplePosXZerY = dot(cLSamplePosXZerY, vScale);\n\t\t\n\t\tfloat fSampleNegXPosY = dot(cLSampleNegXPosY, vScale);\n\t\tfloat fSampleZerXPosY = dot(cLSampleZerXPosY, vScale);\n\t\tfloat fSamplePosXPosY = dot(cLSamplePosXPosY, vScale);\n\n\t\n\t// Sobel operator - http://en.wikipedia.org/wiki/Sobel_operator\n\t\n\tvec2 vEdge;\n\tvEdge.x = (fSampleNegXNegY - fSamplePosXNegY) * 0.25 \n\t\t\t+ (fSampleNegXZerY - fSamplePosXZerY) * 0.5\n\t\t\t+ (fSampleNegXPosY - fSamplePosXPosY) * 0.25;\n\n\tvEdge.y = (fSampleNegXNegY - fSampleNegXPosY) * 0.25 \n\t\t\t+ (fSampleZerXNegY - fSampleZerXPosY) * 0.5\n\t\t\t+ (fSamplePosXNegY - fSamplePosXPosY) * 0.25;\n\n\tresult.vNormal = normalize(vec3(vEdge * fNormalScale, 1.0));\t\n\t\n\treturn result;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\t\n\tvec2 uv = fragCoord.xy / resolution.xy;\n\t\n\tC_Sample materialSample;\n\t\t\n\tmaterialSample = SampleMaterial( uv, iChannel0, resolution.xy, fNormalScale );\n\n\tvec3 vSurfacePos = vec3(uv, 0.0);\n\n\tvec3 vViewPos = vec3(0.5, 0.5, fViewHeight);\n\n\tvec3 vLightPos = vec3(position, fLightHeight);\n\n\t\n\tvec3 vDirToView = normalize( vViewPos - vSurfacePos );\n\tvec3 vDirToLight = normalize( vLightPos - vSurfacePos );\n\t\t\n\tfloat fNDotL = clamp( dot(materialSample.vNormal, vDirToLight), 0.0, 1.0);\n\tfloat fDiffuse = fNDotL;\n\t\n\tvec3 vHalf = normalize( vDirToView + vDirToLight );\n\tfloat fNDotH = clamp( dot(materialSample.vNormal, vHalf), 0.0, 1.0);\n\tfloat fSpec = pow(fNDotH, 10.) * fNDotL * spec;\n\t\n\tvec3 vResult = materialSample.vAlbedo * fDiffuse + fSpec;\n\t\n\tvResult = sqrt(vResult);\n\t\n\tif ( SHOW_NORMAL_MAP )\n\t\tvResult = materialSample.vNormal * 0.5 + 0.5;\n\t\n\tfragColor = vec4(vResult,1.0);\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(6, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("vec2")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("position")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Light position :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("light position in x / y")
        del param

    param = lastNode.getParam("paramDefaultVec20")
    if param is not None:
        param.setValue(959.9999999999999, 0)
        param.setValue(540, 1)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("fNormalScale")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Height :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("bump height")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(-1000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(1000, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("spec")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Specular :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("adjust the glossiness")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(-99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("fLightHeight")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Light height :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("height of the lightsource")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(-1000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(1000, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("fViewHeight")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("View height :")
        del param

    param = lastNode.getParam("paramHint4")
    if param is not None:
        param.setValue("view height")
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(-1000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(1000, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("SHOW_NORMAL_MAP")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Show normal map :")
        del param

    param = lastNode.getParam("paramHint5")
    if param is not None:
        param.setValue("show normal map")
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3775)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)

    param = groupShadertoy1_2.getParam("paramValueVec20")
    group.getParam("Shadertoy1_2paramValueVec20").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat2")
    group.getParam("Shadertoy1_2paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat3")
    group.getParam("Shadertoy1_2paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat4")
    group.getParam("Shadertoy1_2paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool5")
    group.getParam("Shadertoy1_2paramValueBool5").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Crok_emboss_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)