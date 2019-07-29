import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
messages={}
notes=[]
with open(input_file,"r",newline="") as text_file:
    for row in text_file:
        if "[Note]" in row:
            row_list=row.split(" ",4)
            date=row_list[0].strip()
            note=row_list[4].strip("\n").strip()
            if note not in notes:
                notes.append(note)
            if date not in messages.keys():
                messages[date]={note:1}
            elif note not in messages[date].keys():
                messages[date][note]=1
            else:
                messages[date][note]+=1

filewriter=open(output_file,"w",newline="")
header=notes[:]
header.insert(0,"Date")
header=",".join(map(str,header))+"\n"
print(header)
filewriter.write(header)
for date,sub_dict in messages.items():
    row_list=[date]
    for index in range(len(notes)):
        row_list.append(sub_dict.get(notes[index],0))
    output=",".join(map(str,row_list))+"\n"
    print(output)
    filewriter.write(output)
filewriter.close()