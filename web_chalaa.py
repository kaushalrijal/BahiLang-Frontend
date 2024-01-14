from contextlib import redirect_stdout
from io import StringIO

def execute(code):
    # list = [line.strip() for line in code.split("\n")]
    list = code.split('\n')
    # output = "" 
    output = []
    output_buffer = StringIO()
    for i in list:
        if 'bhan bhai' in i:
            # output+=(i.replace("bhan bhai", "print"))
            output.append(i.replace('bhan bhai', 'print'))
        elif 'yo ho bhai' in i:
            output.append(i.replace("yo ho bhai ", ""))
            # output +=(i.replace("yo ho bhai ", ""))
        elif 'haal bhai' in i:
            output.append(i.replace("haal bhai", "input"))
            # output +=(i.replace("haal bhai", "input"))
        else:
            # output += i
            output.append(i)
    with redirect_stdout(output_buffer):
        for i in output:
            try:
                exec(i)
            except:
                print("ke garya bhai, ke garyaaa? error bhayo ta")
                break

    captured_output = output_buffer.getvalue()

    return captured_output