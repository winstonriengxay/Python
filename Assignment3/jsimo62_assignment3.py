# Import CSV class to work with CSV files
import csv

#-----WORK WITH THE FILE---------------------------------------------------------------------------------#


with open('mpg.csv', newline='') as csvfile:
        f_mpg = csv.DictReader(csvfile)

        # initiate list
        ls_avg_cm_all, ls_avg_hm_all, ls_avg_hm_class, ls_avg_hm_manuf = [], [], [], []
        # initiate sets
        s_manuf, s_class = set(),set()

        ls_audi= []
        # Loop through csv
        for row in f_mpg:
            # Create a set of unique manufacurers and classes
            s_manuf.add(row['manufacturer'])
            s_class.add(row['class'])
            # append to specified list
            ls_avg_cm_all.append(int(row['cty']))
            ls_avg_hm_all.append(int(row['hwy']))

            if row['manufacturer'] == 'audi':
                ls_audi.append(int(row['hwy']))
            #elif row['manufacturer'] == 'chevrolet':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'dodge':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'ford':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'honda':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'hyundai':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'jeep':
            #    ls_chev.append(int(row['hwy']))
            #elif row['manufacturer'] == 'land rover':
            #    ls_chev.append(int(row['hwy']))
        ls_manufacturer = s_manuf
        ls_class = s_class
        #print(sorted(ls_manufacturer))
        #print(sorted(ls_class))
        #print(ls_audi)

        # Calculate the average for all vehicles
        calc_avg_cm_all = sum(ls_avg_cm_all)/len(ls_avg_cm_all)
        calc_avg_hw_all = sum(ls_avg_hm_all)/len(ls_avg_hm_all)
        calc_avg_hw_audi = sum(ls_audi)/len(ls_audi)
        # Make the sentence for all vehicles
        w_avg_cm_all = ('Out of all ' + str(len(ls_avg_cm_all))
            + ' vehicles, the average city mpg is ' + str(round(calc_avg_cm_all,2)) + '\n\n')
        w_avg_hm_all = ('Out of all ' + str(len(ls_avg_hm_all))
            + ' vehicles, the average highway MPG is ' + str(round(calc_avg_hw_all,2)) + '\n\n')

        w_avg_hm_audi = ('If we only look at the ' + str(len(ls_audi))
            + ' audis, the average highway MPG is ' + str(round(calc_avg_hw_audi,2)) + '\n\n')
        #-----PRINT TO TEXT FILE-----------------------------------------------------------------------------#
        # 1 - Create/Open File
        output = open('jsimo62_assignment3.txt', 'w+')
        # 2 - Write to file
        output.write(w_avg_cm_all)
        output.write(w_avg_hm_all)
        output.write(w_avg_hm_audi)
        output.close()

        #-----TEST OUTPUTS ----------------------------------------------------------------------------------#

        # Pring grouped by list to command newline
        #print(ls_avg_hm_manuf)
        #print(ls_avg_hm_class)


response = input("Would you like an average mpg of all cars or specfic groups of cars? (all / group) ")

if response == "all":
    # Print the sentences in command line
    print(w_avg_cm_all)
    print(w_avg_hm_all)
elif response =="group":
    # Print sets to command line
    print(s_manuf)
    print(s_class)
else:
    print("Input was not 'all' or 'group'. Good Bye.")