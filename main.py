from pyscript import display, document

def add_members (e):

    Grade_7 = {'Johnathan Price', 'John McTavish', 'Kyle Garrick', 'Simon Riley'}
    Grade_8 = {'Imran Zhakaev', 'Raul Menendez', 'Vladimir Makarov', 'Elias'}
    Grade_9 = {'Logan Walker', 'David Walker', 'Keegan Russ', 'iforgot'}
    Grade_10 = {'Russell Adler', 'Frank Woods', 'Alex Mason', 'Jason Hudson'}



    input_memfn = document.getElementById('input1').value.lower
    input_memln = document.getElementById('input2').value.lower

    new_studentname = input_memfn + " " + input_memln
    new_student = {new_studentname}




    all_members = Grade_7 | Grade_8 | Grade_9 | Grade_10

    total_members = len(all_members)

    member_list = "<br>".join(sorted(all_members))



    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}' 
    
    display(f'Total members: {total_members}', target="output1")