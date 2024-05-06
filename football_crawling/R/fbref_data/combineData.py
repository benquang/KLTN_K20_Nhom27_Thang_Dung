folder_dirs = [
        './ENG_fbref_2018', 
        './ENG_fbref_19_24',
        './ESP_fbref_18_23',
        './ESP_fbref_24',
        './FRA_fbref',
        './GER_fbref_18_19',
        './GER_fbref_20_24',
        './ITA_fbref_18_20',
        './ITA_fbref_21_24',
    ]
files = ['/advanced_match_stats.csv',
         '/match_lineups.csv',
         '/match_results.csv',
         '/match_stats.csv',
         '/match_summary.csv',]
dest_folder = './fbref'

def combineData(file_dir, dest_dir):
    with open(file_dir, 'r',encoding="utf8") as f:
        data = f.readlines()
        f.close()
    with open(dest_dir, 'a',encoding="utf8") as f:
        f.writelines(data[1:])
        f.close()

for folder_dir in folder_dirs:
    for file in files:
        file_dir = folder_dir + file
        dest_dir = dest_folder + file
        combineData(file_dir, dest_dir)

