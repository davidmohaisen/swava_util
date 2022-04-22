import matplotlib.pyplot as plt


f1 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq02.csv', 'rb')
f2 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq03.csv', 'rb')
f3 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq04.csv', 'rb')
f4 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq05.csv', 'rb')
f5 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq06.csv', 'rb')
f6 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq07.csv', 'rb')
f7 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq08.csv', 'rb')
f8 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq09.csv', 'rb')
f9 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq10.csv', 'rb')
f10 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq11.csv', 'rb')
f11 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq12.csv', 'rb')
f12 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq13.csv', 'rb')
f13 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq14.csv', 'rb')
f14 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq15.csv', 'rb')
f15 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq16.csv', 'rb')
f16 = open('/Users/afsahanwar/tmp/disclosure_date/reference_freq17.csv', 'rb')


def output_array_creater(out):
    csv_out = '/Users/afsahanwar/tmp/disclosure_date/reference_freq_aggr.csv'
    with open(csv_out, "a") as output:

        output.write(out)


        # writer.writerows(cout) 
              

    return;


url_freq={}
def csv_aggregator(f):
	for line in f:
		tokens = line.rsplit(",")
		a = tokens[0].rstrip()
		b = tokens[1].rstrip()
		# print b
		if a in url_freq:
			url_freq[a] = int(url_freq[a])+int(b)
		else:
			url_freq[a] = b

def main():
	csv_aggregator(f1)
	csv_aggregator(f2)
	csv_aggregator(f3)
	csv_aggregator(f4)
	csv_aggregator(f5)
	csv_aggregator(f6)
	csv_aggregator(f7)
	csv_aggregator(f8)
	csv_aggregator(f9)
	csv_aggregator(f10)
	csv_aggregator(f11)
	csv_aggregator(f12)
	csv_aggregator(f13)
	csv_aggregator(f14)
	csv_aggregator(f15)
	csv_aggregator(f16)

	for item in url_freq:
		out = item+","+str(url_freq[item])+'\n'
		output_array_creater(out)



if __name__ == "__main__":
    main()

		
