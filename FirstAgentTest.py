import gym
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import imageio

def saveanimation(frames,address="./movie.gif"):
    """ 
    This method ,given the frames of images make the gif and save it in the folder
    
    params:
        frames:method takes in the array or np.array of images
        address:(optional)given the address/location saves the gif on that location
                otherwise save it to default address './movie.gif'
    
    return :
        none
    """
    imageio.mimsave(address, frames)


def testGymImageSave():
    env = gym.make('CartPole-v0')
    env.reset()
    frames = []
    for _ in range(1000):
        frames.append(env.render(mode = 'rgb_array'))
        action = env.action_space.sample()
        obs,reward,done,info = env.step(action) # take a random action
        if done:
            break
    env.close()
    ## save the images as array
    saveanimation(frames)

