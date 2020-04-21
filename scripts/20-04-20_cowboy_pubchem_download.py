"""
downloading a batch of pubchem bioassay data tables cowboy style because the PUG-REST script I'm optimizing works
way too slowly and introduces errors into the downloaded data

in the meantime, I'm emailing PUG-REST to figure out if there's a more efficient way to do this using the PUG-REST
system
"""
import pandas as pd

# import record list
p = '../data/literature/KYHelal_etal_2016_JCIM_supplement.xlsx'
supp_table = pd.read_excel(p, engine='openpyxl')
id_list = supp_table['AID'].values

# define the base URL you're going to use for searching
base_url = 'https://pubchem.ncbi.nlm.nih.gov/'
base_url = base_url + 'assay/pcget.cgi?query=download&record_type=datatable&actvty=all&response_type=save&aid='
data_dir = '../data/1-raw/'

# loop over list of AIDs, read CSV, then save CSV
count = 1
for i in id_list:
    dl_url = base_url + str(i)
    temp_df = pd.read_csv(dl_url, index_col=0)
    temp_df.to_csv(data_dir + str(i) + '.csv')
    print('record {count} of {total} completed'.format(count=count,
                                                       total=len(id_list)))
    count += 1
