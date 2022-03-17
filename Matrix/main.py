import pygame
from pygame.locals import *
from random import randrange, choice

pygame.init()

## Define all the constants
WIDTH, HEIGHT = 900, 700

BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE= (255,255,255)

FONT_SIZE = 10
font = pygame.font.SysFont('arial', FONT_SIZE, True, False)

FPS = 30

letters = [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MATRIX")



class matrix:
    def __init__(self):
        self.fill = 1  ## ??
        self.x_random = randrange(FONT_SIZE, WIDTH + FONT_SIZE, FONT_SIZE)
        self.y_random = randrange(0, HEIGHT + FONT_SIZE, FONT_SIZE)
        self.y_random_list = []
        self.y_random_list.append(self.y_random)
        self.letters_list = []
        
    ## Generate the char letter list and draw a line with the chars in the position x, y
    def draw_matrix(self):
        random_letter = choice(letters)
        self.letters_list.append(random_letter)

        ## Draw the rectangle with chars
        for msg, position_y in zip(self.letters_list, self.y_random_list):
            message = f'{msg}'
            draw_message = font.render(message, True, GREEN)
            screen.blit(draw_message, (self.x_random, position_y))

    
    ## Create the cascade effect
    def move_matrix(self):
       
        ## Redraws (clear) the rectangle that the object occupies 
        if self.y_random > HEIGHT or len(self.y_random_list) > 20:
            message = ' '
            draw_message = font.render(message, True, BLACK)
            
            screen.fill(BLACK, (self.x_random, self.y_random_list[0], draw_message.get_width() + FONT_SIZE, 
                        draw_message.get_height() * self.fill))
            
            ## Clear the the letter list     
            if draw_message.get_height() * self.fill > len(self.y_random_list) * draw_message.get_height():
                self.letters_list.clear() ## letter_list = []
            else:
                self.fill += 1


        ## Draws the last char generated in my list
        else:    
            self.y_random += FONT_SIZE
            self.y_random_list.append(self.y_random)
            message = f'{self.letters_list[-1]}'
            draw_message = font.render(message, True, BLACK)
            screen.blit(draw_message, (self.x_random, self.y_random_list[-1]))




## Generate objects
def gen_obj(obj_lst, obj_lst_clone, num_of_obj, gen_obj_condition):
    if gen_obj_condition:
        for i in range(num_of_obj):
            new_obj = matrix()

            ## Delete the object if it repeats the X position or if the object oversize the screen height
            if new_obj.x_random in obj_lst_clone or new_obj.y_random > HEIGHT:  
                obj_lst_clone.remove(new_obj.x_random)
                del new_obj
            else:    
                obj_lst.append(new_obj)
                obj_lst_clone.append(new_obj.x_random)

        for i in obj_lst:
            i.draw_matrix()
            i.move_matrix()

    else:
        FONT_SIZE = 20
        font = pygame.font.SysFont('arial', FONT_SIZE, True, False)
        message = '## Error: Your MATRIX generator off ##'
        len_messaje = len(message)
        draw_message = font.render(message, True, GREEN)
        screen.blit(draw_message, (((WIDTH-FONT_SIZE)/2)-len_messaje*4, (HEIGHT-FONT_SIZE-4)/2))


### Draw the changes on the screen
def draw_screen(obj_lst,obj_lst_clone, num_of_obj, gen_obj_condition): 
    screen.fill(BLACK)
    gen_obj(obj_lst,obj_lst_clone, num_of_obj, gen_obj_condition)
    pygame.display.flip()


def main():
    obj_lst = []
    obj_lst_clone = []
    num_of_obj = 35
    gen_obj_condition = False
    initial_time = 0
    current_time = 0

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
        current_time = pygame.time.get_ticks()

        if current_time - initial_time > 500: ## Starts drawing the generated objects at 500ms
            gen_obj_condition = True
            draw_screen(obj_lst, obj_lst_clone, num_of_obj, gen_obj_condition)
    
    pygame.quit()

if __name__ == "__main__":
    main()
