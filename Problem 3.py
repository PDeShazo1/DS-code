import string   # using string to get the A to Z character in string

players = list(string.ascii_uppercase)  # creating list of A to Z using string class
count = 0   # variable to keep on counting
x = 0   # variable to access players list using index
rem_count = 0   # to count the numbers of removed character count
# while 25 out of 26 characters aren't removed keep on loop
while rem_count<25:
    # if the count is multiple of 10, and the 
    if (count+1)%10==0 and players[x]!='0':
        #print(players[x]+" "+str(count+1))
        # remove character at the index x
        players.remove(players[x])
        # insert 0 at index x
        players.insert(x, '0')
        # increment player remove count
        rem_count += 1
        # increment count
        count+=1
    # if the element is not removed element
    elif players[x]!='0':
        # increment count
        count+=1
    # increment array indexing variable
    x+=1
    # mod with length to made x inside the list bound
    x%=len(players)
# printing winner
print(str("Winner = "),end='')   
for i in players:
    if(i!='0'):
        print(i)