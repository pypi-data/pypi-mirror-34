def legal_moves(temp):
	z_index=temp.index(0)
	if(z_index==0):
		legal_moves_index=[1,3]
	if(z_index==1):
		legal_moves_index=[0,2,4]
	if(z_index==2):
		legal_moves_index=[1,5]
	if(z_index==3):
		legal_moves_index=[0,4,6]
	if(z_index==4):
		legal_moves_index=[1,3,5,7]
	if(z_index==5):
		legal_moves_index=[2,4,8]
	if(z_index==6):
		legal_moves_index=[3,7]
	if(z_index==7):
		legal_moves_index=[4,6,8]
	if(z_index==8):
		legal_moves_index=[5,7]
	return legal_moves_index
def main(initial_state):
	g_state=[1,2,3,
         4,5,6,
	 7,8,0]
	i_state=initial_state
	node_list=[i_state]
	poped_list=[]
	print("Initial State=",node_list)
	print("Goal State=",g_state)
	while(g_state not in node_list):
        	temp=node_list.pop()
        	print("Poped List=",temp)
        	poped_list.extend(temp)
        	q=[]
        	z_index=temp.index(0)
        	legal_moves_idx=legal_moves(temp)
        	#print("Legal moves",legal_moves_idx)
        	for i in legal_moves_idx:
        	        value=temp[i]
        	        temp[i],temp[z_index]=temp[z_index],temp[i]
        	        print("Added=",temp)
        	        q.extend(temp)
        	        temp[z_index],temp[i]=temp[i],temp[z_index]
        	for i in range(0,len(q),9):
        	        node_list.insert(0,q[i:i+9])
#       	 for k in range(0,len(node_list)):
 #      	         print("\n",node_list[k][0:3],"\n",node_list[k][3:6],"\n",node_list[k][6:9])
        	if g_state in node_list:
        	        position=node_list.index(g_state)
        	        print("Answer is At Position::",position,"In above list")
        	        break
