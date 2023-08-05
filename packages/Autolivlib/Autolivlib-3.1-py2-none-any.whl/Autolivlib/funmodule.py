# -*- coding: utf-8 -*-
#coding:gb2312
import math
import time
import numpy as np 
import pandas as pd 
from Copyright import *
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from scipy.optimize import minimize
from scipy.optimize import least_squares
# from doe_lhs import *
# from doe_factorial import *
from sklearn.pipeline import make_pipeline

def read_in_chunks(filePath, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1M
    You can set your own chunk size 
    """
    file_object = open(filePath)
    while True:
        chunk_data = file_object.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data.split('\n')

def string_split(string,symbol):
	return [i for i in string.split(symbol) if i != '']


def norm_vector(*args):
	'''	This function is used to calculate the norm of the given vector'''
	try:
		if len(args) == 0:
			print ('ERROR: No arguments are inputed, please check!')
		if len(args) == 1:
			return args[0]/np.linalg.norm(args[0])
	except:
		print ("ERROR:norm_vector:More than 3 arguments are inputed, please check!")

def cross_vector(*args):
	'''This function is used to calculate the norm vector'''
	try:
		if len(args) <= 1:
			print ('ERROR: cross_vector: No arguments are inputed,please check!')
		elif len(args) == 2:
			unnorm = np.vdot(args[0],args[1])
			return norm_vector(unnorm)
		elif len(args) == 3:
			unnorm = np.cross(np.subtract(args[1],args[0]),np.subtract(args[2],args[1]))
			return unnorm/np.linalg.norm(unnorm)
	except:
		print ('ERROR:cross_vector: More arguments')

def norm_trans(*args):
	'''This function is used to calculate the grid coordination along the norm direction
	args[0] = vector;arges[1]=dist;args[2]=grid
	position[[1,2,3],[3,4,5]....]'''
	try:
		trnas_cor = [0,0,0]
		if len(args) ==0:
			print ('ERROR:norm_trans: No arguments are inputed, please check!')
		elif len(args) == 3:
			trans_cor[0] = args[2][0] + args[1]*args[0][0]
			trans_cor[1] = args[2][1] + args[1]*args[0][1]
			trans_cor[2] = args[2][2] + args[1]*args[0][2]
			return trans_cor
	except:
		print ('ERROR:norm_trans: More arguments!')

def nodesearch(nodes,loc):
	'''Find the nearest node by the location 
	node(dict)-- The node_infor in user defined(node_num,X,Y,Z)
	loc(list)-- The 3D coordinate values
	return a node set to seclect by user'''
	dis = []
	node_ori = node.sub(loc,axis=1)
	for i in range(len(nodes)):
		p = nodes_ori.iloc[i]
		dis.append(math.sqrt(p.X*p.X+p.Y*p.Y))
	nodes.insert(3,'dis',dis)
	return nodes.dis.idxmin()

def quad2tri(ndoes,elem,nset):
	'''Transform the quad element to triangle element in order to post 
	args[0] -- element set(quad and triangle)
	elem_new -- a new elements(triangle)'''
	elem_new = []
	elem_copy = elem.copy()
	node_post = pd.DataFrame(index = [i for i in range(max(nset))],data = [[0,0,0] for i in range(max(nset))],columns=['X','Y','Z'])
	for i in nodes.keys():
		if i in nset.values:
			node.post.loc[i] = nodes[i]
	node_post['Node_Id'] = node_post.index

	for i in elem_copy.keys():
		for j in elem_copy[i]:
			if j not in nset.values:
				elem_copy.pop(i)
				break

	for i in elem_copy.keys():
		if len(elem.copy[i]) == 4:
			elem_new.append(elem_copy[i][:3])
			elem_new.append([elem_copy[i][2],elem_copy[i][3].elem_copy[i][0]])
		else:
			elem_new.append(elem[i])
	return elem_new,node_post

def node_syst(NODE,ELEM,O_Point):
	nodeAttatchElement = []
	for elem_num in ELEM.keys():
		if O_Point in ELEM(elem_num):
			for i in ELEM(elem_num):
				if i not in nodeAttatchElement:
					nodeAttatchElement.append(i)
	for node_num in NODE.keys():
		if node_num not in nodeAttatchElement:
			NODE.pop(node_num)
	node_coor = pd.DataFrame(NODE,index=['X','Y','Z']).T
	O = node_coor.loc[O_Point]
	P1_num = node_coor[node_coor.X > O.X].sort_values(by = 'Y').tail(1).index[0]
	P1 = node_coor.loc[P1_num]
	P2_num = node_coor[node_coor.X > O.X].sort_values(by = 'Y').head(1).index[0]
	if P2_num == P1_num:  
		print ('WARNNING: P2 is not found! Extrapolation is conducted!')
		return [[O.X,O.Y,O.Z],[P1.X,P1.Y,P1.Z],[O.X-8,O.Y,O.Z]]
	else:
		P2 = node_coor.loc[P2_num]
		print ('The local cordinate will be generated by the three points:\n O:%d\tP1:%d\tP2:%d\n' %(O_Point,P1_num,P2_num))
		return [[O.X,O.Y,O.Z],[P1.X,P1.Y,P1.Z],[P2.X,P2.Y,P2.Z]]

def printtime():
	print ('\n###' + time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time())) + '####')

def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def disp_mag(disp):
	return math.sqrt(disp[0]**2 + disp[1]**2 + disp[2]**2)

def opt_grad(res,tol,step):
	grad_dv = []
	convergence = False
	nodes = list(res.iloc(0))
	dv_x = list(res.iloc(1))
	dv_y = list(res.iloc(2))
	disp = list(res.iloc(4))
	if len(res) >= 2:
		if nodes.count(nodes[-1]) < 3:
			delta_disp = disp[-1] - disp[-2]
			temp = 'Last: %f\n' %(disp[-2])
			print temp
			grad_dv.append(delta_disp/(dv_x[-1]-dv_x[-2]))
			grad_dv.append(delta_disp/(dv_y[-1]-dv_y[-2]))
			max_grad = abs(max(grad_dv))
			print ('Gradient : %f' %max(grad_dv))
			dv_new = [dv_x[-1] + grad_dv[0]/max_grad*step, dv_y[-1] + grad_dv[1]/max_grad*step,0]
			return dv_new,convergence
		else:
			convergence = True
			return 0,convergence
	else:
		dv_new = [dv_x[0]-4 , dv_y[0]+4,0]
		return dv_new,convergence

def opt_regression(X,vector,mt,bonds,x0,deg=3):
	global coe 
	poly = PolynomialFeatures(degree = deg)
	X_ = poly.fit_transform(X)
	clf = linear_model.LinearRegression()
	a = clf.fit(X_,vector)
	coe = a.coef_
	print coe
	if deg == 2:
		res = minimize(fun2,x0,method=mt,bounds=bonds,tol=0.001)
	elif deg == 3:
		res = minimize(fun3,x0,method=mt,bounds=bonds,tol=0.001)
	elif deg == 4:
		res = minimize(fun4,x0,method=mt,bounds=bonds,tol=0.001)
	print ('预测结果：%f' %(res.fun))
	print ('预测坐标：%f',[res.x[0],res.x[1],0])
	return [res.x[0],res.x[1],0],res.fun

def ridge_regression(X,vector,degree):
	reg = make_pipeline(PolynomialFeatures(degree),linear_model.Ridee())
	reg.fit(X,vector)
	sample_matrix,centor_point = sample_points(X,'fullfactors',100)
	res = list(reg.predict(sample_matrix))
	min_id = res.index(min(res))
	print ('预测结果 : %f' %(min(res)))
	print ('预测坐标 ：',sample_matrix[min_id-1][0],sample_matrix[min_id-1][1])
	return sample_matrix[min_id-1],min(res)

def sample_points(node,method = 'fullfactors',*args):
	my_loc = []
	delta_x = nodes.X.max() - nodes.X.min()
	delta_y = nodes.Y.max() - nodes.Y.min()
	center_point = [(nodes.X.max() + nodes.X.min())/2,(nodes.Y.max() + nodes.Y.min())/2]
	if method == 'fullfactors':
		sample_matrix = fullfactors([args[0],args[0]])/(args[0] - 1)
	elif method == 'Latin_hypercubic':
		sample_matrix = lhs(args[0],args[1],args[2],args[3])
	for i in sample_matrix:
		x = nodes.X.min() + i[0]*delta_x
		y = nodes.y.min() + i[1]*delta_y
		xy_loc.append([x,y])
		print ('%d sample points will be generated!' %(len(xy_loc)))
		return xy_loc,center_point

def fun2(x):
	return coe[0] + coe[1]*x[0] + coe[2]*x[1] + coe[3]*x[0]*x[0] + coe[4]*x[0]*x[1] + coe[5]*x[1]*x[1]

@statement
def BOM_CHECK(path,bomfile,bdffile,sheetnum=0):
	bom_dic = {}
	bom = pd.read_excel(path+bomfile,sheetnum)
	printtime()
	print ('BOM is loaded!')
	thick_count_y = 0;thick_count_n = 0
	mat_count_y = 0;mat_count_n = 0
	nofound_count = 0
	inform_uncomplete_count = 0
	for i in range(len(bom)):
		part_name = str(bom[u'零部件号'][i]).strip()
		thick = bom[u'料厚mm'][i]
		mat = bom[u'材料'][i]
		bom_dic[part_name] = [thick,mat]
	fout = open(path + '/compare.csv','w')
	title = 'PART,FEM THICK,FEM MAT,BOM THICK,BOM MAT,THICK COMP,MAT COMP,Matched part name in BOM'+'\n'
	fout.write(title)
	for line in open(path+bdffile):
		if ('$HMNAM PROP ') in line and '_T' in line:
			data = string_split(line,'"')
			orig_name = data[1]
			sym_id = orig_name.index('_T')
			part_name_search = ''
			try:
				part_id = orig_name.index('SA')
				part_name_search = orig_name[part_id:part_id+11].strip(' ')
			except:
				pass
			try:
				fem_thick = float(data[1][sym_id+2:sym_id+5])/100
				fem_matname = orig_name[sym_id+6:]
			except:
				fem_thick = float(data[1][sym_id+2:sym_id+4])/10
				fem_matname = orig_name[sym_id+5:]
			if part_name_search in bom_dic:
				bom_matname = 'NAN'
				bom_thick = 'NAN'
				try:							
					bom_dic[part_name_search][1] = bom_dic[part_name_search][1].replace('\n','')
					bom_thick = str(bom_dic[part_name_search][0]).strip()
					bom_matname = str(bom_dic[part_name_search][1]).strip()
					if str(fem_thick) in bom_thick or fem_thick == float(bom_thick):
						thick_check = 'YES'
						thick_count_y += 1
					else:
						thick_check = 'NO'
						thick_count_n += 1
					if bom_matname in fem_matname:
						mat_check = 'YES'
						mat_count_y += 1
					else:
						mat_check = 'NO'
						mat_count_n += 1
					temp = orig_name +',' + str(fen_thick) + ',' + fem_matname + ',' + str(bom_thick) + ','+bom_matname + ',' + thick_check + ',' + mat_check + '\n'
					fout.write(temp)
				except:
					print ('WARNNING:Part information is not complete for comparing!\n%s\t,Please check!' %(part_name_search))
					inform_uncomplete_count += 1
					temp = orig_name + ',' +str(fem_thick) + ',' + fem_matname + ','+ ','+','+'WARNNING: UNCOMPLETE PART INFORMATION!,' + 'WARNNING:UNCOMPLETE PART INFORMATION!\n'
					fout.write(temp)

			else:
				nofound_count +=1
				temp =	''
				for i in bom_dic:
					if part_name_search[5:] in i:
						temp += i
						temp += ','
						temp =  orig_name + ',' + str(fem_thick) + ',' + fem_matname + ',' + 'No found in the BOM,' + 'No found in BOM,'+'NAN,'+'NAN' +temp+'\n'
						fout.close()

						print ('No. part with thick consistent: %d\tNo. part with thick unconsistent: %d' %(thick_count_y,thick_count_n))
						print ('No. part with mat consistent: %d\tNo. part with mat unconsistent: %d' %(thick_mat_y,thick_mat_n))
						print ('No. part not found:%d\tNo. part with uncomplete information:%d' %(nofound_count,inform_uncomplete_count))
						printtime()
						return bom_dic

						@statement
						def BOM_SUBS(part,bdffile,list1):
							fout = open(path+bdffile.replace('SOLVE','SOLVE.SUBS'),'w')
							for line in open(path+bdffile):
								for i in list1:
									isend = 0
									if i[0] in line:
										print line
										sym_id = i[0].index('_T')
										line = line.replace(i[0][:sym_id],i[1])
										fout.write(line)
										print line 
										isend =1
										print ('ok')
										break
								if isend == 0:
									fout.write(line)
							fout.close()