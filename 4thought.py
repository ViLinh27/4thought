possOps = ['+','*','-','//']
m=int(input())
finalexpr = {}
for i in range(0,m):
    n_testnum = int(input())
    for op1 in possOps:#generate all poss ops for first op
        for op2 in possOps:#generate all poss ops for second op
            for op3 in possOps:#generate all poss ops for third op
                expr = f'4 {op1} 4 {op2} 4 {op3} 4'
                answer = eval(expr)
                expr = expr.replace('//','/')
                fullexpr = f'{expr} = {answer}'
                
                finalexpr[answer] = fullexpr
                    
    if n_testnum < -1000000 & n_testnum > 1000000 or n_testnum not in finalexpr:#if no possible solution
        print('no solution')
    else:
        print(finalexpr[n_testnum])
