import os
import subprocess as sp

############## ALGEMENE FUNCTIES ################

def stringInFile(file_name, string_to_search):
    with open(file_name, 'r') as file:
        for line in file:
            if string_to_search in line:
                return True
    return False

def appendToFile(file_name,list_of_strings):
    with open(file_name,"a") as file:
        for line in list_of_strings:
            file.write(line)

#################################################

def blastPresent():
    if ncbi_folder not in os.listdir(home_directory):# bestaat de ncbi folder al? indien False download en installeer
        try:
            sp.run(["wget","https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/"+ncbi_folder+"-x64-linux.tar.gz"])
        except:
            print("Downloading blast failed")
            exit()
        sp.run(["tar","-xzvf",ncbi_folder+"-x64-linux.tar.gz"])
        sp.run(["rm",ncbi_folder+"-x64-linux.tar.gz"])
        os.chdir(ncbi_folder)
        os.mkdir("blastdb")
        os.chdir("blastdb")
        os.mkdir("db")
        os.chdir("db")
        print("Added blastdb/db to {} folder".format(ncbi_folder))
    else:
        print("Blast+ is already installed: Checking next step...")
            
def installingDatabases():
    if "swissprot.pdb" not in os.listdir(database_folder):
        try:
            os.chdir(database_folder)
            sp.run(["wget","https://ftp.ncbi.nlm.nih.gov/blast/db/swissprot.tar.gz"])
            sp.run(["tar","-xzvf","swissprot.tar.gz"])
            sp.run(["rm","swissprot.tar.gz"])
            os.chdir(os.path.expanduser("~"))
        except:
            print("Downloading swissprot database failed")
            exit()
    else:
        print("swissprot.pdb is already installed: Checking next step...")
    
def checkBashrc():
    os.chdir(os.path.expanduser("~"))
    check = []
    strings = ['export PATH="'+home_directory+ncbi_folder+'/bin:$PATH"','export BLASTDB="'+database_folder+':$BLASTDB"']

    for i in strings:
        check.append(stringInFile(home_directory+bashrc,i))

    if check == [True,True]:
        print("{} and {} are already added to path:\n".format(ncbi_folder+"/bin",database_folder))
    else:
        appendToFile(home_directory+bashrc,["\n","### BLAST ###\n",'export PATH="'+home_directory+ncbi_folder+'/bin:$PATH"\n','export BLASTDB="'+database_folder+':$BLASTDB"\n',"### ----- ###"])
        print("Added Blast+ requirements to {} file".format(bashrc))
  
if __name__ == '__main__':

    os.chdir(os.path.expanduser("~")) # make sure the scripts starts in the home directory of the user
    sp.run(["cp",".bashrc",".bashrc_old"]) #make backup just in case
    
    ### Global Variabels ###
    ncbi_folder = "ncbi-blast-2.12.0+"
    home_directory = str(os.getcwd()+"/") #os.environ['HOME']
    database_folder = str(home_directory+ncbi_folder+"/blastdb/db")
    bashrc = ".bashrc"
    ### --------------- ###

    ### Checks ###
    blastPresent()
    installingDatabases()
    checkBashrc()
    ### ------ ###

    print("Installation completed!")
    print("PLEASE RESTART YOUR TERMINAL!")
