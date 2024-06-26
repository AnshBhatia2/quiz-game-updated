import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

score = 0
time_left = 10
marquee_message = ""
is_game_over = False
question_file_name = "questions.txt"
questions = []
question_index = 0
question_count = 0
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"navy blue")
    screen.draw.filled_rect(timer_box,"navy blue")
    screen.draw.filled_rect(skip_box,"dark green")
    for box in answer_boxes:
        screen.draw.filled_rect(box,"orange")
    
    marquee_message = f"Welcome to Quiz Master... Q: {question_index} of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box,color="white")
    screen.draw.textbox(str(time_left),timer_box,color="white",shadow=(0.5,0.5),scolor="light green")
    screen.draw.textbox("Skip",skip_box,color="white",shadow=(0.5,0.5),scolor="light green",angle=-90)
    screen.draw.textbox(question[0].strip(),question_box,color="white",shadow=(0.5,0.5),scolor="dim grey")
    
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index += 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_next_question():
    global question_index,questions
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        

def read_question_file():
    global question_count, question_file_name, questions
    #writing down the code for reading a text file in python
    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

pgzrun.go()