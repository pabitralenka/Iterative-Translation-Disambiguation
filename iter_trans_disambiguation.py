__author__ = "Pabitra Lenka"

from collections import Counter

#Reading Text File
def read_file(arg1):
	hin = []
	with open(arg1) as rf:
		for line in rf:
			line = line.strip()
			line = line.strip("\n")
			line = line.lower()
			hin.append(line)

	return hin

#Generating Bigram
def generate_2grams(text, n):
	tokens = text.split(" ")
	outp = [(tokens[i],tokens[i+1]) for i in range(0,len(tokens)-1)]
	return outp

#Generating Unigram
def generate_1gram(text, n):
	tokens = text.split(" ")
	outp = [(tokens[i]) for i in range(0,len(tokens))]
	return outp

#Calculating Unigram and Bigram
def bigrams(tot_file):
	outp1 = generate_1gram(tot_file, 1)
	outp2 = generate_2grams(tot_file,2)

	count1 = Counter(outp1)
	count2 = Counter(outp2)
	key1_list = []
	for key in count1:
		key1_list.append(key)

	for key in count2:
		if key[0] in key1_list:
			count2[key] = count2[key]/count1[key[0]]

	return count1, count2

#Finding Most Probable Word
def best_word(hin, hinen, entrans, unigram, bigram):
	for i in range(len(hin)):
		line_hin = hin[i]
		line_hinen = hinen[i]
		line_entrans = entrans[i]

		text_hin = line_hin.split(" ")
		text_hinen = line_hinen.split(" ")
		text_entrans = line_entrans.split(" ")

		nf = open("new_file.txt",'a+')
		if len(text_hinen) >= 3:
			tot = ""
			tot1 = []
			for word in text_hinen:
				if '|' in word:
					pos_hinen = text_hinen.index(word)
					pos_hin = pos_hinen
					pos_entrans = pos_hinen

					flag = 0
					if pos_hinen - 2 >=0 :
						tr_q1 = text_entrans[pos_entrans - 2].split("|")
						tr_q2 = text_entrans[pos_entrans - 1].split("|")
						tr_q3 = text_entrans[pos_entrans].split("|")
						flag = 1
						"""
						dict_query = {}
						dict_query[text_hin[pos_hin - 2]] = text_entrans[pos_entrans - 2].split("|")
						dict_query[text_hin[pos_hin - 1]] = text_entrans[pos_entrans - 1].split("|")
						dict_query[text_hin[pos_hin]] = text_entrans[pos_entrans].split("|")
						"""

					elif pos_hinen + 2 <= len(text_hinen) - 1:
						tr_q1 = text_entrans[pos_entrans].split("|")
						tr_q2 = text_entrans[pos_entrans + 1].split("|")
						tr_q3 = text_entrans[pos_entrans + 2].split("|")
						flag = 2

					else:
						tr_q1 = text_entrans[pos_entrans - 1].split("|")
						tr_q2 = text_entrans[pos_entrans].split("|")
						tr_q3 = text_entrans[pos_entrans + 1].split("|")
						flag = 3


					wt_q1_prev, wt_q2_prev, wt_q3_prev = [], [], []

					#Initialization step: All equal term weights are assigned 
					for j in range(len(tr_q1)):
						wt_q1_prev.append(1/len(tr_q1))
					for j in range(len(tr_q2)):
						wt_q2_prev.append(1/len(tr_q2))
					for j in range(len(tr_q3)):
						wt_q3_prev.append(1/len(tr_q3))
					
					print (tr_q1)
					print (wt_q1_prev)
					print (tr_q2)
					print (wt_q2_prev)
					print (tr_q3)
					print (wt_q3_prev)

						#for i in range(len(value)):
							#wt_q[key][i] = {wt_q[key][i]:[0.2]} 

					wt_q1_new, wt_q2_new, wt_q3_new = [], [], []
					while True:
						wt_all_prev, wt_all_new = [], []

						wt_q1_new = weight_update(wt_q1_prev, wt_q2_prev + wt_q3_prev, tr_q1, tr_q2 + tr_q3, unigram, bigram)
						print (tr_q1)
						print (wt_q1_new)

						wt_q2_new = weight_update(wt_q2_prev, wt_q1_prev + wt_q3_prev, tr_q2, tr_q1 + tr_q3, unigram, bigram)
						print (tr_q2)
						print (wt_q2_new)

						wt_q3_new = weight_update(wt_q3_prev, wt_q1_prev + wt_q2_prev, tr_q3, tr_q1 + tr_q2, unigram, bigram)
						print (tr_q3)
						print (wt_q3_new)

						wt_all_prev.extend(wt_q1_prev)
						wt_all_prev.extend(wt_q2_prev)
						wt_all_prev.extend(wt_q3_prev)

						wt_all_new.extend(wt_q1_new)
						wt_all_new.extend(wt_q2_new)
						wt_all_new.extend(wt_q3_new)

						sum_all = 0
						for g in range(len(wt_all_new)):
							sum_all = abs(wt_all_new[g] - wt_all_prev[g])

						#Threshold check to terminate updation
						th = 0.000001
						#print (sum_all)
						if sum_all < th:
						#if wt_q1_new[0] - wt_q1_prev[0] < th or wt_q2_new[0] - wt_q2_prev[0] < th or wt_q3_new[0] - wt_q3_prev[0] < th:
							#Finding the most probable translated word
							if flag == 1:
								pos = wt_q3_new.index(max(wt_q3_new))
								tr_q3_best = tr_q3[pos]
								tot1.append(tr_q3_best)
							elif flag == 2:
								pos = wt_q1_new.index(max(wt_q1_new))
								tr_q1_best = tr_q1[pos]
								tot1.append(tr_q1_best)
							elif flag == 3:
								pos = wt_q2_new.index(max(wt_q2_new))
								tr_q2_best = tr_q2[pos]
								tot1.append(tr_q2_best)
							print ("\n--------------------Finished----------------------\n")
							break

						wt_q1_prev = wt_q1_new
						wt_q2_prev = wt_q2_new
						wt_q3_prev = wt_q3_new


				else:
					tot1.append(word)

			tot = " ".join(tot1) + "\n"
			nf.write(tot)

		else:
			tot = " ".join(text_hinen) + "\n"
			nf.write(tot)

	nf.close()


#Updating Weights
def weight_update(wt_main, wt_linked, tr_main, tr_linked, unigram, bigram):
	#Iteration step as mentioned in the paper
	wt_total = 0.0
	dc = 0.0
	wt_final = []
	for i in range(len(tr_main)):
		for j in range(len(tr_linked)):
			dc = dc + dice_coeff(unigram, bigram, tr_main[i], tr_linked[j]) * wt_linked[j]

		tot = wt_main[i] + dc
		wt_final.append(tot)
		wt_total = wt_total + wt_final[i]

	#Weight Normalization as mentioned in the paper
	for i in range(len(wt_final)):
		wt_final[i] = wt_final[i]/wt_total

	return wt_final	

#Calculating Dice Coefficient
def dice_coeff(unigram, bigram, word, word1):
	if (word, word1) in bigram and word in unigram and word1 in unigram:
		return ((2 * bigram[(word, word1)])/(unigram[word] + unigram[word1]))
	else:
		return 0

