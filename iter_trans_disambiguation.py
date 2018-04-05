__author__ = "Pabitra Lenka"

from total_ngrams import unigram_all, bigram_all
stopwords = ['no', 'such', 'of', 'ma', 'the', 'him', 'is', 'having', 'couldn', 'o', 'haven', 'aren', 'should', 'shan', 'on', 'hadn', 'from', 'just', 'other', 've', 'yourselves', 'then', 'shouldn', 'through', 'above', 'doing', 'most', 're', 'won', 'did', 'your', 'don', 'only', 'its', 'and', 'doesn', 'myself', 'itself', 'their', 'a', 'this', 'or', 'by', 'will', 'd', 'with', 'there', 'does', 'these', 'own', 'because', 'at', 'he', 'while', 'me', 'be', 'more', 'yourself', 'as', 'here', 'our', 'them', 'very', 'up', 'so', 'his', 'to', 't', 'hers', 'for', 'out', 'all', 'mustn', 'once', 'ain', 'into', 's', 'not', 'himself', 'i', 'can', 'isn', 'an','wouldn', 'that', 'both', 'but', 'do', 'it', 'same', 'until', 'too', 'now', 'm', 'down', 'those', 'you', 'about', 'nor', 'weren', 'am', 'hasn', 'she', 'ourselves', 'was', 'theirs', 'themselves', 'my', 'll', 'mightn', 'are', 'had', 'herself', 'y', 'her', 'being', 'were', 'they', 'didn', 'been', 'off', 'ours', 'if', 'in', 'each', 'any', 'over', 'yours', 'further', 'than', 'we', 'wasn', 'needn', "'s"]

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

#Finding Most Probable Word
def best_word(hin, hinen, entrans, unigram, bigram, stopwords):
	for i in range(len(hin)):
		line_hin = hin[i].lower()
		line_hinen = hinen[i].lower()
		line_entrans = entrans[i].lower()

		text_hin = line_hin.split(" ")
		text_hinen = line_hinen.split(" ")
		text_entrans = line_entrans.split(" ")

		nf = open("filename.txt",'a+')
		if len(text_hinen) >= 3:
			tot = ""
			tot1 = []
			for word in text_hinen:
				if '|' in word:
					pos_hinen = text_hinen.index(word)
					pos_hin = pos_hinen
					pos_entrans = pos_hinen

					flag = 0
					terminate = 0
					if pos_hinen > 0 and pos_hinen < (len(text_hinen)-1):
						trans_q1 = text_entrans[pos_entrans - 1].split("|")
						trans_q2 = text_entrans[pos_entrans].split("|")
						trans_q3 = text_entrans[pos_entrans + 1].split("|")
						flag = 2

					elif pos_hinen == (len(text_hinen) - 1):
						trans_q1 = text_entrans[pos_entrans - 2].split("|")
						trans_q2 = text_entrans[pos_entrans - 1].split("|")
						trans_q3 = text_entrans[pos_entrans].split("|")
						flag = 3
						print (flag)

					elif pos_hinen == 0:
						trans_q1 = text_entrans[pos_entrans].split("|")
						trans_q2 = text_entrans[pos_entrans + 1].split("|")
						trans_q3 = text_entrans[pos_entrans + 2].split("|")
						flag = 1
						print (flag)

					#Stopword Removal
					tr_q1, tr_q2, tr_q3 = [], [], []
					for s in trans_q1:
						if s not in stopwords:
							tr_q1.append(s)
					
					if len(tr_q1) == 0:
						if len(trans_q1) > 1:
							for z in range(2):
								tr_q1.append(trans_q1[z])
						else:
							tr_q1.append(trans_q1[0])
					
					for s in trans_q2:
						if s not in stopwords:
							tr_q2.append(s)
					
					if len(tr_q2) == 0:
						if len(trans_q2) > 1:
							for z in range(2):
								tr_q2.append(trans_q2[z])
						else:
							tr_q2.append(trans_q2[0])
					
					for s in trans_q3:
						if s not in stopwords:
							tr_q3.append(s)
					
					if len(tr_q3) == 0:
						if len(trans_q3) > 1:
							for z in range(2):
								tr_q3.append(trans_q3[z])
						else:
							tr_q3.append(trans_q3[0])

					print (tr_q1)
					print (tr_q2)
					print (tr_q3)

					wt_q1_prev, wt_q2_prev, wt_q3_prev = [], [], []

					#Initialization step: All equal term weights are assigned 
					
					for j in range(len(tr_q1)):
						wt_q1_prev.append(1/len(tr_q1))
					for j in range(len(tr_q2)):
						wt_q2_prev.append(1/len(tr_q2))
					for j in range(len(tr_q3)):
						wt_q3_prev.append(1/len(tr_q3))
					
					
					# for j in range(len(tr_q1)):
					# 	wt_q1_prev.append(1/(j+1))
					# for j in range(len(tr_q2)):
					# 	wt_q2_prev.append(1/(j+1))
					# for j in range(len(tr_q3)):
					# 	wt_q3_prev.append(1/(j+1))
					
					print (tr_q1)
					print (wt_q1_prev)
					print (tr_q2)
					print (wt_q2_prev)
					print (tr_q3)
					print (wt_q3_prev)

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
							if sum_all < 0.000001:
								terminate = 1
								break

						#Threshold check to terminate updation
						if terminate == 1:
							#Finding the most probable translated word
							if flag == 1:
								if len(wt_q2_new) > 0:
									pos = wt_q1_new.index(max(wt_q1_new))
									tr_q1_best = tr_q1[pos]
									print (tr_q1_best)
									tot1.append(tr_q1_best)
							
							elif flag == 2:
								if len(wt_q2_new) > 0:
									pos = wt_q2_new.index(max(wt_q2_new))
									tr_q2_best = tr_q2[pos]
									print (tr_q2_best)
									tot1.append(tr_q2_best)

							elif flag == 3:
								if len(wt_q3_new) > 0:
									pos = wt_q3_new.index(max(wt_q3_new))
									tr_q3_best = tr_q3[pos]
									#print (tr_q3_best)
									tot1.append(tr_q3_best)
							print ("\n--------------------Finished----------------------\n")
							terminate = 0
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
	wt_final = []
	for i in range(len(tr_main)):
		dc = 0.0
		wt_total = 0.0
		for j in range(len(tr_linked)):
			dc_score = dice_coeff(unigram, bigram, tr_main[i], tr_linked[j]) * wt_linked[j]
			dc = dc + dc_score

		tot = wt_main[i] + dc
		wt_final.append(tot)

	#Weight Normalization as mentioned in the paper
	wt_total = sum(wt_final)
	for i in range(len(wt_final)):
		wt_final[i] = wt_final[i]/wt_total

	return wt_final	

#Calculating Dice Coefficient
def dice_coeff(unigram, bigram, word, word1):
	if (word, word1) in bigram and word in unigram and word1 in unigram:
		return ((2 * bigram[(word, word1)])/(unigram[word] + unigram[word1]))
	else:
		return 0


hin, hinen, entrans = [], [], []
hin.append("Text")
hinen.append("Text")
entrans.append("Text")
best_word(hin, hinen, entrans, unigram_all, bigram_all, stopwords)