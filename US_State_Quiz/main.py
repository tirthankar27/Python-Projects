import turtle
import pandas as pd
from write_turtle import Write

screen = turtle.Screen()
screen.title("U.S States Game")

imgturtle=turtle.Turtle()
image="blank_states_img.gif"
screen.addshape(image)
imgturtle.shape(image)
writer=Write()

data=pd.read_csv("50_states.csv")

state_list=list()
while len(state_list)<50:
    user_answer=screen.textinput(title=f"{len(state_list)}/50 Guess the state",prompt="What's the state name?")
    if user_answer is not None:
        user_answer=user_answer.capitalize()
    else:
        break
    if user_answer == 'Exit':
        break
    filtered_data=data[data.state==user_answer]
    if filtered_data.empty or state_list.count(user_answer)>0:
        continue
    else:
        writer.write_turtle(filtered_data)
        state_list.append(user_answer)

if len(state_list)==50:
    writer.print_msg("Congratulations!! You found all the states")
elif len(state_list)<50:
    writer.print_msg("Sorry!! You could not find all the states")
    filtered_list=data[~data['state'].isin(state_list)]['state'].tolist()
    new_df=pd.DataFrame(filtered_list)
    new_df.to_csv("states_to_learn.csv")
    print(f"You didn't get these states\n{filtered_list}")

screen.exitonclick()
