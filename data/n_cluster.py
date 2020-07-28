import csv
from sklearn_extra.cluster import KMedoids
from kneed import KneeLocator
import statistics as math

cluster_list = []

path=os.getcwd()
target = 'Training-Set-2018/'

entries = os.listdir(target)

for entry in entries:
	if entry == 'FilterSent':
		continue
	temPath = path+'/'+target+entry+'/Reference_XML/'
	print(temPath)
	temPath2 = glob.glob(temPath+'*.csv')[0]
	print(temPath2)
	csv_file = temPath2
	filename = temPath2.split('/')[-1]
	print(temPath2)
	print(filename)

	# print(inputFile)
	# outpath = temPath+filename.rstrip(".xml") + ".csv"
	# print(outpath)

	model = SentenceTransformer('bert-base-nli-mean-tokens')

	out_dir = path+"/embeddnings"
	if not os.path.exists(out_dir): os.mkdir(out_dir)

	def generate_embedding(inp_file, out_file):
	    # with open(inp_file, encoding='latin') as f:
	        # soup = bs(f.read())
	        # sentences = list(map(lambda x: x.text, soup.find_all("s")))
	    df = pd.read_csv(inp_file)
	    sentences = df['sentence']
	    embd = np.array(model.encode(sentences))

	    with open(out_file, "wb") as nf:
	        np.save(nf, embd)
	    
	    return sentences, embd

	out_file = os.path.join(out_dir, os.path.basename(csv_file).replace(".csv", ".npy"))
	sentences, data = generate_embedding(csv_file, out_file)
	
	wcss = []
	for i in range(1,10):
		km1 = KMedoids(n_clusters=i, metric = 'cosine', random_state= 42)
		km1.fit(x)
		wcss.append(km1.inertia_)


	# plt.plot(range(1,10),wcss)
	# plt.title('The Elbow Method')
	# plt.xlabel('Number of clusters')
	# plt.ylabel('WCSS')
	# plt.show()

	kneedle = KneeLocator(range(1,10),wcss, S=1.0, curve='convex', direction='decreasing')

	print(round(kneedle.knee, 3))
	print(round(kneedle.elbow, 3))
	kneedle1 = KneeLocator(range(1,10),wcss, S=1.0, curve='concave', direction='decreasing')
	print(round(kneedle1.knee, 3))
	print(round(kneedle1.elbow, 3))
	n_cluster = round((kneedle1.elbow + kneedle.elbow)/2)
	print(n_cluster)

	cluster_list.append(round(kneedle.elbow, 3))


avg_cluster = math.mean(cluster_list)
print(avg_cluster)



	