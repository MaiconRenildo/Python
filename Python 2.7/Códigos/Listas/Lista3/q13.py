satisfacao=raw_input('Voce esta satisfeito com o produto: ')
satisfeito=0
insatisfeito=0
while satisfacao!='F':
    if satisfacao=='S':
        satisfeito+=1
    elif satisfacao=='N':
        insatisfeito+=1
    satisfacao=raw_input('Voce esta satisfeito com o produto: ')
total=satisfeito+insatisfeito
psim=(satisfeito*100)/float(total)
pnao=(insatisfeito*100)/float(total)
print 'Satisfeitos: ',psim,'%'
print 'Insatisfeitos: ',pnao,'%'
        
