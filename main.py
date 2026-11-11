from pyscript import display, document

def add_members (e):

    Grade_7 = {'Johnathan Price', 'John McTavish', 'Kyle Garrick', 'Simon Riley'}
    Grade_8 = {'Imran Zhakaev', 'Raul Menendez', 'Vladimir Makarov', 'Elias Walker'}        #all current members in the club
    Grade_9 = {'Logan Walker', 'David Walker', 'Keegan Russ', 'Thomas Merrick'}             
    Grade_10 = {'Russell Adler', 'Frank Woods', 'Alex Mason', 'Jason Hudson'}



    input_memfn = document.getElementById('input1').value   #first name
    input_memln = document.getElementById('input2').value   #last name

    new_studentname = input_memfn + " " + input_memln   #combines the names with a space inbetween
    new_student = {new_studentname} #proper name




    all_members = Grade_7 | Grade_8 | Grade_9 | Grade_10 | new_student  #combines all members, including the inputed student

    total_members = len(all_members)    #how many student

    member_list = "<br>".join(sorted(all_members))  #all members but alphabetical 



    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}'   #shows the sorted / alphabetical list
    
    display(f'Total members: {total_members}', target="output1")  #the len
