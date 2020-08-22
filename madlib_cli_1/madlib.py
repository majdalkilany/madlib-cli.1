def welcom() :

    """
    print welcom message 
    """
    print('''welcom in madlib game
    
     please  fill the blanks in the words
    ''')


def read_file() :
    '''
    read text from file  
    '''
    fname = open('assets/mad_file.txt','r')
    fname = fname.read()
    fname =fname.strip()
    return(fname)

def parse(fname):
        '''
        parse text and extract the words between  '{} and put it in list '
        '''
    
        
        second_pos = 0
        counter_parn = fname.count('{')
        user_inputs = []
        for i in range(counter_parn):
            first_pos = fname.find('{',second_pos) + 1
            second_pos = fname.find('}',first_pos)
            # print(fname[first_pos:second_pos])
            the_word = fname[first_pos:second_pos]

            
            
            # user_input = input(f' please  enter {the_word}  >> ')  
            
            user_inputs.append(the_word)
        # print(user_inputs)
        return user_inputs 
        

def user_input(l_u) :

    '''
     take list 
     and put every value in print to take value from user 
    '''
    new_words_list = []
    print(l_u)
    for i in range (len(l_u) ) :
             user_input = input(f' please  enter {l_u[i]}  >> ')
             new_words_list.append(user_input)
    return new_words_list

        


def merge_and_write_file(list_words , fname) :
    
            '''
            take 2 arguments list and txt 
            put the words in list after remove the word betwwen {}  and put the new word
            '''
            

            for i in range(len(list_words)) :
                first_pos = fname.find('{',0) 
                second_pos = fname.find('}',0)+1
                # print(fname[first_pos:second_pos])
                fname = fname[:first_pos] +list_words[i] + fname[second_pos:]
    # print(fname)

                txt = open('assets/ready.txt','w')
                txt.write(fname)

            return fname 

    


if __name__ == "__main__":
    fname = read_file()
    list_words =   parse(fname)
    # print(list_words)
    new_words = user_input(list_words)

    majd=merge_and_write_file(new_words,fname)
    print(majd)