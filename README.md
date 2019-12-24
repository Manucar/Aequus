# Aequus
*Low cost portable system for interactive balance exercise games for rehabilitation.*

# *Context*
The fear of falling is one of the elements that most limits the active life of subjects who have experienced a fall. There is a strong need for the patient with Multiple Sclerosis, but in reality for many patients with neuromotor diseases and frail elderly people, to minimize the risk of falling, and the associated fear of falling. It is necessary to have low-cost technological solutions that can be used at home that encourage the safe execution of exercises aimed at improving the control of balance, giving awareness to the subject of his own ability and improvements.

# *Project design*
-img

Aequus is composed of a Raspbery Pi that acts like a master to control 6 MPU6050 sensors disposed along the back strap, and runs the main game application.

# *Usage information*

- All the files have to be uploaded to a Raspberry Pi (≥3)
- Connect all the sensors to a I2C Mux Expander and place them on a back strap
-img

- Install all the requirements in requirements.txt
    ```sh
    $ pip3 install -r requirements.txt
    ```

- Run DiSfida_APP.py
    - click on training
    - choose the preferences (Duration, Difficulty)
    - click on start
    - wait the connection of all the sensors
    - play

- Video:
