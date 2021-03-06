#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *
from mcpi.block import *
from blockData import *

# this means that the file can be imported without executing anything in this code block
if __name__ == "__main__":

    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """

    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    # Get the current tile/block that the player is located at in the world
    playerPosition = mc.player.getTilePos()

    height = mc.getHeight(playerPosition.x, playerPosition.z)
    # create the output message as a string
    message = "Height is "+ str(height)
    
     # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
    
    # Get the type of block for the highest point in world
    # This is done at the horizonal player posn
    blockIdNum = mc.getBlock(playerPosition.x, height , playerPosition.z)
    

    if (blockIdNum == AIR.id):
         # Need to do height minus one for this as not flower etc
         blockIdNum = mc.getBlock(playerPosition.x, height -1 , playerPosition.z)
    
    blockName = getBlockNameFromId(blockIdNum)
    # Add to message, the type of block stood on
    message = "Block is of type " + str(blockIdNum)+ " which is " + blockName

    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
